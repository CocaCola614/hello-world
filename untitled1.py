# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:46:15 2021

@author: Administrator
"""

import pandas as pd
import os

path = 'G://工作//转融通委托//导出借入//'
fileName = os.listdir(path)[0]
filePath = os.path.join(path,fileName)

df = pd.read_excel(filePath, usecols=[1,2,4,5,9,7,14])
