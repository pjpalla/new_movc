__author__ = 'pg'
import numpy
import pandas
import re
import os
import glob
from movc.province_data import *
from _datetime import date
from movc.movutility import MovUtility
from movc.exceptions import IllegalArgumentError
from movc import province_data


MAPPER_IDX = (1, 2, 3, 4, 5)
class Movc:
    """
    This class allows to build the MOVC for the new Sardinian provinces
    """
    def __init__(self, month, year):
            self.month = month
            self.year = year


    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def set_mapper(self, file_path):
        try:
            self.mapper = pandas.read_csv(file_path, encoding = 'ISO-8859-1', sep=';', usecols=MAPPER_IDX)
            self.mapper.columns = ["prov_new", "com_new", "com_name", "com_old", "prov_ old"]
        except FileNotFoundError:
            print("The file does not exist!")

    def get_mapper(self):
        return self.mapper

    def set_input_dir(self, input_dir_path):
        dir = os.path.join(input_dir_path)
        if os.path.exists(dir):
            self.input_dir = dir
        else:
            raise NotADirectoryError("Invalid directory!")

    def get_input_dir(self):
        return self.input_dir

    def set_output_dir(self, output_dir_path):
        dir = os.path.join(output_dir_path)
        if os.path.exists(dir):
            self.output_dir = dir
        else:
            raise NotADirectoryError("Invalid directory")

    def get_output_dir(self):
        return self.output_dir

    def __merge_movs(self, year, month):
        #input_dir = MovUtility.config_io_paths(year, month)[0]
        month = str(month)
        if len(str(month)) == 1:
            month = '0' + month

        base_dir = os.path.join(str(year), str(month))
        input_dir = os.path.join(self.get_input_dir(), base_dir)
        output_filename = 'all_' + month + str(year) + '.txt'

        if not (os.path.isdir(input_dir)):
            raise NotADirectoryError("Invalid input directory!")
        elif len(os.listdir(input_dir)) < province_data.OLD_PROVINCE_NUMBER:
            raise Exception(
                "Insufficent number of old movc modules.\nTo generate new movc modules you must provide the modules of the eight old provinces.")

            ##      filenames of the movc modules contained in the source dir
        mov_files = glob.glob(input_dir + "/movc*")
        if not os.path.exists(input_dir):
            raise NotADirectoryError("Invalid output directory!")

        print("\nMerging movc modules of the old provinces into one global file. This might take a while...\n")
        with open(os.path.join(input_dir, output_filename), 'wb') as ofile:
            for f in mov_files:
                with open(f, 'rb') as infile:
                    ofile.write(infile.read())

        ofile.close()
        print("\n... Mov/c config merged!")
        return os.path.join(input_dir, output_filename)


    def create_movc(self, province_name):

        generated_movc = []
        merged_movc = self.__merge_movs(self.year, self.month)

        new_province_code = None
        provincial_symbol = None
        province = province_name.lower()
        if (re.search('città|metropolitana|cagliari', province)):
            new_province_code = NEW_CODES["cagliari"]
            provincial_symbol = PROVINCIAL_SYMOBOLS["cagliari"]
        elif (re.search('sud|sardegna', province)):
            new_province_code = NEW_CODES["sud sardegna"]
            provincial_symbol = PROVINCIAL_SYMOBOLS["sud sardegna"]
        elif (re.search('sassari', province)):
            new_province_code = NEW_CODES["sassari"]
            provincial_symbol = PROVINCIAL_SYMOBOLS["sassari"]
        elif (re.search('oristano', province)):
            new_province_code = NEW_CODES["oristano"]
            provincial_symbol = PROVINCIAL_SYMOBOLS["oristano"]
        elif (re.search('nuoro', province_name)):
            new_province_code = NEW_CODES['nuoro']
            provincial_symbol = PROVINCIAL_SYMOBOLS["nuoro"]

        prov_mapper = self.mapper[self.mapper['prov_new'] == new_province_code]


        # i = 0
        print("\nGenerating MOV/C\nThe operation might take a few minutes....\n\n\n")
        for index, row in prov_mapper.iterrows():
            com_old_code = row['com_old']
            com_new_code = row['com_new']

            if len(com_old_code) < 6:
                com_old_code = '0' + com_old_code
            if len(com_new_code) < 6:
                com_new_code = '0' + com_new_code



            with open(merged_movc, 'r+') as infile:
                for irow in infile:
                  if (irow[7:13] == com_old_code):
                      new_row = irow[0:7] + com_new_code + irow[13:len(irow)]
                      generated_movc.append(new_row)
            infile.close()        # print("new row: " + irow[7:13])


        #### Output file ####
        # TODO: aggiungere uno zero in testa a month qunado è costituito da una sola cifra ####
        if len(str(self.month)) == 1:
            self.month = '0' + str(self.month)
        output_base_filename = "movc_" + provincial_symbol + "_" + str(self.month) + str(self.year)
        base_dir = os.path.join(str(self.year), self.month)
        output_dir =  os.path.join(self.get_output_dir(), base_dir)
        output_filename = os.path.join(output_dir, output_base_filename) + ".txt"


        with open(output_filename, 'w') as ofile:
            for item in generated_movc:
                ofile.write(str(item))
        ofile.close()

        print("... MOV/C correctly created!\n")


    def validate(self, movc_file_generated):
        prov_code = None
        com_codes = []
        rows = []
        if not(os.path.exists(movc_file_generated)):
            raise FileNotFoundError("Move/C module not found!")

        with open(movc_file_generated, 'r') as ifile:
            prov_code = ifile.readline()[7:10]
            prov_code = prov_code[1:] if prov_code[0] == '0' else prov_code
            for row in ifile:
                rows.append(row)
                com_code = row[7:13]
                if com_code[0] == '0':
                    com_code = com_code[1:len(com_code)+1]

                com_codes.append(com_code)
        ifile.close()
        com_codes = list(set(com_codes))

        if prov_code == '92':# città metropolitana
            prov_code = '2' + prov_code
        mapper = self.mapper[self.mapper['prov_new'] == prov_code]
        nrows = mapper.shape[0]
        all_com_codes = mapper.ix[:, 'com_new'].tolist()

        missing_codes = [item for item in all_com_codes if item not in com_codes]
        missing_districts = self.mapper.ix[self.mapper['com_new'].isin(missing_codes), 'com_name'].tolist()


        province_name = self.get_province_name(prov_code)

        print("\n***** Mov/c Validation Report *****")
        print("\n***** Provincia: " + province_name.upper() + " *****\n" )

        print("* Numbero di Comuni della provincia: " + str(len(all_com_codes)))
        print("\n* Numero di Comuni non presenti nel MOV/C corrente: " + str(len(missing_codes)))
        print("\n* Comuni mancanti: " + str(missing_districts))
        print("\n***** Formato Dati *******")
        print("\n* Numero totale righe: " + str(len(rows)))
        print("\n* Lunghezza righe: " + str(len(rows[0].rstrip())))
        print("\n* Righe duplicate: " + str(self.get_duplicate_lines(rows)))
        print("\n**********************************************************\n")
        # print("first row: " + rows[0][1:20])
        # print("last row: " + rows[-1][1:20])


    def get_province_name(self, new_code):
        new_code = str(new_code)
        allowed_codes = NEW_CODES.values()
        if new_code not in allowed_codes:
            raise IllegalArgumentError("Wrong province code!")

        province_name = list(NEW_CODES.keys())[list(NEW_CODES.values()).index(new_code)]
        if province_name == 'cagliari':
            province_name = "città metropolitana di cagliari"
        return province_name


    def get_duplicate_lines(self, file_rows):
        row_set = set(file_rows)
        return len(file_rows) - len(row_set)




