#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Myfirst.py
# @Author: LeonYan
# @Contact : http://blog.csdn.net/yl_1314 
# @Date  : 2017/9/8
# @Desc  :

import tensorflow as tf
import numpy as np


sess = tf.Session()

matrix1 = tf.constant([[3., 3.]])
result = sess.run(matrix1)
print (result)

matrix2 = tf.constant([[2.],[2.]])
result = sess.run(matrix2)
print (result)
product = tf.matmul(matrix1, matrix2)

result = sess.run(product)

print (result)

with tf.Session() as sess:
  result = sess.run([product])
  print(result)

sess.close()
