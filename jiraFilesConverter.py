#!/usr/bin/env python3

import pandas as pd
import csv

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

################################# Reading csv file & selecting important fields #####################################
data = pd.read_csv("Demanda_Dummy.csv")

# create new file
df_demanda_data = open("df_data.csv", "w")

# selection
df = pd.DataFrame(data, columns= ['Client','Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

# save selection in new file
print (df, file=df_demanda_data)
df_demanda_data.close()

# create unique value field "Issue Type"
df["Issue Type"] = 'Demand'
df.to_csv("df_data.csv", index=False)

############################## Gettting neccesary information from Jira .csv file ###################################

# Read csv
data2 = pd.read_csv("DDE.csv")

# selection
df_sumik = pd.DataFrame(data2, columns= ['Summary','Issue key'])

#################################### Issue key & Summary concatenation ##############################################
  
# Read csv
data_df = pd.read_csv("df_data.csv")

# create new file
df_final_data = open("finalData.csv", "w")

# selection
df2 = pd.DataFrame(data_df, columns= ['Issue Type', 'Client', 'Project','Role Title','Role ID','IQN','Status','POC','Resource Start Date','Role Created Date','Resource End Date'])

# Join
result = df_sumik.join(df2, how = "outer")

print(result)

# save result
print (result, file=df_final_data)
df_final_data.close()

