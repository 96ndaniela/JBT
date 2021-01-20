#!/usr/bin/env python3

#print('Hello World!')
#print( )
import pandas as pd
import csv

data = pd.read_csv("DDE.csv")
print(data.head())
df_data = open("issuekey.csv", "w")
df = pd.DataFrame(data, columns= ['Issue key'])
print(df)
print (df, file=df_data)
df_data.close()
