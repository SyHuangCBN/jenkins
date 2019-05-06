# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:03:30 2018

@author: lynn_lin
@changer: gerben_chen
"""

from jenkinsapi.jenkins import Jenkins
import argparse
import sys
import os
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

HELP_EPILOG = '''
Example use:

 python jenkins_parser -u <Jenkins URL> -j <Job Name> -i <Build ID>

 python jenkins_parser -u 'http://10.118.251.119:8080/' -j 'DailyTest_CH7465CE_2_cbn_voice' -i 78 -U cbnmat -P just4mat -n cbn_voice

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
parser.add_argument('-n', '--node', metavar='', type=str, default=None, help='node_account')
''''''
args = parser.parse_args()
url = args.url
job = args.job
username = args.User
password = args.Pwd
#username = 'cbnmat'
#password = 'just4mat'
build_id = args.id
node_account = args.node
#build_id = getBuildId(url, job, username, password)
#print("build_id = %s" %build_id)
'''Default Setting'''
mv_db_list = ["Using Board mv1-1-1,","Using Board mv1-1-2,","Using Board mv1-1-3,","Using Board mv1-1-4,","Using Board mv1-1-5,","Using Board mv1-1-6,",
              "Using Board mv1-1-7,","Using Board mv1-1-8,","Using Board mv1-1-9,","Using Board mv1-1-10,","Using Board mv1-1-11,","Using Board mv1-1-12,",
              "Using Board mv1-1-13,","Using Board mv1-1-14,","Using Board mv1-1-15,","Using Board mv1-1-16,","Using Board mv1-1-17,","Using Board mv1-1-18,",
              "Using Board mv1-1-19,","Using Board mv1-1-20,","Using Board mv1-1-21,","Using Board mv1-1-22,","Using Board mv1-1-23,","Using Board mv1-1-24,",
              "Using Board mv1-1-25,","Using Board mv1-1-26,","Using Board mv1-1-27,","Using Board mv1-1-28,","Using Board mv1-1-29,","Using Board mv1-1-30,",
              "Using Board mv1-1-31,","Using Board mv1-1-32,","Using Board mv1-1-33,","Using Board mv1-1-34,","Using Board mv1-1-35,","Using Board mv1-1-36,",
              "Using Board mv1-2-1,","Using Board mv1-2-2,","Using Board mv1-2-3,","Using Board mv1-2-4,","Using Board mv1-2-5,","Using Board mv1-2-6,",
              "Using Board mv1-2-7,","Using Board mv1-2-8,","Using Board mv1-2-9,","Using Board mv1-2-10,","Using Board mv1-2-11,",
              "Using Board mv1-2-12,","Using Board mv1-3-1,","Using Board mv1-3-2,","Using Board mv1-3-3,"]
'''console log'''
data = getConsoleLog(url, job, username, password, build_id)
for word in range(len(mv_db_list)):
    if mv_db_list[word] in data:
        print (mv_db_list[word][12:-1])
        break
