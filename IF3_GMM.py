#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:41:11 2021

@author: gattigli
gaussian mixture model to apply to my violin plots

theory of GMM and implementation https://towardsdatascience.com/gaussian-mixture-models-explained-6986aaf5a95
practical implementation: https://stackoverflow.com/questions/10143905/python-two-curve-gaussian-fitting-with-non-linear-least-squares
practical implementation: https://stackoverflow.com/questions/35990467/fit-two-gaussians-to-a-histogram-from-one-set-of-data-python

API reference: https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture
https://jakevdp.github.io/PythonDataScienceHandbook/05.12-gaussian-mixtures.html

weights explanation: https://stats.stackexchange.com/questions/476335/meaning-of-gaussian-mixture-weights
probability density estimation: https://machinelearningmastery.com/probability-density-estimation/

env: py376

to get the number of positive cells per condition go to IF4_threshold_loop.py
"""
import matplotlib.mlab
from scipy.stats import norm
import numpy as np
import os, fnmatch
import pandas as pd
from matplotlib import pyplot as plt 
from sklearn.mixture import GaussianMixture
import seaborn as sns

directory = ''
file = 'TNanogconc_Ch3.csv'
sheet = 'Sheet8'
#outer_directory = '/Users/gattigli/Desktop/transfer2110/2206_IF/Tbx6Foxa2/mergefiles/GMM/'

graph_name = 'experiment1'
form = '.pdf'

df = pd.read_csv(directory + file)
df = df[df.columns[1:2]]
#df = df.reshape(1, -1)
# %%
gm = GaussianMixture(n_components=2, random_state=0).fit(df)
probs = GaussianMixture.predict_proba(gm, df)
#print(probs[:5].round(4))
labels = GaussianMixture.predict(gm, df)

m1, m2 = gm.means_
w1, w2 = gm.weights_
c1, c2 = gm.covariances_
#there is also precisions, precisions_cholesky, 
threshold = np.mean(gm.means_)
#histdist = plt.hist(df, bins=40)
print('First gaussian. Mean: ' + str(m1) + ' and weight: ' + str(w1))
print('Covariances: ' + str(c1) +str(c2))
print('Second gaussian. Mean: ' + str(m2) + ' and weight: ' + str(w2))
print('The mean of the two means is: ' + str(threshold))
print('Was convergence reached in fit()? :', str(gm.converged_))
print('Number of step used by the best fit of EM to reach the convergence: ', str(gm.n_iter_))
# %%
df_probs = pd.DataFrame(probs)
#df_probs.to_excel(excel_writer = outer_directory + 'probs' + '.xlsx')
df_labels = pd.DataFrame(labels)
#df_labels.to_excel(excel_writer = outer_directory + 'labels' + '.xlsx')
merge_probs_df = pd.merge(df_probs, df, left_index=True, right_index=True)
merge_probs_df.columns = ['neg', 'pos', 'fluorescence']
#%%
# then shift + enter
percentage = 0.70
neg_df = merge_probs_df.loc[(merge_probs_df.neg > percentage)]
threshold_0 = neg_df[neg_df.fluorescence == neg_df.fluorescence.max()]
print(threshold_0)
print('Number of data points contained by the '+ str(percentage) + ' threshold: ' + str(len(neg_df)) + ', which is ' + str(len(neg_df)/len(df)))

pos_df = merge_probs_df.loc[(merge_probs_df.pos > percentage)]
threshold_1 = pos_df[pos_df.fluorescence == pos_df.fluorescence.min()]
print(threshold_1)
print('Number of data points contained by the '+ str(percentage) + ' threshold: ' + str(len(pos_df)) + ', which is ' + str(len(pos_df)/len(df)))
print('Total number of cells: '+ str(len(df)))
print('This leaves out '+ str(len(df)-len(neg_df)-len(pos_df)) + ' cells.')
#%%
plt.hist(df, bins=100)
#plt.axvline(x = 1417.457, color='black', linestyle='-')
#plt.axvline(x = 1570.303, color='red', linestyle='--')
plt.title(str(percentage)+' confidence GMM')
plt.show()
