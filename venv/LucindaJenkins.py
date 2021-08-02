# -*- coding: UTF-8 -*-

import os
#num1 = input('输入第一个数字：')

class getData():
    def get_parameters_from_jenkins(self,parameters_name):
        return os.getenv(parameters_name)

data=getData()
num1=data.get_parameters_from_jenkins("num1")
num2=data.get_parameters_from_jenkins("num2")

#num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))


