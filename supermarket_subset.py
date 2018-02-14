# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:53:00 2016

@author: haoli
"""
import os
#os.chdir("C:\\assignments\\Python")
import Apriori as ar
import csv

f = open("basket") 
freader = csv.reader(f, delimiter=',')
market = []
i = 1 
for row in freader:
    market.append(row)
    i = i + 1
    if (i >= 20):
        break

import sys
sys.stdout = open('supermarketout.txt', 'w')

L,support_data =  ar.apriori(market,minsupport=0.05)
ar.generateRules(L,support_data,min_confidence=0.9)

