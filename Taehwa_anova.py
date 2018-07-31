# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
#https://partrita.github.io/posts/ANOVA-python/

data=np.genfromtxt('Photo-1807.csv',delimiter=',')
plot1=data[data[:,6]==1,0:8]
plot2=data[data[:,6]==2,0:8]
plot3=data[data[:,6]==3,0:8]

#Amax=1, #Vcmax=2, #Jmax=3, #TPU=4, #Rd=5, #Gm=6
#ud=0, fr=1, ap=2, zs=3


    
ud_1=plot1[plot1[:,7]==0,0:6]
ud_2=plot2[plot2[:,7]==0,0:6]
ud_3=plot3[plot3[:,7]==0,0:6]

fr_1=plot1[plot1[:,7]==1,0:6]
fr_2=plot2[plot2[:,7]==1,0:6]
fr_3=plot3[plot3[:,7]==1,0:6]

ap_1=plot1[plot1[:,7]==2,0:6]
ap_2=plot2[plot2[:,7]==2,0:6]
ap_3=plot3[plot3[:,7]==2,0:6]


zs_1=plot1[plot1[:,7]==3,0:6]
zs_2=plot2[plot2[:,7]==3,0:6]
zs_3=plot3[plot3[:,7]==3,0:6]

sp=['ud','fr','ap','zs']
data=[0,'Amax','Vcmax','Jmax','TPU','Rd','Gm']
Ttest=np.zeros((6,5,2))
Ttest[:,4,1]=[1,2,3,4,5,6]
Ttest[:,4,0]=[1,2,3,4,5,6]

for i in range(0,6):   
    ud=[ud_1[:,i],ud_2[:,i],ud_3[:,i]]
    fr=[fr_1[:,i],fr_2[:,i],fr_3[:,i]]
    zs=[zs_1[:,i],zs_2[:,i],zs_3[:,i]]
    ap=[ap_1[:,i],ap_2[:,i],ap_3[:,i]]
    F_statistic, pVal=stats.f_oneway(ud_1[:,i],ud_2[:,i],ud_3[:,i])
    Ttest[i,0,0],Ttest[i,0,1]=F_statistic, pVal
    F_statistic, pVal=stats.f_oneway(fr_1[:,i],fr_2[:,i],fr_3[:,i])
    Ttest[i,1,0],Ttest[i,1,1]=F_statistic, pVal
    F_statistic, pVal=stats.f_oneway(zs_1[:,i],zs_2[:,i],zs_3[:,i])
    Ttest[i,3,0],Ttest[i,3,1]=F_statistic, pVal
    Ttest[i,2,0:2]=stats.ttest_ind(ap_2[:,i],ap_3[:,i])
    #stacked=np.dstack((ud,fr,zs))
    #ap_st=np.dstack((ap_2[:,i],ap_3[:,i]))
    #mini=min(np.min(stacked),np.min(ap_st))
    #maxi=max(np.max(stacked),np.max(ap_st))
    plt.figure(figsize=(18,12)),\
    plt.subplot(221),plt.boxplot(ud),plt.title('ud_{:}'.format(data[i+1])),\
    plt.subplot(222),plt.boxplot(fr),plt.title('fr_{:}'.format(data[i+1])),\
    plt.subplot(223),plt.boxplot(ap),plt.title('ap_{:}'.format(data[i+1])),\
    plt.subplot(224),plt.boxplot(zs),plt.title('zs_{:}'.format(data[i+1])),plt.savefig('{:}.png'.format(data[i+1]))

#,plt.ylim(np.min(stacked),np.max(stacked)
    
    np.savetxt("stat.csv",Ttest[:,:,0],delimiter=",")
    np.savetxt("Pvalue.csv",Ttest[:,:,1],delimiter=',')
