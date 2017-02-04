#!/usr/bin/env python3
import os
import time
from subprocess import Popen, DEVNULL,PIPE
import csv
# import re

def creat( name ):
    pass
    p = {} # ip -> process
    for n in range(1, 255): # start ping processes
        ip = "223.239.221.%d" % n
        p[ip] = Popen(["ping", "-c", "1", "-n", "-W", "2", ip], stdout=DEVNULL)
        # NOTE: you could set stderr=subprocess.STDOUT to ignore stderr also
    file=open(name,'w')
    while p:
        for ip, proc in p.items():
            if proc.poll() is not None: # ping finished
                del p[ip] # remove from the process list
                if proc.returncode == 0:
                    print('%s active' % ip)
                    file.write(ip)
                    file.write("\n")
                #elif proc.returncode == 1:
                    #print('%s no response' % ip)
                #else:
                    #print('%s error' % ip)
                break
def comp(name1  ,name2):
    with open(name1, 'r') as csvfile:
        spamreader = csv.reader(csvfile,  delimiter='\n')
        print("disconnected ips are as follows ")
        for row in spamreader:
            strg1=str(row)
            strg1=strg1[2:len(strg1)-2]
            #print(strg1)
            if strg1 not in open(name2).read():
                #print (strg1)
                Popen(["ping", "-c 1", strg1], stdout = PIPE)
                pid = Popen(["arp", "-n", strg1], stdout=PIPE)
                s = pid.communicate()
                s=str(s);
                print(s)
                # s=Popen([s|grep *:*:*:*:*])
                print( strg1,s)


if __name__ == '__main__':

    # while True:
    str1="test1.txt"
    str2="test2.txt"
    # print("during 1st scan "+'\n')
    creat(str1)
    # print("\n")
    time.sleep(2)
    # print("during 2nd scan "+'\n')
    creat(str2)
    comp(str1,str2)
