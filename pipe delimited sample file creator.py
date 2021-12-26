import pandas as pd


df = pd.read_csv('BNN-bnwkreport2021.txt', sep='|')
df = df.drop(columns=['BNCollege','BN.com','BarnesNoble'])
df["TotalRetail"] = df["TotalRetail"].astype(int)

df.to_csv('AMZ_Studios_Sample.txt', sep='|', index=False)