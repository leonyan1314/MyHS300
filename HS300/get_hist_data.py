#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_tick_data.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/9/2
# @Desc  :获取沪深300全部日k线数据

from HS300 import GetHS300
import tushare as ts
from HS300 import  MysqlConn
import json

def get_hist_data():#获取沪深300所有个股以往交易历史的分笔数据明细
    codelist=GetHS300.GetHS300().get300code()
    Myconn=MysqlConn.MysqlConn()
    for i in range(len(codelist)):
      #  print(ts.get_hist_data(codelist[i]))
        Myconn.get_hist_data(codelist[i],'Thistday')
        print("success insert into "+codelist[i])
if __name__ == "__main__":
    get_hist_data()

