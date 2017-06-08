#!/usr/bin/python
#_*_coding:utf-8_*_
#一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
import math
def float_(num):
	if num - int(num) == 0:
		return 1
	else:
		return 0

for i in range(100001):
	num1 = math.sqrt(i + 100)
	num2 = math.sqrt(i + 268)
	if float_(num1) and float_(num2):
		print i