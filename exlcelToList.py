import xlrd

book=xlrd.open_workbook('filename.xlsx')
sheet=book.sheet_by_name('SheetName')

rowlist=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

print rowlist