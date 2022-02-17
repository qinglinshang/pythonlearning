import xlrd
path = 'C:\\Users\\qshang\\Downloads\\测试用例.xls'
file = xlrd.open_workbook(path)
sheet = file.sheet_by_name('发布文章')
rownum = sheet.nrows
print(rownum)

for i in range(rownum):
    data = sheet.row_values(i)
    print(data)
    getdata = data[3]
    print(getdata)