#!/usr/bin/env python3

import pandas as pd
import csv

#data2 = pd.read_csv("DDE.csv")
#print(data2.head())

# leer el csv
data = pd.read_csv("Demanda_Dummy.csv")

# make new csv with wanted results
df_demanda_data = open("df_data.csv", "w")

# to select the fields that are important to you
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])
print (df, file=df_demanda_data)
df_demanda_data.close()

df["Issue Type"] = 'Demand'
df.to_csv("df_data.csv", index=False)
#df["Summary"] = ""
#df.to_csv("df_data.csv", index=False)
# just to add fields for the newly made csv (df_data.csv)


#####################################################################################################################

data2 = pd.read_csv("DDE.csv")

#df_dde_data = open("summ_n_ik.csv", "w")
#print(data.head())
df_sumik = pd.DataFrame(data2, columns= ['Summary','Issue key'])
print(df_sumik)
#print(df_sumik)
#print(data.head()) // shows everything
#print (df_sumik, file=df_dde_data)
#df_dde_data.close()

#####################################################################################################################
  
# concatena la issue key

#data3 = pd.read_csv("summ_n_ik.csv")
#print(data3)
data_df = pd.read_csv("df_data.csv")
df_final_data = open("finalData.csv", "w")
print()

#df3 = pd.DataFrame(data3, columns= ['Summary', 'Issue key'])
#print(df3)
df2 = pd.DataFrame(data_df, columns= ['Issue Type', 'Client', 'Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])
print(df2)
result = df_sumik.join(df2, how = "outer")


print(result)

print (result, file=df_final_data)
df_final_data.close()

