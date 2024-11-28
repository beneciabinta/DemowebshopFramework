import xlrd

path = r'C:\Users\guestuser\PycharmProjects\framework\locator_data.xlsx'

def read_locators(sheetname):
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name(sheetname)
    used_rows = worksheet.nrows
    data = {}
    for i in range(1,used_rows):
        rows = worksheet.row_values(i)
        data[rows[0]] = (rows[1], rows[2])
    return data

import xlrd

