import pandas as pd
import re
from collections import defaultdict


df = pd.read_csv("./backend/csv/cosmetics.csv")

# first, drop all rows without ingredient list
rows_to_drop = []
for i, row in df.iterrows():
    if row['Name'] == '#NAME?' or row['Ingredients'] == "#NAME?" or row['Ingredients'].lower() == 'no info' or "visit" in row['Ingredients'].lower():
        rows_to_drop.append(i)
for row in rows_to_drop:
    df.drop(row, inplace=True)

for i, row in df.iterrows():
    # change all 0,0,0,0,0 products to 1,1,1,1,1
    if row['Combination'] == 0 and row['Dry'] == 0 and row['Normal'] == 0 and row['Oily'] == 0 and row['Sensitive'] == 0:
        df.loc[i, 'Combination'] = 1
        df.loc[i, 'Dry'] = 1
        df.loc[i, 'Normal'] = 1
        df.loc[i, 'Oily'] = 1
        df.loc[i, 'Sensitive'] = 1

    ingreds_per_prod = []

    for ingred in row['Ingredients'].split(','):
        ingred = ingred.lower()
        # remove "... {Active Ingredients, May Contain, etc}:"
        if ":" in ingred:
            index = ingred.index(":")
            ingred = ingred[index+len(":"):]

        # remove "Please be aware that ingredient lists may change... up to date list of ingredients."
        if "Please be aware" in ingred:
            ingred = ingred[:ingred.index("please be aware")]

        # remove "x.xx%"
        ingred = re.sub(r'\d+\.\d+%', '', ingred)
        # remove "x%"
        ingred = re.sub(r'\d+%', '', ingred)
        # remove "(CI 12345)""
        ingred = re.sub(r'ci\s*\d+', '', ingred)
        # remove "*" and "." and "()"
        ingred = ingred.replace('*', '')
        ingred = ingred.replace('.', '')
        ingred = ingred.replace('(', '')
        ingred = ingred.replace(')', '')
        # remove trailing whitespace
        ingred = ingred.strip()
        ingreds_per_prod.append(ingred)

    # update ingredients in dataframe
    new_column = pd.Series([",".join(ingreds_per_prod)], name='Ingredients', index=[i])
    df.update(new_column)

df.to_csv("./backend/csv/cosmetics_clean.csv")