#Analize how many musicians, including their genre, are from the United States listed as Best Selling Artists.
#The data source comes from: https://www.kaggle.com/datasets/kabhishm/best-selling-music-artists-of-all-time.

import pandas as pd
import matplotlib

best_selling_artists = pd.read_csv("best_selling_artists.csv")

print(best_selling_artists.head(10))

#Will focus on/keep columns: Artist, Country, Genre.
#Will drop columns: period_active, year, TCU, Sales.
df = best_selling_artists

best_selling_artists = best_selling_artists(df[list][{'period_active','Year','TCU','Sales'}])
if 'period_active' in best_selling_artists and 'Year' in best_selling_artists and 'TCU' in best_selling_artists and 'Sales' in best_selling_artists:
    best_selling_artists.drop(['period_active'],['Year'],['TCU'],['Sales'], axis=1, inplace=True)
else:
    'Artist' in best_selling_artists and 'Country' in best_selling_artists and 'Genre' in best_selling_artists

