# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 23:50:49 2021

@author: Win 10
"""

import pandas as pd
import numpy as np
url="C:/Users/Win 10/Documents/FB.csv"
data= pd.read_csv(url)

# head and tail of data
data.head(10)
data.tail(10)


# set header
header=["A","B","C","D","E","F","G"]
data.columns= header

# export file
# we use data.to_csv() function

# data type
data.dtypes

# display all descriptive statistics of data
## Numeric attributes only
data.describe()
## both numeric and object type attibutes
data.describe(include="all")

# basic info of dataframe
data.info()

# replace data
data_2= data.replace('202.130005',np.NaN)

# drop missing value
## use the dropna() function
# DB-API
from dbmodule import connect
## Create connection object
connection= connect('databasename','username','pswd')
## Create cursor object
cursor= connection.cursor()
## Run queries
cursor.execute('select * from mytable')
results= cursor.fetchall()
## Free resoures
cursor.close()
connection.close()




