#!/usr/bin/env python3

import pandas as pd
import csv

# leer el csv
data = pd.read_csv("Demanda_Dummy.csv")
#print(data.head()) // shows everything
# make new csv with wanted results
df_data = open("df_data.csv", "w")

# to show the fields that are important to you
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','POC','Resource Start Date','Role Created Date','Resource End Date'])

print (df, file=df_data)
df_data.close()
df["Issue Type"] = 'Demand'
df.to_csv("df_data.csv", index=False)
df["Summary"] = ""
df.to_csv("df_data.csv", index=False)



# just to add fields for the newly made csv (df_data.csv)
