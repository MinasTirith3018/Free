# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 19:16:11 2018

@author: Canopus
"""

import numpy as np
import argparse, os, re, copy,subprocess, time
import shutil
import exifread
    
#subprocess.call(["python", "classify.py", "--imgtype", "CR2", "--filename", "12", "--time_long", "8"])

parser = argparse.ArgumentParser()
parser.add_argument('--imgtype', default='CR2',type=str)
parser.add_argument('--filename', default=12, type=int)
parser.add_argument('--time_long', default=8, type=float)
parser.add_argument('--start_folder_number', default=1, type=int)
args = parser.parse_args()

def log(description):
	print(description)

dirlist = os.listdir('.')
dirlist = list(filter(lambda x : x[args.filename-3:args.filename] == args.imgtype, dirlist))
output = '\n'.join(dirlist)
f = open('{:}.txt'.format(args.imgtype), 'w')
f.write(output)
f.close()
     

try:
	lst_f = open('{:}.txt'.format(args.imgtype), 'r')
except:
	error("List file list not found: " + "{:}.txt".format(args.imgtype))


lst = lst_f.read()
lst = lst.replace('\r\n', '\n')
lst = lst.replace('\r', '\n')
lst = lst.split('\n')


def origindate(k): #DateTimeOriginal from EXIF data
    f=open(k,'rb')
    tags=exifread.process_file(f)
    date=str(tags["EXIF DateTimeOriginal"])
    f.close()
    return date

def timecal(x): # Time calculate function
    a=int(x[11:13])*3600+int(x[14:16])*60+int(x[17:19])
    return a
    

n=args.start_folder_number
os.mkdir(("({:})".format(n)))
shutil.copy('{:}'.format(lst[0]),"({:})".format(n))
a1=origindate(lst[0])
b1=timecal(a1)
a2=origindate(lst[1])
b2=timecal(a2)

if (b2-b1<args.time_long):
        shutil.copy('{:}'.format(lst[0]),"({:})".format(n))
        log("Copy {:} to folder ({:})".format(lst[0],n))
        shutil.copy('{:}'.format(lst[1]),"({:})".format(n))
        log("Copy {:} to folder ({:})".format(lst[1],n))   
else:
        shutil.copy('{:}'.format(lst[0]),"({:})".format(n)) 
        log("Copy {:} to folder ({:})".format(lst[0],n))
        n+=1
        log("time change {:}".format(a2))
        os.mkdir(("({:})".format(n)))
        shutil.copy('{:}'.format(lst[1]),"({:})".format(n))
        log("Copy {:} to folder ({:})".format(lst[1],n))	


for i in range(1, int(len(lst)/2)+1) :
        if (2*i+1 == (int(len(lst)))):
            n1=origindate(lst[2*i])
            n0=origindate(lst[2*i-1])
            t1=timecal(n1)
            t0=timecal(n0)
            if ((t1-t0)>args.time_long):
                n+=1
                log("\nChange time {:}".format(n1))
                os.mkdir(("({:})".format(n)))
                shutil.copy('{:}'.format(lst[2*i]),"({:})".format(n))
                log("Change Copy {:} to folder ({:})".format(lst[2*i],n))
            else:
                shutil.copy('{:}'.format(lst[2*i]),"({:})".format(n))
                log("time {:}".format(n1))
                log("Keep to Copy {:} to folder ({:})".format(lst[2*i],n))
        else:    
            n1=origindate(lst[2*i])    
            n2=origindate(lst[2*i+1])
            n0=origindate(lst[2*i-1])
            t1=timecal(n1)
            t2=timecal(n2)
            t0=timecal(n0)
            if ((t1-t0)<=args.time_long):
                if ((t2-t1)<=args.time_long):
                    shutil.copy('{:}'.format(lst[2*i]),"({:})".format(n))        
                    log("time {:}".format(n1))
                    log("Keep to Copy {:} to folder ({:})".format(lst[2*i],n))    
        
                    shutil.copy('{:}'.format(lst[2*i+1]),"({:})".format(n))        
                    log("time {:}".format(n2))    
                    log("Keep to Copy {:} to folder ({:})".format(lst[2*i+1],n))        
    
                else:
                    shutil.copy('{:}'.format(lst[2*i]),"({:})".format(n)) 
                    log("time {:}".format(n1))
                    log("Keep to Copy {:} to folder ({:})".format(lst[2*i],n))
        
                    n+=1
                    os.mkdir(("({:})".format(n)))
                    shutil.copy('{:}'.format(lst[2*i+1]),"({:})".format(n))        
                    log("\nChange time {:}".format(n2))        
                    log("Change Copy {:} to folder ({:})".format(lst[2*i+1],n))
    
            else:
                if ((t2-t1)<=args.time_long):                
                    n+=1
                    log("\nChange time {:}".format(n1))
                    os.mkdir(("({:})".format(n)))
                    shutil.copy('{:}'.format(lst[2*i]),"({:})".format(n))
                    log("Change Copy {:} to folder ({:})".format(lst[2*i],n))
                    shutil.copy('{:}'.format(lst[2*i+1]),"({:})".format(n)) 
                    log("Keep to Copy {:} to folder ({:})".format(lst[2*i+1],n))
                else:
                    n+=1
                    os.mkdir(("({:})".format(n)))
                    shutil.copy('{:}'.format(lst[2*i]),"({:})".format(n)) 
                    log("\nChange time {:}".format(n1))
                    log("Change copy {:} to folder ({:})".format(lst[2*i],n))
                    
                    n+=1
                    os.mkdir(("({:})".format(n)))
                    log("\nChange time {:}".format(n2))
                    shutil.copy('{:}'.format(lst[2*i+1]),"({:})".format(n))
                    log("Change copy {:} to folder ({:})".format(lst[2*i+1],n))