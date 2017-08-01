'''
	date:20170706
	author:gongrui
	describe:
	Write stock basic info to csvfile.
'''
filedir = 'stock_data/'
import tushare as ts
ts.get_stock_basics().to_csv(filedir+'stock_basic_info.csv')
