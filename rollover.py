# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:46:15 2021

@author: Administrator
"""

import pandas as pd
import xlrd

pathRzrq = 'G://工作//转融通委托//导出展期//503129.xls'
df = pd.read_excel(xlrd.open_workbook(pathRzrq, encoding_override="gbk"),\
              usecols=[3,6,7,9,10,12,13,17,21], dtype=str)
# df = pd.read_excel(pathRzrq, usecols=[3,6,7,9,10,12,13,17,21], dtype=str)

df688 = df[df['证券代码'].str.startswith('688')]
df999 = df[(df['证券代码']=='300999')]   
df888 = df[(df['证券代码']=='300888')]   
df866 = df[(df['证券代码']=='300866')]   
dfKcb = pd.concat([df688, df999, df888, df866])

dfKcb.to_excel('G://工作//转融通委托//导出展期//kcbzq.xls', encoding='GBK', index=False)

pathZrq = 'G://工作//转融通委托//导出展期//L0001000.xls'
# dfZrq = pd.read_excel(pathZrq, usecols=[1,2,3,4,7,10,11,15,16,22,46,55], dtype=str)
dfZrq = pd.read_excel(xlrd.open_workbook(pathZrq, encoding_override='GBK'), usecols=[1,2,3,4,7,10,11,15,16,22,46,55], dtype=str)
# 当日成交合约 转融券融入
dfRr = dfZrq.groupby(['合约类型', '转融券业务类型']).get_group(('当日成交合约', '转融券融入'))
# 创建合并的Key
dfKcb['Key'] = dfKcb['证券代码'] + dfKcb['合约日期'] + dfKcb['合约到期日']
dfRr['Key'] = dfRr['证券代码'] + dfRr['开仓日期'] + dfRr['合约到期日']
dfRrMerge = dfRr[['Key','合约编号','对手方合约编号','转融通息费率','合约数量']]
# Merge
result = pd.merge(dfKcb, dfRrMerge, how='left', on='Key')
columns = ['资金账号','客户名称','证券代码','证券名称','展期数量','合约数量','申请展期天数', \
           '转融通息费率','合约编号','对手方合约编号','合约到期日']
result0 = result[columns]
# 保存
result0.to_excel('G://工作//转融通委托//导出展期//result.xls', index=False, encoding='GBK')

# 以下是主板的展期尝试
# df['Key'] = df['证券代码'] + df['合约日期'] + df['合约到期日']
# dfMerge = pd.merge(df, dfRrMerge, how='left', on='Key')
# dfMerge0 = dfMerge[columns]
# dfMerge1 = dfMerge0.drop_duplicates(subset='合约编号')

