# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:51:50 2021

@author: lordm
"""

'''
Webscrap Helpers
'''


import pandas as pd
import numpy as np
from datetime import datetime
from bs4 import BeautifulSoup


def open_website():    
    return "open"


def get_table(html, min_humans = 6, min_rounds = 15):
    
    # make soup and get all tables
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.findAll('table')
    tbl = tables[0]

    rows = tbl.find_all('tr')
    column_names = [x.get_text() for x in rows[0].find_all('th')]
    column_names[1] = 'Date'
    
    # table content
    data = np.array([[column.get_text() for column in row.find_all('td')]
                           for row in rows[1:]])
    data = np.delete(data, 8, 1)
    df = pd.DataFrame(data, columns=column_names)
    df.drop(columns=['Time', 'Filled', 'Format', '# Teams'], inplace=True)
    
    # convert time into date
    df.Date = string2time(df.Date)
    # filter by minimum number of participating humans and rounds drafted
    df['# Humans'] = pd.to_numeric(df['# Humans'])
    df['RoundsFinished'] = pd.to_numeric(df['RoundsFinished'])
    df = df[[h>= 6 and rf>=15 for (h,rf) in zip(df['# Humans'], df['RoundsFinished'])]]
    
    return df

def string2time(time_col):
    time_col = [datetime.strptime(date_string, '%m/%d/%Y, %I:%M %p').date()
                for date_string in time_col]
    return time_col


def read_mockdraft():
    df_mockdraft = None
    return df_mockdraft


