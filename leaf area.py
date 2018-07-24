# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:07:46 2018

@author: Seo Yukyeong
"""
#%%

from numpy import *
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import subprocess
import cv2
#%% 사진파일이 저장된 디렉토리 경로
cd C:\Users\Seo Yukyeong\Downloads\pa
#%%
#파일 이름 리스트를 만들어 두어야 한다.
f=open('name.txt','r')

filelist=[]
for line in f:
    filelist.append(line.strip())
f.close()

area=np.zeros(len(filelist))
cnt=0
for i in filelist: 
            imag=plt.imread(i+'.jpg')
            if (np.shape(imag)!=(1773,2481)): 
                imag=imag[:,:,0]     #사진파일이 회색조나, 흑백이어야만 한다.
            ret,thresh1 = cv2.threshold(imag,170,255,cv2.THRESH_BINARY) #(자동으로 threshold 하는게 아니라, threshold 범위를 손으로 지정)
          :}.png'.format(i))
            time.sleep(1)  cut=thresh1[int(1773*0.55)+20:1773,int(2481*0.3):int(2481*0.8)]#잎이 존재하는 영역 잘라내기. 여기는 매번 수정해줘야 한다.           
            plt.figure(figsize=(10,6)),plt.contourf(cut),plt.colorbar(),plt.axis('equal'),plt.title('{:}'.format(i)),plt.savefig('{
            acnt=0
            for x in range(0,778):
                for y in range(0,1240):
                        if (cut[x,y]<50): acnt+=1
            acnt=acnt/(118.2*118.2)
            area[cnt]=acnt  
            cnt+=1



np.savetxt('area.csv',area)

