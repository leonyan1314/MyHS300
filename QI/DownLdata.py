#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : DownLdata.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/8/30
# @Desc  :

import lxml
from influxdb import *
import datetime
import pandas as pd
from pandas import Series, DataFrame
from sqlalchemy import create_engine
import tushare as ts

def get_stork():
    df = ts.get_tick_data('600848', date='2016-12-22')
    engine = create_engine('mysql://root:passw0rd@192.168.1.88/stocks?charset=utf8')
    df.to_sql('tick_data',engine)
   # print (df)

def getdf():
   df=pd.read_csv('stock.csv',sep=';')
   df['times1']=datetime.datetime.now()
   return df

def inert():
    user = 'root'
    password = 'root'
    dbname = 'stocks'
    protocol = 'json'
    host='192.168.1.163'
    port='8086'
    stdf=getdf().set_index(['times1'])

    print (stdf)
    client = DataFrameClient(host, port, user, password, dbname)
    client.write_points(stdf,'leonyan', protocol=protocol)


if __name__ == "__main__":
    #inert()
  # print(getdf())
    get_stork()
#    print ('agent start successful at: '+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
