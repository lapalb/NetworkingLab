# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:46:08 2019

@author: student
"""

#Getting the Service Name
print("\nThe Service Name is ",socket.getservbyport(53))
print("\nThe port is ",socket.getservbyname('dns'))