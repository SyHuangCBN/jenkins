# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 18:00:00 2018

@author: Gerben_chen
"""

import os
import argparse


def FW_7465_NAME_PA():    
    fw_name = os.popen("ls /home/cbn/FW_space/CH7465LG-NCIP-*-$(date +'%Y%m%d')-SH-PA | awk -F/ '{print $5}'").readlines() 
    return fw_name

def FW_8568_NAME_PA():       
    fw_name = os.popen("ls /home/cbn/FW_space/CH8568LG-NCIP-*-$(date +'%Y%m%d')-SH-PA | awk -F/ '{print $5}'").readlines() 
    return fw_name

def FW_7465_WIFI_NAME_PA():    
    fw_name = os.popen("ls /home/cbn/FW_space/CH7465LG-NCIP-*-$(date +'%Y%m%d')-W-SH-PA | awk -F/ '{print $5}'").readlines() 
    return fw_name

def FW_7465_NAME_P7():    
    fw_name = os.popen("ls /home/cbn/FW_space/CH7465LG-NCIP-*-$(date +'%Y%m%d')*.p7 | awk -F/ '{print $5}'").readlines() 
    return fw_name

def FW_8568_NAME_P7():  
    fw_name = os.popen("ls /home/cbn/FW_space/CH8568LG-NCIP-*-$(date +'%Y%m%d')*.p7 | awk -F/ '{print $5}'").readlines() 
    return fw_name

def FW_7465_WIFI_NAME_P7():    
    fw_name = os.popen("ls /home/cbn/FW_space/CH7465LG-NCIP-*-$(date +'%Y%m%d')-W-*.p7 | awk -F/ '{print $5}'").readlines() 
    return fw_name

def Rename_P7(fw_name_choose):
    return fw_name_choose[0:-12] + '.p7'
    
def FW_7465_NAME_PA_TITLE():    
    fw_name = os.popen("ls /home/cbn/FW_space/$(date +'%Y%m%d')/*/CH7465LG-NCIP-*-$(date +'%Y%m%d')-SH-PA | awk -F/ '{print $7}'").readlines() 
    return fw_name 

def FW_7465_WIFI_NAME_PA_TITLE():    
    fw_name = os.popen("ls /home/cbn/FW_space/$(date +'%Y%m%d')/*/CH7465LG-NCIP-*-$(date +'%Y%m%d')-W-SH-PA | awk -F/ '{print $7}'").readlines() 
    return fw_name
  
def FW_8568_NAME_PA_TITLE():    
    fw_name = os.popen("ls /home/cbn/FW_space/$(date +'%Y%m%d')/*/CH8568LG-NCIP-*-$(date +'%Y%m%d')-SH-PA | awk -F/ '{print $7}'").readlines() 
    return fw_name

HELP_EPILOG = '''
Example use:
    python sign_fw_name.py -n <FW_NAME> -f <file_format>
    python sign_fw_name.py -n ch7465ce -f PA(P7)
Example For Copy to Windows about SH.p7  
    python sign_fw_name.py -p <parameter>
    python sign_fw_name.py -p <8568p7>
    python sign_fw_name.py -p <7465p7>
'''
'''
Read command-line arguments, return a simple configuration for running tests.
'''        
parser = argparse.ArgumentParser(description='',
								 usage='',
								 formatter_class=argparse.RawDescriptionHelpFormatter,
								 epilog=HELP_EPILOG)
parser.add_argument('-n', '--name', metavar='', type=str, default=None, help='FW_NAME')
parser.add_argument('-f', '--fileformat', metavar='', type=str, default=None, help='File_Format')
parser.add_argument('-p', '--parameter', metavar='', type=str, default=None, help='ParameterForP7')
args = parser.parse_args()   
name = args.name
file_format = args.fileformat
parameter_type = args.parameter
if name == 'ch7465ce' and file_format == 'PA':    
    fw_name = FW_7465_NAME_PA()
    print fw_name[0].strip()
elif name == 'ch8568qe' and file_format == 'PA':
    fw_name = FW_8568_NAME_PA()
    print fw_name[0].strip()
elif name == 'ch7465ce_wifi' and file_format == 'PA':
    fw_name = FW_7465_WIFI_NAME_PA()
    print fw_name[0].strip()
elif name == 'ch7465ce' and file_format == 'P7':
    fw_name = FW_7465_NAME_P7()
    print fw_name[0].strip()
elif name == 'ch8568qe' and file_format == 'P7':
    fw_name = FW_8568_NAME_P7()
    print fw_name[0].strip()
elif name == 'ch7465ce_wifi' and file_format == 'P7':
    fw_name = FW_7465_WIFI_NAME_P7()
    print fw_name[0].strip()
elif name == 'ch7465ce' and file_format == 'PA_TITLE':    
    fw_name = FW_7465_NAME_PA_TITLE()
    print fw_name[0].strip()
elif name == 'ch8568qe' and file_format == 'PA_TITLE':    
    fw_name = FW_8568_NAME_PA_TITLE()
    print fw_name[0].strip()
elif name == 'ch7465ce_wifi' and file_format == 'PA_TITLE':    
    fw_name = FW_7465_WIFI_NAME_PA_TITLE()
    print fw_name[0].strip()
elif parameter_type == '7465p7':
    fw_name = FW_7465_NAME_P7()
    fw_name_choose = fw_name[0].strip()
    rename = Rename_P7(fw_name_choose)
    print rename
elif parameter_type == '8568p7':
    fw_name = FW_8568_NAME_P7()
    fw_name_choose = fw_name[0].strip()
    rename = Rename_P7(fw_name_choose)
    print rename
elif parameter_type == '7465wifip7':
    fw_name = FW_7465_WIFI_NAME_P7()
    fw_name_choose = fw_name[0].strip()
    rename = Rename_P7(fw_name_choose)
    print rename

