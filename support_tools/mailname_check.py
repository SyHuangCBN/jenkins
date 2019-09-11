# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 16:41:56 2019

@author: gerben_chen
"""
import os
fw_name = os.popen("cat /home/cbnntl/cbn/cbn_ntl.txt").readlines()
fw = str(fw_name[0].strip())
fw = fw.split('/')
fw = fw[-1]
print fw
