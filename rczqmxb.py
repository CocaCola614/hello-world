# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:39:37 2021

@author: Administrator
"""

import pandas as pd

path = 'G://工作//报表//202107//融出证券明细表//自营划入融券专户余额202107.xls'
df = pd.read_excel(path,dtype=str)
df0 = df[df.columns[0:10]]

# df0[df0['部门'] == '证券投资部']
'''
目前，columns[10]其实是对应股票所有的融券余额。
我们需要分出来哪些是自营的，哪些是转融券的。
规则：
[10] - [9] > 0, 则全部为
'''

dfnew = pd.DataFrame()

dfSelectStock = df0.groupby('证券代码')
for name, temp in dfSelectStock:
    # 一只股票对应一个初始的融券余额,remainder表示融券余额减去划入专户的值。>=0表示此余额有
    # 转融通的成份。<=0表示此余额全部为自营证券融出
    remainder = temp.iloc[0,9]-temp.iloc[0,8]
    if temp.shape[0] == 1:
        if remainder >= 0:
            temp.iloc[0, 9] = temp.iloc[0, 8]
        dfnew = dfnew.append(temp)
        # dfnew = dfnew.append(temp, ignore_index=True)
    # 当同一个证券代码有多个条目时
    elif temp.shape[0] > 1:
        # 先量化后证投，先可供后交易
        rowNum = temp.shape[0]
        # temp['余额'] = []
        # temp['rank'] = []
        temp.loc[(temp['部门']=='量化投资部') & (temp['资产性质']=='可供出售金融资产'), \
                 'rank'] = 1
        temp.loc[(temp['部门']=='量化投资部') & (temp['资产性质']=='交易性金融资产'), \
                 'rank'] = 2
        temp.loc[(temp['部门']=='证券投资部') & (temp['资产性质']=='可供出售金融资产'), \
                 'rank'] = 5       
        temp.loc[(temp['部门']=='证券投资部') & (temp['资产性质']=='交易性金融资产'), \
                 'rank'] = 6
        temp.loc[(temp['部门']=='衍生产品部') & (temp['资产性质']=='可供出售金融资产'), \
                 'rank'] = 3
        temp.loc[(temp['部门']=='衍生产品部') & (temp['资产性质']=='交易性金融资产'), \
                 'rank'] = 4

        # a = 0
        for i in range(0, rowNum):
            # a += i
            # 相同性质的条目，优先自营多的
            if temp.iloc[i, 10] == temp.iloc[i+1, 10]:
                balance = temp.iloc[i, 10] - temp.iloc[i, 9]
                temp.sort()
            



            
        dfnew = dfnew.append(temp)    
            
        
    
for i in range(0,3):
    print(i)


for name, temp in dfSelectStock:
    print(name)









