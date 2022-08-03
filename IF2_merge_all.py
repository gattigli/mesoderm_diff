#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:37:33 2020

@author: gattigli

just merging the files coming from the IF1_merge_datasets.py
15.12.20: it works, I win
2nd program to run
env: py376

go to seaborn_plots.py for plotting directly the (outer_dir + experiment + 'Ch1' + '.csv') 
or to IF3_GMM.py to calculate the threshold for the (outer_dir + experiment + 'conc_Ch3' + '.csv')
"""

import pandas as pd
import numpy as np
import os, fnmatch
import openpyxl

directory = ""
outer_dir = ""
experiment = 'Tbx6Foxa2'
#fileorder = ['epi', '000', '0-75', '1-5', '3', '6', '12', '24']

splitpoint = '_'

ch1_merge = pd.DataFrame()
ch2_merge = pd.DataFrame()
ch3_merge = pd.DataFrame()
df_ch1 = pd.DataFrame()
ch1_concatenate = pd.DataFrame()
ch2_concatenate = pd.DataFrame()
ch3_concatenate = pd.DataFrame()


for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*' + experiment + '*.csv'):
        file = filename.split(splitpoint)[1].split('.')[0]
        df = pd.read_csv(directory+filename, engine='python')
        df_ch1 = df[['Mean_Ch1']]
        ch1_concatenate = pd.concat([ch1_concatenate, df_ch1])
        df_ch1.rename(columns={'Mean_Ch1': file}, inplace = True)
        ch1_merge = pd.merge(ch1_merge, df_ch1 , left_index = True, right_index=True, how='outer')#works

for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*' +experiment+'*.csv'):
        file = filename.split(splitpoint)[1].split('.')[0]
        df = pd.read_csv(directory+filename, engine='python')
        df_ch2 = df[['Mean_Ch2']]
        ch2_concatenate = pd.concat([ch2_concatenate, df_ch2])
        df_ch2.rename(columns={'Mean_Ch2': str(file)}, inplace=True)
        ch2_merge = pd.merge(ch2_merge, df_ch2 , left_index = True, right_index=True, how='outer')#works
        
for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*' +experiment+'*.csv'):
        file = filename.split(splitpoint)[1].split('.')[0]
        df = pd.read_csv(directory+filename, engine='python')
        df_ch3 = df[['Mean_Ch3']]
        ch3_concatenate = pd.concat([ch3_concatenate, df_ch3])
        df_ch3.rename(columns={'Mean_Ch3': str(file)}, inplace=True)
        ch3_merge = pd.merge(ch3_merge, df_ch3 , left_index = True, right_index=True, how='outer')#works
        
ch1_concatenate.to_csv(outer_dir + experiment + 'conc_Ch1' + '.csv')
ch2_concatenate.to_csv(outer_dir + experiment + 'conc_Ch2' + '.csv')
ch3_concatenate.to_csv(outer_dir + experiment + 'conc_Ch3' + '.csv')
ch1_merge.to_csv(outer_dir + experiment + 'Ch1' + '.csv')
ch2_merge.to_csv(outer_dir + experiment + 'Ch2' + '.csv')
ch3_merge.to_csv(outer_dir + experiment + 'Ch3' + '.csv')