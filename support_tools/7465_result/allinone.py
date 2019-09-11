# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 14:00:49 2018

@author: gerben
"""

# coding=utf-8
import glob
import os,sys,re
import time
def texttotext():
    '''Check P7 file date'''
    dir_files=glob.glob('/home/gerben_test/7465_result/*.html')
    #print dir_files
    localtimes = time.strftime("%Y%m%d",time.localtime())
    #print localtimes
    for i in range(len(dir_files)):
	#print dir_files
        fp = open('%s' % dir_files[i], "r")	
        lines = fp.readlines()
        fp.close()
        status = False
        for j in range(len(lines)):
            #print (lines[j])
            if localtimes in lines[j]:
                status = True
        if status == False:
            os.remove('%s' % dir_files[i])
    dir=glob.glob('/home/gerben_test/7465_result/*.html')
    if len(dir) == 0:
	sys.exit(1)
    dir_sort = []
    for i in range(len(dir)):
        if 'results_daily.html' in dir[i]:
            dir_sort.insert(0,dir[i])
        elif 'results_wifi.html' in dir[i]:
            if len(dir_sort) < 1:
    	        dir_sort.insert(0,dir[i])
            elif (0 < len(dir_sort) < 2) and ('results_daily.html' not in dir_sort[0]) :
                dir_sort.insert(0,dir[i])
            else:
                dir_sort.insert(1,dir[i])
        elif 'results_voice.html' in dir[i]:
    	    if len(dir_sort) < 1:
                dir_sort.insert(2,dir[i])
    	    elif (0 < len(dir_sort) < 2) and ('results_daily.html' not in dir_sort[0]) and ('results_wifi.html' not in dir_sort[0]):
                dir_sort.insert(0,dir[i])
    	    elif (1 < len(dir_sort) < 3) and ('results_daily.html' not in dir_sort[1]) and ('results_wifi.html' not in dir_sort[1]):
                dir_sort.insert(1,dir[i])
    	    else:
                dir_sort.insert(2,dir[i])
        elif 'results_isolate.html' in dir[i]:
    	    if len(dir_sort) < 1:
                dir_sort.insert(2,dir[i])
    	    elif (0 < len(dir_sort) < 2) and ('results_daily.html' not in dir_sort[0]) and ('results_wifi.html' not in dir_sort[0]) and ('results_voice.html' not in dir_sort[0]):
                dir_sort.insert(0,dir[i])
    	    elif (1 < len(dir_sort) < 3) and ('results_daily.html' not in dir_sort[1]) and ('results_wifi.html' not in dir_sort[1]) and ('results_voice.html' not in dir_sort[1]):
                dir_sort.insert(1,dir[i])
    	    elif (3 < len(dir_sort) < 4) and ('results_daily.html' not in dir_sort[2]) and ('results_wifi.html' not in dir_sort[2]) and ('results_voice.html' not in dir_sort[2]):
                dir_sort.insert(2,dir[i])
    	    else:
    	    	dir_sort.insert(3,dir[i])

    fout=open('/home/gerben_test/7465_result/ch7465ce-results.html','a')
    for filename in dir_sort:
        print(filename)
        fopen=open(filename,'r')
        lines=[]
        lines=fopen.readlines()
        fopen.close()
        for line in lines:
            line.decode('gbk','ignore').encode('utf-8')
            for x in line:
                fout.write(x)


if __name__ == '__main__':
    texttotext()
