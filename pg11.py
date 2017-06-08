#!/usr/bin/python
#_*_coding:utf-8_*_
#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
def rabb_(m):
	if m == 1:
		return 1
	if m == 2:
		return 1
	elif m >= 2:
		return rabb_(m-1)+rabb_(m-2)


m = int(raw_input("month:"))

print rabb_(m)
	