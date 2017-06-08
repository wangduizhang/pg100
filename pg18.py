#!/usr/bin/python
#_*_coding:utf-8_*_
#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

def chong_(n,a):
	l =[]	
	for b in range(1,int(n)+1):
		aaa =  str(a)*b
		l.append(aaa)
	return l			
n = raw_input('多少个重叠数相加？')
a = raw_input('重叠项为？')
for i in chong_(n, a):
	print  '%s +' % i, 
print '= %s' % sum(int(b) for b in chong_(n, a))