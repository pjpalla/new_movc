__author__ = 'pg'

from openpyxl import *
from movc.province_data import *
from all7.all7_consts import *

class All7:
    def __init__(self, year, province, template_file_path):
        self.year = year
        self.template = load_workbook(template_file_path)
        if province in NEW_PROVINCES:
            self.province = province
        else:
            raise Exception("Illegal province")

    def load_xl(self, movc_xl_path):
        self.movc = load_workbook(movc_xl_path)
        self.sheets = self.movc.get_sheet_names()


    def get_arrivi_residenti_alberghi(self):
        tot_arrivi = 0
        for sheet_name in self.sheets:
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            print(current_sheet.title)
            for i in RESIDENTS_RANGE:
                idx = 'O' + str(i)
                print(current_sheet[idx].value)
                tot_arrivi += int(current_sheet[idx].value)

        print(tot_arrivi)
        return(tot_arrivi)


    def get_presenze_residenti_alberghi(self):
        tot_presenze = 0
        for sheet_name in self.sheets:
            current_sheet = self.movc.get_sheet_by_name(sheet_name)
            print(current_sheet.title)
            for i in RESIDENTS_RANGE:
                idx = 'P' + str(i)
                print(current_sheet[idx].value)
                tot_presenze += int(current_sheet[idx].value)
        print(tot_presenze)
        return(tot_presenze)

    def get_arrivi_alloggi(self):
        tot_arrivi = 0
        sheet_name = self.sheets[0]
        current_sheet = self.movc.get_sheet_by_name(sheet_name)
        for label in ALLOGGI_DICT.keys():
            idx = label + "16"
            print(current_sheet[idx].value)
            tot_arrivi += current_sheet[idx].value

        return(tot_arrivi)
        





