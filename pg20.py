#!/usr/bin/python
#_*_coding:utf-8_*_
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
tall = 100.0
stall = 0
for i in range(1,11):
	tall = tall/2
	stall += tall*2 
	print 'No. %s %f '% (i,tall)
print "Sum tall %f" % (stall+100)

