# -*- coding: UTF-8 -*-

import os

# Get numbers from Jenkins
num1=os.getenv("num1")
num2=os.getenv("num2")

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


