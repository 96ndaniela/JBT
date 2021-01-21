#!/usr/bin/env python3
  
# concatena la issue key
import pandas as pd
import csv

datadde = pd.read_csv("DDE.csv")
datadd = pd.read_csv("Demanda_Dummy.csv")

df_final = open("final_report.csv", "w")


df1 = pd.DataFrame(datadde, columns= ['Summary', 'Issue key'])
df2 = pd.DataFrame(datadd, columns = [ 'Issue Type', 'Client', 'Project', 'Role Title', 'Role ID', 'IQN', 'Status', 'POC', 'Resource Start Date', 'Role Created Date', 'Resource End Date'])

result = df1.join(df2, how = "outer")


# show everything 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

print(result)
#print and save on the file
print (result, file=df_final)
#print the file itself to show results.
print(df_final)
df_final.close()
