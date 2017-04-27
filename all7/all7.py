__author__ = 'pg'

from openpyxl import *
from movc.province_data import *
from all7.all7_consts import *

class All7:
    def __init__(self, template_file_path, year, province):
        self.year = year
        self.template = load_workbook(template_file_path)
        if province in NEW_PROVINCES:
            self.province = province
        else:
            raise Exception("Illegal province")

    def load_xl(self, movc_xl_path):
        self.movc = load_workbook(movc_xl_path, data_only=True)
        self.sheets = self.movc.get_sheet_names()
        if self.sheets[-1] == 'Riepilogo':
            self.sheets = self.sheets[0:-1]


    def get_alberghi(self, type='arrivi', category='residenti'):
        tot = 0
        for sheet_name in self.sheets:
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            # print(current_sheet.title)
            RANGE = RESIDENTS_RANGE if category == 'residenti' else NON_RESIDENTS_RANGE
            for i in RANGE:
                idx = 'O' + str(i) if type == 'arrivi' else 'P' + str(i)
                # print(current_sheet[idx].value)
                tot += int(current_sheet[idx].value)
        print(tot)
        return(tot)

    def get_alloggi(self, type='arrivi', category='residenti'):
        tot = 0
        #sheet_name = self.sheets[0]
        for sheet_name in self.sheets:
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            # print(current_sheet.title)
            RANGE = RESIDENTS_RANGE if category == 'residenti' else NON_RESIDENTS_RANGE
            for row_idx in RANGE:
                for k in ALLOGGI_DICT.keys():
                    value_idx = 0 if (type == 'arrivi') else 1
                    idx = ALLOGGI_DICT[k][value_idx] + str(row_idx)
                    tot += current_sheet[idx].value
                    #print("row id: " + str(row_idx) + " " + str(tot_arrivi))
        return(tot)

    def get_campeggi(self, type="arrivi", category='residenti'):
        tot = 0
        for sheet_name in self.sheets:
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            RANGE = RESIDENTS_RANGE if category == 'residenti' else NON_RESIDENTS_RANGE
            for row_idx in RANGE:
                for k in CAMPEGGI_DICT.keys():
                    value_idx = 0 if (type == "arrivi") else 1
                    idx = CAMPEGGI_DICT[k][value_idx] + str(row_idx)
                    # print(idx)
                    tot += current_sheet[idx].value
        return(tot)

    def get_altri_alloggi(self, type='arrivi', category='residenti'):
        tot = 0
        for sheet_name in self.sheets:
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            RANGE = RESIDENTS_RANGE if category == 'residenti' else NON_RESIDENTS_RANGE
            for row_idx in RANGE:
                for k in ALTRI_ALLOGGI_DICT.keys():
                    value_idx = 0 if (type == "arrivi") else 1
                    idx = ALTRI_ALLOGGI_DICT[k][value_idx] + str(row_idx)
                    # print(idx)
                    tot += current_sheet[idx].value
        return(tot)


    def get_giornate_letto(self):
        tot = 0
        for sheet_name in self.sheets:
            # print(sheet_name)
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            idx = 'P11'
            tot += int(current_sheet[idx].value)
        return(tot)


    def get_giornate_camere(self, type = 'disponibili'):
        tot = 0
        idx = 'P12' if (type == 'disponibili') else 'P13'
        for sheet_name in self.sheets[0:3]:
            # print(sheet_name)
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            tot += int(current_sheet[idx].value)
        return(tot)


    def build_xl(self, movc_dir):
        file_names = []
        try:
            file_names = os.listdir(movc_dir)
        except NotADirectoryError():
            print("Wrong directory! Please enter the correct movc directory name")
            return





