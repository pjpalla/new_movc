__author__ = 'pg'

import openpyxl
from openpyxl import *
from pandas import *
import pandas


print(openpyxl.__version__)
fname = "MOVC_OG_Marzo_2016.xlsx"
output = "sorted.xlsx"
wb = load_workbook(fname)
names = wb.get_sheet_names()
print(names)

arrivi = 0

sheet_names = wb.get_sheet_names()
val = 0
for n in sheet_names:
    print(n)
    current_sheet = wb.get_sheet_by_name(n)
    for i in (range(16,37)):
        idx = 'O' + str(i)
        val += int(current_sheet[idx].value)



print("Totale_alberghi_residenti: " + str(val))
    # print(current_sheet['O16'].value)

# ws = wb.get_sheet_by_name("ASSEMINI")
# print(ws['O16'].value)
# wb._sheets.sort(key = lambda ws: ws.title)
# names_after = wb.get_sheet_names()
# print(names_after)
# wb.save(output)
