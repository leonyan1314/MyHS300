#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : HS300.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/9/2
# @Desc  :

import lxml
import pandas as pd
from pandas import Series, DataFrame
import tushare as ts

class GetHS300():

  def get300list(self):
     return ts.get_hs300s()

  def get300code(self):
     df= ts.get_hs300s()
     ps=df['code']
     return ps