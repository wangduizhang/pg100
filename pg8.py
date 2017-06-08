#!/usr/bin/python
#_*_coding:utf-8_*_
#输出9*9口诀

for i in range(1,10):
	for j in range(1,10):
		result = 1 * j
		if j == 9: 
			print '%d * %d = %d ' % (i , j ,result), '\n' 
		else:
			print '%d * %d = %d'  % (i , j ,result),

