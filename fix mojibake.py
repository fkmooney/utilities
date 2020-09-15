import pandas as pd 
import ftfy

"""
fixes mojibake in all rows of a one column CSV
and outputs an excel file to ensure special chracters
are preserved in output
"""

df = pd.read_csv("Moji.csv")

for index, row in df.iterrows():
    row['videotitle'] = ftfy.fix_encoding(row['videotitle'])

df.to_excel("Moji_Output.xlsx")