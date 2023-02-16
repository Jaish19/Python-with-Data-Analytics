from openpyxl import Workbook
import time

book = Workbook()
sheet = book.active

sheet['A1'] = 56
sheet['A2'] = '平均油耗'
j=3
now = time.strftime("%x")
sheet['A3'] = now
sheet.cell(row=j, column=4).value = 'Match'



rows = (
    (88, 46, 57),
    (89, 38, 12),
    (23, 59, 78),
    (56, 21, 98),
    (24, 18, 43),
    (34, 15, 67)
)

for row in rows:
    sheet.append(row)

book.save("sample.xlsx")