'''
	date:20170705
	author:gongrui
	describe:
	Write stock data to csvfile.
'''
filedir = 'stock_data/'
def stock_data_write(stock_id,start_date,end_date):
	import tushare as ts
	pd = ts.get_hist_data(stock_id,start=start_date,end=end_date)
	if pd is None:
		print 'Could not get data of %s'%stock_id
	else:
		pd.to_csv(filedir+str(stock_id)+'.csv')

fr = open(filedir+'stock_code_list.txt','r')
stock_codes = fr.readlines()
lenth = len(stock_codes)
cnt = 0
pct = 1
print 'Stock data downloading...'
for line in stock_codes:
	line = line.strip()
	line = str(line)
	stock_data_write(stock_id=line,start_date='2014-07-05',end_date='2017-07-06')
	if cnt == lenth//10*pct:
		print '%d'%(pct*10) +'% data has been downloaded!'
		pct = pct + 1
	cnt = cnt + 1
print 'Stock data has been downloaded!'
fr.close()
