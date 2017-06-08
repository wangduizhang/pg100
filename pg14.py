#!/usr/bin/python
#_*_coding:utf-8_*_
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#运算效率低，规则的数字好求算。
def cheji(num):
	n = 1
	for i in num:
		n = n * int(i)
	return n
	

ln = []
rnum = int(raw_input('你要分解的数字：'))

num = rnum

n = 2
while cheji(ln) != rnum:
	if num % n == 0:
		ln += str(n)
		num = num / n
		n = 2
		
	else:
		n += 1

print '*'.join(ln)