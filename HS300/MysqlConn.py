#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : MysqlConn.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/9/2
# @Desc  :
import lxml
import datetime
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine
import tushare as ts
import json

class MysqlConn():

    def __init__(self):

        with open('DbConn.json') as json_file:
            data = json.load(json_file)
            print('trying to connect to DB on '+str(data['MysqlIp'])+'....')
        self.url ="mysql://"+data['MySqlUser']+":"+data['MysqlPwd']+"@"+data['MysqlIp']+"/"+data['MySqlDB']+"?charset=utf8"

#获取日开线
    def get_hist_data(self,code,table):
        df = ts.get_hist_data(code)
        df['code']=code
        engine = create_engine(self.url)
        df.to_sql(table, engine,if_exists='append')
#获取日大单数据
    def get_sina_dd(self,mycode,mytable,mydate):

        try:
            df = ts.get_sina_dd(mycode,date=mydate)
            df.to_csv('../docs/BigTrade'+mycode+".cvs")
        except:
            print("failed to get " +mycode+"'s data")
        else:
            engine = create_engine(self.url)
            df["Tdate"]=mydate
            df.to_sql(mytable, engine, if_exists='append')


