import pandas as pd


df = pd.read_csv('wkreport2021.txt', sep='|')
df = df.drop(columns=['College','.com','Other'])
df["TotalRetail"] = df["TotalRetail"].astype(int)

df.to_csv('Sample.txt', sep='|', index=False)
