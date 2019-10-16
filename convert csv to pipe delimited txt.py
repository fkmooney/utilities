import pandas as pd

file = "Fixed.csv"
df = pd.read_csv(file,  encoding = "ISO-8859-1", header=0) # load data
df.to_csv("Output.txt", sep='|', encoding='utf-8', index=False)
