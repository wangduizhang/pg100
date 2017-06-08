#!/usr/bin/python
#_*_coding:utf-8_*_
#判断101-200之间有多少个素数，并输出所有的素数。
def pd_(num):
	n = []
	for i in range(2,num):
		if num % i == 0:
			n += str(num)
	return n


for num in range(101,201):
	n = pd_(num)
	if len(n) == 0:
		print num ,
