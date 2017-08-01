'''
	date:20170706
	author:gongrui
	describe:
	Write stock basic info to csvfile.
'''
filedir = 'stock_data/'
import tushare as ts
pd = ts.get_stock_basics()
fp = open(filedir+'stock_code_list.txt','w')
for i in range(len(pd.index)):
	fp.write(pd.index[i] + '\n')
fp.close()
