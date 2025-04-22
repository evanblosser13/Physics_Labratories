# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:56:12 2023

@author: galac
"""


import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

fname = 'run1data.csv'

data = np.loadtxt(fname, skiprows=2, delimiter=',')

data_size = np.shape(data)
print(data_size)



# 713 Frames from mathmatica? 
time_frame = np.linspace(start=1,stop=712,num=712)
# Debugg
# print(time)

#################
## Conversions ##
#######################################
# Time from frames to minutes         #
# - 7.97754902 sec/frame              #
# - 60 seconds in a min.              #
time = time_frame*7.97754902*(1/60)   #
##                                  ###
# Distance from pixels to mm          #
# - 1.75723mm/pixel                   #
distance = data*1.75723               #
#######################################

##############
# mean & std #
mean_position = np.mean(distance)  
std_position  = np.sqrt(mean_position/data_size-1)


##########
## Plot ##
#####################################
fig = plt.figure('Cavendish Run 1') #
ax = fig.add_axes([0.1,0.1,0.8,0.8])


plt.yscale('log')
ax.tick_params(axis='y', which='minor')
ax.errorbar(time,mean_position,color='k',
            marker='o',markersize=4, markerfacecolor='white',markeredgecolor='black',markeredgewidth=1.0,
            linestyle='', yerr=std_position, capsize=2, label='data', zorder=1)

ax.set_xlabel('time (days)')
ax.set_ylabel('activity (counts per minute)')
ax  = plt.axes()
ax.plot(time,distance)
plt.show()

plt.scatter(time,distance)