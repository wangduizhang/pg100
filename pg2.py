#!/usr/bin/python
#_*_coding:utf-8_*_
#企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def money(i):
	if i <= 10:
		m = i * 0.1
	elif i <= 20:
		m = 1 + (i-10)*0.075
	elif i <= 40:
		m = 1 + 10*0.075 + (i-20)*0.05
	elif i <= 60:
		m = 1 + 10*0.075 + 20*0.05 + (i - 40)*0.03
	elif i <= 100:
		m = 1 + 0.75 + 1 + 0.6 + (i - 60)*0.015
	elif i > 100:
		m = 1 + 0.75 + 1 + 0.6 + 40*0.015 + (100 - 60)*0.01
	return m	
m = float(raw_input('请输入利润：'))
print "工资是：%s " % (money(m/10000)*10000)
		
		
		
