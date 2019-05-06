# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:03:30 2018

@author: Gerben_Chen
"""

from jenkinsapi.jenkins import Jenkins
import argparse
import sys, os, time

def getConsoleLog(url, jobName, username, password, BUILD_ID):
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_build(BUILD_ID)
    return lgb.get_console()

def getBuildId(url, jobName, username, password):
    J = Jenkins(url, username, password)
    job = J[jobName]
    lgb = job.get_last_good_build()
    return lgb.get_revision()

def check_rootfsboot(node_account):
    rootfsboot_result = os.popen("cat /home/%s/cbn/boardfarm/results/test_results.json | jq '.test_results[0].grade' | sed 's/\"//g'" % node_account).readlines()    
    if rootfsboot_result == "FAIL":
	return rootfsboot_result
 
HELP_EPILOG = '''
Example use:

 python jenkins_parser -u <Jenkins URL> -j <Job Name> -i <Build ID>

 python jenkins_parser -u 'http://10.118.252.30:8080/' -j 'DailyTest_CH7465CE_2_cbn_voice' -i 78 -U cbnmat -P just4mat

'''
'''
Read command-line arguments, return a simple configuration for running tests.
'''

parser = argparse.ArgumentParser(description='',
								 usage='',
								 formatter_class=argparse.RawDescriptionHelpFormatter,
								 epilog=HELP_EPILOG)
parser.add_argument('-u', '--url', metavar='', type=str, default=None, help='Jenkins URL')
parser.add_argument('-j', '--job', metavar='', type=str, default=None, help='Job Name')
parser.add_argument('-U' ,'--User', metavar='',type=str,default=None , help='Username')
parser.add_argument('-P' ,'--Pwd', metavar='',type=str,default=None , help='Password')
parser.add_argument('-i', '--id', metavar='', type=int, default=None, help='Build ID')
parser.add_argument('-t', '--test', metavar='', type=str, default=None, help='Test project token')
parser.add_argument('-n', '--node', metavar='', type=str, default=None, help='node_account')

args = parser.parse_args()
url = args.url
job = args.job

username = args.User
password = args.Pwd
testsuite = args.test

#username = 'cbnmat'
#password = 'just4mat'
build_id = args.id
node_account = args.node

#build_id = getBuildId(url, job, username, password)
#print("build_id = %s" %build_id)
error_dict = {'FAIL':"RootFsBootTest"}

error_in_data = []
rootfsboot_result = check_rootfsboot(node_account)
if rootfsboot_result == "FAIL" and rootfsboot_result != None:
    error_in_data.append('FAIL')
data = getConsoleLog(url, job, username, password, build_id)
    
if len(error_in_data) > 0 : 
    for i in range(len(error_in_data)):
        print (error_dict[error_in_data[i]])
    #sys.exit(1)
    #raise Exception(error_in_data)

localtimes = time.strftime("%Y%m%d",time.localtime())

try:
    timeout = os.popen("cat ~/cbn/dailytimeout/%s/timeout.txt" % localtimes).readlines()
    #print timeout
    times= int(timeout[0].strip())
except:
    os.makedirs("/home/%s/cbn/dailytimeout/%s"% (node_account,localtimes))
    os.popen("echo '0' > ~/cbn/dailytimeout/%s/timeout.txt" % localtimes).readlines()
    timeout = os.popen("cat ~/cbn/dailytimeout/%s/timeout.txt"% localtimes).readlines()
    #print timeout
    times= int(timeout[0].strip())

times += 1
#print times

if testsuite != None and times < 5: 
    os.popen("echo '%s' > ~/cbn/dailytimeout/%s/timeout.txt" % (times,localtimes)).readlines()
    #print "curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.251.119:8080/job/%s/build?token=%s" % (job,testsuite)
    os.system("curl -u admin:1efb06decbc9a2daceb595da61a555d6 http://10.118.252.30:8080/job/%s/build?token=%s" % (job,testsuite))

#data = getConsoleLog('http://10.118.251.119:8080/', 'DailyTest_CH7465CE_2_cbn_voice', 'cbnmat', 'just4mat', 78)
#print(data)
