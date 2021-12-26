import os
import glob


files = glob.glob('*_Rankings.csv')

for file in files:
    parts = file.split('Scraped',)  # [date, _ranking.csv]
    new_name = '{}_Longtail{}'.format(parts[0], parts[1])  # year_2000.jpg
    os.rename(file, new_name)