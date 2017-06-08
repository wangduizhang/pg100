#!/usr/bin/python
#_*_coding:utf-8_*_
import random

num = random.choice(range(1,100000))
print len(str(num))
print (str(num))[len(str(num):1)]