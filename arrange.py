#!/usr/bin/env python3
  
import pandas as pd
import csv

# leer el csv
data = pd.read_csv("df_data.csv")
# make new csv with wanted results
arr_data = open("arr_data.csv", "w")

# to show the fields that are important to you
# as admin, it supposedly lets you download a csv with the issue key so it's just adding it in the columns to show
df = pd.DataFrame(data, columns= ['Summary','Issue Type','Client','Project','Role Title','Role ID','POC','Resource Start Date','Role Created Date','Resource End Date'])

# show everything 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

#print result
print(df)
print (df, file=arr_data)
arr_data.close()
