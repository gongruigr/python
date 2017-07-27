#!/usr/bin/env python
#coding=utf-8
# Filename : num2chinese.py
# Description : change numbers to chinese
# Author : gongrui
# Date : 20160806
# E-mail : gongruigr@126.com
#-----------------------------------------

#function: 4 numbers to chinese
def num2chinese_4(string):
	chinese=[]
	flag=0
	dict_num={'0':'零','1':'一','2':'二','3':'三','4':'四','5':'五','6':'六','7':'七','8':'八','9':'九'}
	dict_position={3:'千',2:'百',1:'十',0:''}
	if(string=='0000'):
		chinese.append(dict_num['0'])
	else:
		for i in range(len(string)):
			if(string[i]=='0'):
				flag=1
			else:
				if(flag==1):
					flag=0
					chinese.append(dict_num['0'])
				else:
					pass	
				chinese.append(dict_num[string[i]])
				chinese.append(dict_position[len(string)-i-1])
	return chinese

#function: change a list to string and print
def print_str(list_in):
	temp=''
	for i in range(len(list_in)):
		temp=temp + list_in[i]
	print ('%s'%temp)

import math
print ('Please enter a number which is less than 10^32 and more than 0!')
num = int(input())
if num>=1e+32:
	print ('The number is more than 10^32, it will be exit!')
	exit()
elif num<0:
	print ('The number is less than 0, it will be exit!')
	exit()
elif num==0:
	print ('The result is: \n零')
	exit()
else:
	pass

num_str=str(num)#change number to string
num_len=len(num_str)#get lenth of the string
dict_unit = {0:'',1:'万',2:'亿',3:'兆',4:'京',5:'垓',6:'秭',7:'穰',8:'沟',9:'涧',10:'正',11:'载'}
result=[]#list for storing
num_divided_by_4 = int(math.ceil(num_len/4.0))
for i in range(num_divided_by_4):
	result_temp = []
	num_str_4 = num_str[-4:]
	num_str = num_str[:-4]
	result_temp = num2chinese_4(num_str_4)
	if(result_temp[0]=='零' and len(result_temp)==1):#if the block is '0000', do not add unit
		if(len(result)==0):#if the first block(lowest 4 num) is '0000', result is null
			pass
		elif(result[0]=='零'):#if pre block's first string is '零', keep one '零' to instead two
			pass
		else:
			result = result_temp + result
	else:
		result_temp.append(dict_unit[i])
		result = result_temp + result

print ('The result is:')
print_str(result)
