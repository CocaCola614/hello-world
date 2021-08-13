# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 14:13:04 2021

@author: Administrator
"""

import pandas as pd
import os

path = 'G://工作//转融通委托//导出借入//'
fileName = os.listdir(path)[0]
filePath = os.path.join(path,fileName)

df = pd.read_excel(filePath, usecols=[1,2,4,5,9,7,14])

# 若金证中股票名称前有XD等除权除息标，去除
# for name in df[df.columns[3]]:
    
#     if ""

borrowDf = pd.DataFrame(columns=['资金账号','姓名','股票','市场','股票代码','委托数量', \
                                 '期限','申请方式','约定费率'])    
# 资金账号
borrowDf[borrowDf.columns[0]] = df[df.columns[0]]
# 姓名
borrowDf[borrowDf.columns[1]] = df[df.columns[1]]
# 股票
borrowDf[borrowDf.columns[2]] = df[df.columns[3]]
# 市场
borrowDf[borrowDf.columns[3]] = 1
# 股票代码
borrowDf[borrowDf.columns[4]] = df[df.columns[2]]
# 委托数量
borrowDf[borrowDf.columns[5]] = df[df.columns[5]]
# 期限
borrowDf[borrowDf.columns[6]] = df[df.columns[4]]
# 申请方式
borrowDf[borrowDf.columns[7]] = 1

borrowDf.to_excel(path + 'bd.xlsx', encoding='GBK')


































