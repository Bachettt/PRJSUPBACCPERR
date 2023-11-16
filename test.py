# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:44:47 2023

@author: user
"""

from zeep import Client

client = Client('http://192.168.141.58:8000/?wsdl')
result1=client.service.calcultrajetcharg(120,9,30)

print(result1)