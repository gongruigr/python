# -*- coding: utf-8 -*- 
import xlrd
import xlwt
col_num = [8,9]	#column number for saving
def rw_excel():
	# 打开文件   
	workbook = xlrd.open_workbook("主机列表.xls")   
	# 获取所有sheet   
	sheet1_name = workbook.sheet_names()[0]     
	# 根据sheet索引或者名称获取sheet内容   
	sheet1 = workbook.sheet_by_index(0)
	# sheet索引从0开始   
	#sheet1 = workbook.sheet_by_name("Sheet2")     
	# sheet的名称，行数，列数   
	#print sheet1.name,sheet1.nrows,sheet1.ncols     
	# 获取整行和整列的值（数组）
    	row0 = sheet1.row_values(0)	#first row, title
	for i in range(1,sheet1.nrows):
    		row = sheet1.row_values(i)
		if sheet1.cell(i,0).ctype != 0:	#ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
			row_num = 1;	#for writing, num 0 is tile
			f = xlwt.Workbook() #创建工作簿
			w_sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
			w_sheet1.col(0).width=256*100
			filename = sheet1.cell(i,0).value.encode('utf-8')+".xls"
        		w_sheet1.write(0,0,row0[col_num[0]])
        		w_sheet1.write(0,1,row0[col_num[1]])
        		w_sheet1.write(row_num,0,row[col_num[0]])
        		w_sheet1.write(row_num,1,row[col_num[1]])
			row_num = row_num + 1
			f.save(filename)
		else:
        		w_sheet1.write(row_num,0,row[col_num[0]])
        		w_sheet1.write(row_num,1,row[col_num[1]])
			row_num = row_num + 1
			f.save(filename)

if __name__ == '__main__':
    	rw_excel()
