#!/usr/bin/env python3

# bring summary and IK from the csv that already has it
import pandas as pd
import csv

data = pd.read_csv("DDE.csv")

df_summaryandik = open("summ_n_ik.csv", "w")
df = pd.DataFrame(data, columns= ['Summary', 'Issue key'])


#print(df)
#print (df, file=df_summaryandik)
df_summaryandik.close()
