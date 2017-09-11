#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/9/4
# @Desc  :

import tushare as ts
import  datetime

tst=ts.get_sina_dd('600848',date='2017-08-24')

tst.to_csv("../docs/600848.csv")
print(tst)
