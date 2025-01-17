#Analize how many musicians, including their genre, are from the United States listed as Best Selling Artists.
#The data source comes from: https://www.kaggle.com/datasets/kabhishm/best-selling-music-artists-of-all-time.

import pandas as pd
import matplotlib

best_selling_artists = pd.read_csv("best_selling_artists.csv")

best_selling_artists.head(10)

#Will focus on/keep columns: Artist, Country, Genre.
#Will drop columns: period_active, year, TCU, Sales.

cols_to_drop = ['period_active','Year','TCU','Sales']

best_selling_artists = best_selling_artists.drop(columns = cols_to_drop)

best_selling_artists.head(10)

#Drop rows, if any, with NaN values
best_selling_artists_cleaned = best_selling_artists.dropna()

#Drop rows with United States in Country
best_selling_artists = best_selling_artists[best_selling_artists['Country'] != 'United States']
best_selling_artists.tail()

#Filter to only United States in Country
best_selling_artists = best_selling_artists[best_selling_artists['Country'] == 'United States']
best_selling_artists.head()

#Identify the column 'Sales'.
#Calculate the total number of sales.
#Calculate the mean number of sales.
#Calculate the median number of sales.
Sales_sum = best_selling_artists['Sales'].sum()
Sales_mean = best_selling_artists['Sales'].mean()
Sales_median = best_selling_artists['Sales'].median()

print(f'The total number of best selling artists is {Sales_sum}./n The mean number of best selling artists is {Sales_mean}./n The median number of best selling artists is {Sales_median}.')


