import openpyxl
from openpyxl.drawing.image import Image

wb = openpyxl.Workbook()
ws = wb.active
ws['A1'] = 'You should see the logos below'
img = Image('test.png')
ws.add_image(img, 'A2')
wb.save('out.xlsx')