#!/usr/bin/env python3
  
# concatena la issue key
import pandas as pd
import csv

datadde = pd.read_csv("DDE.csv")
datadd = pd.read_csv("DD.csv")
#print(data.head())
df_data = open("pls.csv", "w")


df = pd.DataFrame(datadde, columns= ['Issue key'])
df2 = pd.DataFrame(datadd, columns = ['Summary', 'Issue Type', 'Client', 'Project'])

result = df.join(df2, how = "outer")
print(result)

#pd.concat([df, datadd.reindex(df.index)], axis=2)


#print(df)
print (result, file=df_data)
df_data.close()
