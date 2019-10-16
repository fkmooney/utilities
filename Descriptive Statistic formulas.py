import pandas as pd
import numpy as np
from scipy import stats

file = "2018-08-08.csv"
df = pd.read_csv(file, encoding="ISO-8859-1", header=1)

# Extract all of the scores from the data set
scores = df['TW Total(08/05/18)'].tolist()

# Sum up all of the scores
sum_score = sum(scores)

# Get the number of observations
num_score = len(scores)

# Now calculate the average
avg_score = sum_score / num_score
print('avg_vol: ', avg_score)

# Isolate prices from the data set
prices = df['Price'].tolist()

# Find the number of prices
num_price = len(prices)

# We'll sort the prices into ascending order
sorted_prices = sorted(prices)

# calc median using numpy
price_median = np.nanmedian(sorted_prices)
print('price_median: ', price_median)

# calc min and max
min_price = min(prices)
max_price = max(prices)
print('min:', min_price, 'max: ', max_price)

mode_price = stats.mode(prices)
print('mode_price: ', mode_price)

price_range = max_price - min_price
print('price_range: ', price_range)


def stdev(nums):
    diffs = 0
    avg = sum(nums) / len(nums)
    for n in nums:
        diffs += (n - avg)**(2)
    return (diffs / (len(nums) - 1)) ** (0.5)


print('vol_stdev: ', stdev(scores))
