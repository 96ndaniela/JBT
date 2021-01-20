#!/usr/bin/env python3
  
# concatena la issue key
import pandas as pd
import csv

datadde = pd.read_csv("DDE.csv")
#print(data.head())
df_data = open("issuekey.csv", "w")
df = pd.DataFrame(data, columns= ['Issue key'])

datadd = pd.read_csv("DD.csv") 
pd.concat([df, datadd.reindex(df.index)], axis=2)


print(df)
print (df, file=df_data)
df_data.close()
