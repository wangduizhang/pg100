#!/usr/bin/python
#_*_coding:utf-8_*_
import math
for i in range(10000):
	#转化为整型值
	x = int(math.sqrt(i + 100))
	y = int(math.sqrt(i + 268))
	if(x * x == i + 100) and (y * y == i + 268):
		print i
