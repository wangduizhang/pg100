#!/usr/bin/python
#_*_coding:utf-8_*_
#打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身.

for i in range(100,1001):
	n1 = i / 100
	n2 = i /10 % 10
	n3 = i % 10
	if n1**3 + n2**3 + n3**3 == i:
		print i


