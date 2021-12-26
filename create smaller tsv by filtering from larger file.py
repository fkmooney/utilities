import pandas as pd 
pd.set_option('display.max_columns', None)

f = "Netflix_NPD_2020-05-01-08-00-11.tsv"

df = pd.DataFrame()
number = 1

for chunk in pd.read_csv(f, sep="|", chunksize=4000000):
	chunk = chunk.drop(['season_descriptor',
	'account_last_scrape_at', 'account_profile_last_scrape_at', 'profile_is_kids'], 1)
	chunk = chunk[(chunk['date_of_view'] > '2019-01-01')]
	df = df.append(chunk)
	print(number)
	number = number + 1



df.to_csv("shorter w series.tsv", sep="|")