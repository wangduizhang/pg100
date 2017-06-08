#!/usr/bin/python
#_*_coding:utf-8_*_
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
s = 2.0
m = 1.0
num = 20
a = 0
for i in range(num):
	a += s/m
	b = s
	s = s+m
	m = b
print a
