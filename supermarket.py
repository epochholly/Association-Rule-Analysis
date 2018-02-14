# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:53:00 2016

@author: haoli
"""
import os
os.chdir("C:\\assignments\\Python")
import Apriori as ar
import csv



f = open("basket") 
freader = csv.reader(f, delimiter=',')
market = []
for row in freader:
    market.append(row)

L,support_data =  ar.apriori(market,minsupport=0.002)
ar.generateRules(L,support_data,min_confidence=0.01)


