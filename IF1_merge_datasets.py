#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:40:40 2020

@author: gattigli
2nd attempt. 
program loops through the csv files in the given folder, reads only 
the files with a specific string in the name, and gives back a .csv that contains 
as rows all the cells that were masked and as columns, the means of the three 
channels, with renamed columns (easier to read)

1rst program to run
env: py376

ATTENTION
run the program for every condition
take care of changing the 'experiment' name
take care what it reads and the '*'
here I added a checkup for size particle due to the small particles in Stardist (pre-2021 deep learning model)

go to IF2_merge_all.py 
"""
import pandas as pd
import numpy as np
import os, fnmatch


#run the program for every condition
condition =  '24'
experiment = 'hand1cdx2'
directory = ""
outer_directory = ""

#creates empty dataframes that will be used to loop later
ch1_concatenate = pd.DataFrame()
ch2_concatenate = pd.DataFrame()
ch3_concatenate = pd.DataFrame()
#treshold = 17.5

#loops through files, reads the ones with the 'condition' in the file name, 
#select rows that have Ch1, concatenate the dataframe
for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*' + condition+'*.csv'): #works
        df = pd.read_csv(directory+filename, engine='python')
        df_ch1 = df[df.Ch ==1]#[df.Area > treshold]
        ch1_concatenate = pd.concat([ch1_concatenate, df_ch1])#works
        print(filename) #troubleshoot
        continue
    else:
        continue
# %%
#,select only the colums I'm interested in and rename the mean column. 
#change the Label itself, I cut at the ':c:', so that the labels are the same 
#in every channel
        
ch1_mean = ch1_concatenate[['Label','Mean']]

ch1_mean.rename(columns={
        'Mean':'Mean_Ch1'},
        inplace=True)
ch1_mean['Label'] = ch1_mean.Label.apply(lambda x: x.split(':c:')[0])
#ch1_mean['Label'] = ch1_mean.Label.apply(lambda x: x.split(':Ch2')[0])


#Ch2
for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*'+condition+'*.csv'): #works
        df = pd.read_csv(directory+filename, engine='python')
        df_ch2 = df[df.Ch ==2]#[df.Area > treshold]
        ch2_concatenate = pd.concat([ch2_concatenate, df_ch2])#works
        continue
    else:
        continue
    
ch2_mean = ch2_concatenate[['Label','Mean']]
ch2_mean.rename(columns={
        'Mean':'Mean_Ch2'},
        inplace=True)
ch2_mean['Label'] = ch2_mean.Label.apply(lambda x: x.split(':c:')[0])
#ch2_mean['Label'] = ch2_mean.Label.apply(lambda x: x.split(':Ch3')[0])

#Ch3
for filename in os.listdir(directory):
    if fnmatch.fnmatch(filename, '*' + condition+'*.csv'): #works
        df = pd.read_csv(directory+filename, engine='python')
        df_ch3 = df[df.Ch ==3]#[df.Area > treshold]
        ch3_concatenate = pd.concat([ch3_concatenate, df_ch3])#works
        continue
    else:
        continue
    
    
ch3_mean = ch3_concatenate[['Label','Mean']]
ch3_mean.rename(columns={
        'Mean':'Mean_Ch3'},
        inplace=True)
ch3_mean['Label'] = ch3_mean.Label.apply(lambda x: x.split(':c:')[0])
#ch3_mean['Label'] = ch3_mean.Label.apply(lambda x: x.split(':APD1')[0])


#merge the three df around the common Label. only line I have never run!!!!
merged_df0 = pd.merge(ch2_mean, ch3_mean)
merged_df = pd.merge(ch1_mean, merged_df0)

merged_df.to_csv(outer_directory + experiment + '_'+ condition + '.csv')