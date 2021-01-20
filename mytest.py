#!/usr/bin/env python3

#print('Hello World!')
#print( )
import pandas as pd
import csv


data = pd.read_csv("Demanda_Dummy.csv")
print(data.head())
df_data = open("df_data.csv", "w")
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','POC','Resource Start Date','Role Created Date','Resource End Date'])
#print(df)
print (df, file=df_data)
df_data.close()
#print( )
#print('Hello World!')


