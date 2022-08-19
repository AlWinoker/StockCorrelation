# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:04:21 2022

@author: 14015
"""

import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import pandas as pd
import statistics

tickers = ['AAPL','MSFT','AMZN','TSLA','META','TSM','JPM','NVDA','XOM','BAC','PFE','BABA','KO','CVX','VZ','CMCSA','CSCO','DIS','CRM','BMY','INTC','WFC','T','AMD','C','BA','BP','NOW','PYPL','MO','INFY','PBR','PDD','PBR-A','IBN','MU','VALE','CSX','EPD','OXY','F','GM','SLB','SU','UBER','SAN','SHOP','ITUB','ABEV','FCX','KMI','SQ','LYG','LI','NIO','DVN','WBD','BBD','CVE','HPQ','LCID','ET','GOLD','RIVN','TWTR','NOK','HAL','SIRI','SNAP','LUV','RBLX','TTD','CTRA','DAL','PLTR','BEKE','AMCR','NU','AVTR','RF','HABN','HPE','PARA','UMC','MRO','CS','COIN','TECK','UAL','PINS','U','APA','CCL','PLUG','GRAB','AAL','NLY','RCL','AMC','GFI','CLF','TEVA','TME','GGB','HOOD','SWN','COTY','AFRM','AGNC','NVAX','DNA','DKNG','NCLH','SOFI','X','M','AUY','MQ','LYFT','KGC','PSTH','CVNA','CPG','FRSH','IQ','BTG','OPEN','BB','PTON','GPS','AGI','STNE','FTCH','JBLU','HASI','INMD','UPST','HL']
averagecorrelations = [[]]
tickers = tickers[0:50]
correlationlist = []  
storage = [] 
scount = 0
for tickers1 in tickers:
    
    msft = yf.Ticker(tickers1)
    
    # get stock info
    msft.info
    
    # get historical market data
    hist = msft.history(period="max")
    
    #hist.plot(x='Date',y='Open',kind = 'scatter')
    
    count = []
    opened = []
    opendata = hist['Close']
    for i in range(0,len(hist)):
        count.append(i)
        opened.append(opendata[i])
    
    
    baseline = opened
    
    averagecorrelations[scount].append(tickers1)
    
    for ii in tickers:
        if tickers1 != ii:
            msft = yf.Ticker(ii)
            
            # get stock info
            msft.info
            
            # get historical market data
            hist = msft.history(period="max")
            
            #hist.plot(x='Date',y='Open',kind = 'scatter')
            
            count = []
            opened = []
            opendata = hist['Close']
            for i in range(0,len(hist)):
                count.append(i)
                opened.append(opendata[i])
            
            storedlist = []
            ####EDIT 7/13/2022
            for days in range(4,720):
                
                cora = stats.spearmanr(opened[-days:-1],baseline[-days:-1])
                storedlist.append(cora[0])
            if statistics.mean(storedlist)>0.8:
                averagecorrelations[scount].append(ii)
    
            
    scount=scount+1
    averagecorrelations.append([])