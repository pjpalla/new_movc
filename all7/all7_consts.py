__author__ = 'pg'


#template
ALL7_TEMPLATE_PATH = r"C:\Users\piepalla\PycharmProjects\new_movc\config\allegato7_base.xlsx"

### range of cells of the movc related to people resident and not resident in Italy
RESIDENTS_RANGE = list(range(16, 37))
NON_RESIDENTS_RANGE = list(range(39, 96))

### range of cells of the all7 related to people resident and not resident in Italy
ALL7_RESIDENTS_RANGE = list(range(8, 20))
ALL7_NON_RESIDENTS_RANGE = list(range(21, 33))
ALL7_DAYS_RANGE = list(range(8,20))
ALL7_COL1 = list(range(3, 9)) + list(range(12,14))#[chr(i) for i in range(ord('C'), ord('I'))] + [chr(i) for i in range(ord('L'), ord('N'))]
ALL7_COL2 = list(range(2, 5))
ALL7_BASE_OUTPUT = "all7_"
ALL7_EXT = '.xlsx'


TOT_RES_IDX = 20
TOT_NO_RES_IDX = 33
TOT_IDX = 34
TOT_DAYS_IDX = 20
###
ALLOGGI_DICT = {"B2":["S","T"], "B4":["W", "X"], "B5":["Y", "Z"], "B6":["AA", "AB"], "B7":["AC", "AD"], "B8":["AE", "AF"], "B9": ["AG", "AH"], "C1":["AK", "AL"]}
CAMPEGGI_DICT = {"B1": ["Q", "R"], "B3":["U", "V"]}
ALTRI_ALLOGGI_DICT = {"C2":["AM", "AN"]}
MONTHS_DICT = {"GENNAIO":0, "FEBBRAIO":1, "MARZO":2, "APRILE":3, "MAGGIO":4, "GIUGNO":5, "LUGLIO":6, "AGOSTO":7, "SETTEMBRE":8, "OTTOBRE":9, "NOVEMBRE":10, "DICEMBRE":11}

###MOVC SOURCE DIR###
SOURCE_DIR = r"C:\Users\piepalla\PycharmProjects\new_movc\all7\movc"

#Number of movc modules needed to build all7 module
NUM_OF_MOVC = 12

MONTHS = 12
PROVINCE_CELL = 'A1'
YEAR_CELL = 'B2'