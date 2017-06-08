#!/usr/bin/python
#_*_coding:utf-8_*_
#有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
for i in [1,2,3,4]:
	for j in range(1,5):
		for k in range(1,5):
			if (i != j) and (i != k) and (j != k):
				print i*100 + j*10 + k