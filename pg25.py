#!/usr/bin/python
#_*_coding:utf-8_*_
#求1+2!+3!+...+20!的和
def jc_(num):
	if num == 1:
		return 1
	else:
		return num *jc_(num-1)	

s = 0
for i in range(1,21):
	s += jc_(i)
print s



