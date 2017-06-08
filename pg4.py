#!/usr/bin/python
#_*_coding:utf-8_*_
#输入某年某月某日，判断这一天是这一年的第几天？
def run_(year):
	if year % 4 == 0:
		return 1
	else:
		return 0

def try_mon(m):
	if m > 12:
		print "Month  Error"
		return 0
	elif m <= 12:
		return 1

def try_day(d,m,y):
	if day > 31:
		print "Day Error"
		return 0
	elif m in (1,3,5,7,8,10,12) and d > 31:
		print "Day Error"
		return 0
	elif m in (4,6,9,10) and d > 30:
			print "Day Error"
			return 0
	elif m == 2 and y % 4 == 0 and d > 28:
			print "Day Error"
			return 0
	elif m == 2 and y % 4 != 0 and d > 29:
				print "Day Error"
				return 0
	else:
		return 1
	
while 1:	
	year = int(raw_input("请输入年份："))
	month = int(raw_input("请输入月份："))
	day = int(raw_input("请输入天数："))

	mouthday = (31,29,31,30,31,30,31,31,30,30,30,31)
	mouthday2 = (31,28,31,30,31,30,31,31,30,30,30,31)



	if try_day(day, month, year) and try_mon(month):
		if month == 1:
			print 'This is NO. %d day' % day
	
		elif run_(year):
			m = mouthday2[0:month]
			days = sum((int(x) for x in m)) + day - 1
			print 'This is NO. %d day' % days
		elif not run_(year):
			m = mouthday[0:month]
			days = sum((int(x) for x in m)) + day - 1
			print 'This is NO. %d day' % days