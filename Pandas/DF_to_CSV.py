import os
import pandas as pd 
os.chdir("/storage/emulated/0/PythonAadil/Pandas")


df=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=["A","B","C"])

df.to_csv("DF_to_CSV.csv",index=False)