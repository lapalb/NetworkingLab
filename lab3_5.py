# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 09:49:07 2019

@author: student
"""

import ntplib
from time import ctime
c = ntplib.NTPClient()
response = c.request('pool.ntp.org',version=3)
print(ctime(response.tx_time))

