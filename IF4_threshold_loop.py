#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:29:17 2022

just looping through csv files to obtain the number of positive cells, given a user-defined threshold

@author: gattigli

env: py376
"""
import pandas as pd
import numpy as np
import os, fnmatch

#directory with files to loop through
directory = ''
experiment = 'hand1cdx2'
print(experiment)

threshold_Ch1=15.43
threshold_Ch2=4.632
threshold = 0

channel = 1
if channel == 1:
    threshold = threshold_Ch1;
elif channel == 2:
    threshold = threshold_Ch2;

#print (perc)
# %%
ch_merge = pd.DataFrame()

for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*' + experiment + '*.csv'): 
        print(filename)
        df = pd.read_csv(directory + filename)
        file = filename.split('_')[1].split('.')[0]
        
        df_ch = df[['Mean_Ch'+ str(channel)]]
        #newcolumn = 'Ch'+ str(channel) + ':' +file
        #df_ch.rename(columns={'Mean_Ch'+ str(channel): newcolumn}, inplace = True)

        #concatenate the dataframes
        complete_list_len = len(df_ch)

        #threshold
        ch_thresh = df_ch[df_ch['Mean_Ch'+ str(channel)] >= threshold]
        thresh_list_len = len(ch_thresh)#ok until here

        #percentage of positive cells
        percent = (thresh_list_len / complete_list_len)*100
        print('In the condition '+ file + 'for the channel' + str(channel))
        print('There are '+str(thresh_list_len)+' positive cells out of '+str(complete_list_len))
        print ('The percentage of positive cells is ' + str("%.2f" % percent) + '%')
        ch_thresh = ch_thresh.reset_index()
        #del ch_thresh['index']
        #ch_merge = pd.merge(ch_merge, ch_thresh , left_index = True, right_index=True, how='outer')#works

#ch_merge.to_excel(outer_directory + experiment + '_threshold_' + marker + '.xlsx')