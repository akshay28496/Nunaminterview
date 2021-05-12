#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd

files = ['data.xlsx','data1.xlsx']  

## Method to get sheets of a given file
df_total = pd.DataFrame()
for file in files:                         # loop through Excel files
    if file.endswith('.xlsx'):
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names
        for sheet in sheets:               # loop through sheets inside an Excel file
            if sheet.startswith('Detail_67_'):
                df = excel_file.parse(sheet_name = sheet)
                df_total = df_total.append(df)
df_total.to_csv('detail.csv')


# In[53]:


files = ['data.xlsx','data1.xlsx']  

## Method to get sheets of a given file
df_total = pd.DataFrame()
for file in files:                         # loop through Excel files
    if file.endswith('.xlsx'):
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names
        for sheet in sheets:               # loop through sheets inside an Excel file
            if sheet.startswith('DetailVol_67_'):
                df = excel_file.parse(sheet_name = sheet)
                df_total = df_total.append(df)
df_total.to_csv('detailVol.csv')


# In[52]:


## Method to get sheets of a given file
df_total = pd.DataFrame()
for file in files:                         # loop through Excel files
    if file.endswith('.xlsx'):
        excel_file = pd.ExcelFile(file)
        sheets = excel_file.sheet_names
        for sheet in sheets:               # loop through sheets inside an Excel file
            if sheet.startswith('DetailTemp_67_'):
                df = excel_file.parse(sheet_name = sheet)
                df_total = df_total.append(df)
df_total.to_csv('detailTemp.csv')


# In[62]:


import pandas as pd
import numpy as np


# In[63]:


## To perform Downloadsample for detailTemp.csv
df_sales = pd.read_csv(
    'detailTemp.csv', 
    parse_dates=['Realtime'], 
    index_col=['Realtime']
)
df_sales


# In[64]:


## Downsampling to 1sample per minute
df =df_sales.resample('1Min',origin='start').sum()
df.to_csv('detailTempDownsampling.csv')


# In[57]:


df = pd.read_csv('detailTempDownsampling.csv')
df.head(10)


# In[ ]:


## To perform Downloadsample for detail.csv
df_sales = pd.read_csv(
    'detail.csv', 
    parse_dates=['Realtime'], 
    index_col=['Realtime']
)
## Downsampling to 1sample per minute
df =df_sales.resample('1Min',origin='start').sum()
df.to_csv('detailDownsampling.csv')


# In[ ]:


## To perform Downloadsample for detailVol.csv

df_sales = pd.read_csv(
    'detailVol.csv', 
    parse_dates=['Realtime'], 
    index_col=['Realtime']
)
## Downsampling to 1sample per minute
df =df_sales.resample('1Min',origin='start').sum()
df.to_csv('detailVolDownsampling.csv')

