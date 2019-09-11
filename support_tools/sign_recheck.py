# -*- coding: utf-8 -*-

"""
Created on Thu Dec 14:30:30 2018

@author: Gerben_chen
"""

import sys, os, re, time
import argparse




def SignPAandP7Check(localtimes, searchfile):
    '''Check PA And P7 In File Or Not'''    
    status = False   
    search = os.popen('find /home/cbn/FW_space/ -name "%s"' % (searchfile)).readlines()    
    for value in search: 
        head_end = searchfile.split('*')
        print head_end[0].strip()
        print head_end[1].strip()
        if (head_end[0].strip() in value) and (head_end[1].strip() in value):
            print 'Check Config In File : %s...PASS' % search
            status = True        
    if status == False:
        print 'Check Config In File : %s...FAIL'% search
        if fw_name == 'ch8568qe' and fw_parameter == 'PA':
            TriggerJenkins8568_PA(search,searchfile)
        elif fw_name == 'ch8568qe' and fw_parameter == 'p7':
            TriggerJenkins8568_P7(search,searchfile)
        elif fw_name == 'ch7465ce' and fw_parameter == 'PA':
            TriggerJenkins7465_PA(search,searchfile)
        elif fw_name == 'ch7465ce' and fw_parameter == 'p7':
            TriggerJenkins7465_P7(search,searchfile)

def TriggerJenkins8568_P7(search,searchfile):
    '''Restart Trigger DailyBuild and DailySign'''     
    print 'Restart Trigger CH8568QE DailySign'    
    #os.system("cp %s /home/cbn/FW_space/" % search[0].strip()) 
    time.sleep(60)
    os.system("curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.252.30:8080/job/DailySign_CH8568QE/build?token=dailysign8568")
    
def TriggerJenkins7465_PA(search,searchfile):
    '''Restart Trigger DailyBuild and DailySign'''    
    localtimes = time.strftime("%Y%m%d",time.localtime())    
    try:
        timeout = os.popen("cat ~/cbn/dailytimeout/%s/timeout7465.txt" % localtimes).readlines()
        #print timeout
        times= int(timeout7465[0].strip())
    except:
        os.makedirs("/home/cbn_ixia/cbn/dailytimeout/%s"% localtimes)
        os.popen("echo '0' > ~/cbn/dailytimeout/%s/timeout7465.txt" % localtimes).readlines()
        timeout = os.popen("cat ~/cbn/dailytimeout/%s/timeout7465.txt"% localtimes).readlines()
    #print timeout
        times= int(timeout[0].strip())
    times += 1  
    print 'Restart Trigger CH7465LG DailyBuild'        
    if times < 4 :
	os.popen("echo '%s' > ~/cbn/dailytimeout/%s/timeout7465.txt" % (times,localtimes)).readlines()    
        os.system("curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.252.30:8080/job/DailyBuild_CH7465CE/build?token=dailybuild7465")
        sys.exit(1)
    else:
        print "Restart Trigger CH7465CE DailyBuild Fail....SKIP And Trigger CH8568QE"
        os.system("curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.252.30:8080/job/DailyBuild_CH8568QE/build?token=dailybuild8568")        
        sys.exit(1)
def TriggerJenkins8568_PA(search,searchfile):
    '''Restart Trigger DailyBuild and DailySign'''  
    localtimes = time.strftime("%Y%m%d",time.localtime())
    try:
        timeout = os.popen("cat ~/cbn/dailytimeout/%s/timeout8568.txt" % localtimes).readlines()
        #print timeout
        times= int(timeout8568[0].strip())
    except:
        os.makedirs("/home/ch8568qe_test/cbn/dailytimeout/%s"% localtimes)
        os.popen("echo '0' > ~/cbn/dailytimeout/%s/timeout8568.txt" % localtimes).readlines()
        timeout = os.popen("cat ~/cbn/dailytimeout/%s/timeout8568.txt"% localtimes).readlines()
    #print timeout
        times= int(timeout[0].strip())
    times += 1       
    print 'Restart Trigger CH8568QE DailyBuild'
    if times < 4:
	os.popen("echo '%s' > ~/cbn/dailytimeout/%s/timeout8568.txt" % (times,localtimes)).readlines()
        os.system("curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.252.30:8080/job/DailyBuild_CH8568QE/build?token=dailybuild8568")
        sys.exit(1)
    else:
        print "Restart Trigger CH8568QE DailyBuild Fail"        
        sys.exit(1)
def TriggerJenkins7465_P7(search,searchfile):
    '''Restart Trigger DailyBuild and DailySign'''
    #os.system("cp %s /home/cbn/FW_space/" % search[0].strip()) 
    time.sleep(60)
    print 'Restart Trigger CH7465LG DailyBuild'
    os.system("curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.252.30:8080/job/DailySign_CH7465CE/build?token=dailysign7465")

HELP_EPILOG = '''
Example use:

 python jenkins_parser -u <Jenkins URL> -j <Job Name> -i <Build ID>

 python jenkins_parser -u 'http://10.118.252.30:8080/' -j 'DailyTest_CH7465CE_2_cbn_voice' -i 78 -U cbnmat -P just4mat -n cbn_voice

'''
'''
Read command-line arguments, return a simple configuration for running tests.
'''

parser = argparse.ArgumentParser(description='',
								 usage='',
								 formatter_class=argparse.RawDescriptionHelpFormatter,
								 epilog=HELP_EPILOG)

parser.add_argument('-p' ,'--parameter', metavar='',type=str,default=None , help='check parameter P7 or PA')
parser.add_argument('-n', '--fwname', metavar='', type=str, default=None, help='fw_name')
''''''
args = parser.parse_args()
fw_name = args.fwname
fw_parameter = args.parameter
#address = args.address
#token = args.token
#job_name = args.jobname

localtimes = time.strftime("%Y%m%d",time.localtime())
#print 'Time Now : %s' % localtimes
#config for date
#searchlist = ['CH8568QE-LGI-NOPP-PC15-7.11.46.22-%s-SH-PA'%localtimes,'CH7465LG-NCIP-6.15.18.26-%s-SH-PA'%localtimes,'CH8568QE-LGI-NOPP-PC15-7.11.46.22-%s-SH-PA.NNEMN.p7'%localtimes,'CH7465LG-NCIP-6.15.18.26-%s-SH-PA.NNEMN.p7'%localtimes]
searchlist = {'ch8568qePA':'CH8568LG-NCIP-*-%s-SH-PA'%localtimes,'ch7465cePA':'CH7465LG-NCIP-*-%s-SH-PA'%localtimes,'ch8568qep7':'CH8568LG-NCIP-*-%s-SH-PA.NNEMN.p7'%localtimes,'ch7465cep7':'CH7465LG-NCIP-*-%s-SH-PA.NNEMN.p7'%localtimes}

check_main = str(fw_name) + str(fw_parameter)

if fw_name == 'ch8568qe' and fw_parameter == 'p7':
    SignPAandP7Check(localtimes,searchlist[check_main])
elif fw_name == 'ch8568qe' and fw_parameter == 'PA':
    SignPAandP7Check(localtimes,searchlist[check_main])
elif fw_name == 'ch7465ce' and fw_parameter == 'p7':
    SignPAandP7Check(localtimes,searchlist[check_main])    
elif fw_name == 'ch7465ce' and fw_parameter == 'PA':
    SignPAandP7Check(localtimes,searchlist[check_main])
