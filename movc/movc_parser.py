__author__ = 'pg'
import os
import pandas
from movc import consts
from movc.movc_fields import *
from movc.province_data import *

MAPPER_IDX = (1, 2, 3, 4, 5)

class MovcParser:
    def __init__(self, movc_file, mapper_file):
        if not (os.path.exists(movc_file) or os.path.exists(mapper_file)):
            print("Invalid path to movc or mapper")
            return

        self.movc_path = movc_file
        self.mapper_path = mapper_file

#### ToDo: Implementare un decorator per la gestione della sessione
    def open_session(self):
#         self.movc = open(self.movc_path, mode='r')
         self.mapper = pandas.read_csv(self.mapper_path, encoding='ISO-8859-1', sep=';', usecols=MAPPER_IDX)
         self.mapper.columns = ["prov_new", "com_new", "com_name", "com_old", "prov_ old"]

    def close_session(self):
        self.movc.close()
        self.mapper = None

    def get_movc_blocks(self, size = 90):
        movc_file = open(self.movc_path, mode='r')
        movc = movc_file.readlines()
        ####lambda function
        splitter = lambda lst, sz: [movc[i:i + sz] for i in range(0, len(lst), sz)]
        blocks = splitter(movc, size)
        movc_file.close()
        return(blocks)

    def get_year(self, file_block):
        year = file_block[0][YEAR_START:YEAR_END]
        return (year)

    def get_month(self, file_block):
        month = file_block[0][MONTH_START:MONTH_END]
        if len(month) > 1 and month[0] == '0':
            month = month[1]
        return(month)

    def get_province(self, file_block):
        codice_comune = self.get_comune(file_block)[1]
        codice_provincia = (self.mapper['prov_new'].loc[self.mapper['com_new'] == codice_comune]).values[0]

        allowed_codes = NEW_CODES.values()
        if codice_provincia not in allowed_codes:
            print("Wrong province code!")
            return

        nome_provincia = list(NEW_CODES.keys())[list(NEW_CODES.values()).index(codice_provincia)]
        if nome_provincia == 'cagliari':
            nome_provincia = "città metropolitana di cagliari"
        elif nome_provincia == 'sud sardegna':
            nome_provincia = 'provincia del ' + nome_provincia
        else:
            nome_provincia = 'provincia di ' + nome_provincia

        return(nome_provincia)


    def get_comune(self, file_block):
          codice_comune = file_block[0][COMUNE_START: COMUNE_END]
          codice_comune = codice_comune[1:len(codice_comune) + 1] if codice_comune[0] == '0' else codice_comune
          nome_comune = (self.mapper['com_name'].loc[self.mapper['com_new'] == codice_comune]).values[0]
          #nome_comuni = self.mapper['com_name'].loc[self.mapper['com_new'].isin(codici_comuni)]
          return nome_comune,codice_comune

    def get_tipo_localita_turistica(self, file_block):
        codice_localita = file_block[0][LOC_START:LOC_END]
        return codice_localita


    def get_structure(self, type, line):
        types = (list(STRUCTURE.keys()))
        if type not in types:
            print("Invalid structure category!\n")
            return
        start, end = STRUCTURE[type]
        structure_field = int(line[start:end])
        return(structure_field)


    def get_capacity(self, capacity_code, block):
        if capacity_code not in CAPACITY_CODES:
            print("A problem has occurred. Wrong capacity code!")
            return
        line_index = CAPACITY_CODES.index(capacity_code)
        line_selected = block[line_index]
        record_type = line_selected[RECORD_TYPE_FLD]
        if record_type != '6':
            print("Incorrect line selected!")
            return

        capacity = [self.get_structure(type, line_selected) for type in STRUCTURE_TYPES]
        capacity = capacity[0:len(capacity) - 1]
        return(capacity)

    def get_arrivals_presences_by_structure(self, type, line):

        line_type = line[0]
        types = (list(STRUCTURE.keys()))
        if line_type != '7':
            print("Invalid line type!")
            return
        elif type not in types:
            print("Invalid structure category!\n")
            return

        #campo arrivi
        a_start, a_end = ARRIVI[type]
        arrivals = int(line[a_start:a_end])
        #campo presenze
        presences = None
        if type != 'X':
            p_start, p_end = PRESENZE[type]
            presences = int(line[p_start:p_end])
        return(arrivals, presences)


    def get_movements(self, provenance_code, block):
        if provenance_code not in ORIGIN_CODES:
            print("A problem has occurred. The code of the Region/State provided is not valid!")
            return
        block_subset = list(filter(lambda  line: (line[0] == '7'), block))
        target_line = list(filter(lambda line: (line[17:20] == provenance_code), block_subset))[0]
        #print(target_line)
        if target_line[0] != '7':
            print("Incorrect line selected!")
            return

        movements = [self.get_arrivals_presences_by_structure(type, target_line) for type in STRUCTURE_TYPES ]
        movements = movements[0:len(movements)-1]
        # flatten = lambda l: [item for sublist in l for item in sublist]
        # print(flatten(movements))
        return(movements)


    def compute_extra_total(self, line):

        line_type = line[0]
        if line_type == '6':
            b10_start, b10_end = STRUCTURE["B10"]
            c1_start, c1_end = STRUCTURE["C1"]
            c2_start, c2_end = STRUCTURE["C2"]

            complementari = int(line[b10_start:b10_end])
            bb = int(line[c1_start:c1_end])
            alloggi = int(line[c2_start:c2_end])
            tot_extra = complementari + bb + alloggi
            return(tot_extra)
        elif line_type == '7':
            ab10_start, ab10_end = ARRIVI["B10"]
            pb10_start, pb10_end = PRESENZE["B10"]
            ac1_start, ac1_end = ARRIVI["C1"]
            ac2_start, ac2_end = ARRIVI["C2"]
            pc1_start, pc1_end = PRESENZE["C1"]
            pc2_start, pc2_end = PRESENZE["C2"]

            arrivi_b10 = int(line[ab10_start:ab10_end]) #totale arrivi complementari
            arrivi_c1 = int(line[ac1_start:ac1_end]) #totale arrivi B&B
            arrivi_c2 = int(line[ac2_start:ac2_end]) #totale arrivi alloggi privati

            presenze_b10 = int(line[pb10_start:pb10_end]) #totale presenze complementari
            presenze_c1 = int(line[pc1_start: pc1_end]) #totale presenze B&B
            presenze_c2 = int(line[pc2_start:pc2_end]) #totale presenze alloggi privati

            arrivi = arrivi_b10 + arrivi_c1 + arrivi_c2
            presenze = presenze_b10 +presenze_c1 + presenze_c2
            return(arrivi, presenze)
        else:
            print("wrong line type!")
            return




        # def get_esercizi(self, file_block):
        #     line_selected = file_block[0]
        #     record_type = line_selected[RECORD_TYPE_FLD]
        #     codice_capacita = line_selected[CODICE_CAPACITA_START:CODICE_CAPACITA_END]
        #
        #     if record_type != 6 and codice_capacita != '001':
        #         print("Invalid line selected!")
        #         return
        #
        #     esercizi = [self.get_structure(type, line_selected) for type in STRUCTURE_TYPES]
        #
        #     return esercizi

    # #Alberghi 5 stelle e stelle lusso
    # def getA1(self, line):
    #     a1 = line[A1_START:A1_END]
    #     if a1[RECORD_TYPE_FLD] != '6':
    #         print("Invalid line!")
    #         return
    #     try:
    #         a1 = int(a1)
    #     except TypeError("invalid format"):
    #         return
    #     return (a1)
    #
    # def getA2(self, line):
    #     a2 = line[A2_START:A2_END]
    #     if a2[RECORD_TYPE_FLD] != '6':
    #         print("Invalid line!")
    #         return
    #     try:
    #         a1 = int(a1)
    #     except TypeError("invalid format"):
    #         return
    #     return (a1)




