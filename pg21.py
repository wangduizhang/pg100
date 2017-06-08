#!/usr/bin/python
#_*_coding:utf-8_*_
#猴子吃桃：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


endnum = 1
day = 10
rnum = 1
num = rnum

for i in range(1,day+1):
	print "No. %s day ago has %d peach." % (i,num)
	if i < day:
	    num = 2*num + 2
	
print "总共 %d 个桃子" % num
	