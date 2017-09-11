#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_sina_dd.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/9/6
# @Desc  :获取HS300所有个股大单交易数据

from HS300 import GetHS300
import tushare as ts
from HS300 import  MysqlConn
import json
import datetime

def get_sina_dd():#获取沪深300所有个股大单交易数据明细(默认为400手)
    codelist=GetHS300.GetHS300().get300code()
    Myconn=MysqlConn.MysqlConn()
    for da in range(20):
        LastDay=datetime.date.today()-datetime.timedelta(days=da)
        for i in range(len(codelist)):
      #print(ts.get_hist_data(codelist[i]))
            Myconn.get_sina_dd(codelist[i],'Tbigtrade',LastDay)
            print("success get big trade data ： "+codelist[i])
if __name__ == "__main__":
    get_sina_dd()