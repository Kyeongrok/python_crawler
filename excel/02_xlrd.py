import xlrd
workbook = xlrd.open_workbook('user_info.xlsx')
worksheet = workbook.sheet_by_name('db')
list = worksheet._cell_values

for row in list[1:]:
    keyword = row[0]
    print(keyword)

