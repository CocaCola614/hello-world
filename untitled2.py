# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 09:39:37 2021

@author: Administrator
"""

import backtrader as bt
import datetime


class TestStrategy(bt.Strategy):
    params = (
        ('maperiod', 20)
        )
    
    def log(self, txt, dt=None):
        '''策略日志函数'''
        dt = dt or self.datas[0].datetime.date(0)
        