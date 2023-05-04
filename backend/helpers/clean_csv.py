import pandas as pd
import re
from collections import defaultdict


df = pd.read_csv("./backend/csv/cosmetics.csv")

no_ingreds = [
    '*ingredients from organic farming. **clinical grade essential oils blend.',
    'no info',
    '#NAME?'
]

# first, drop all rows without ingredient list
rows_to_drop = []
for i, row in df.iterrows():
    if row['Name'] == '#NAME?' or row['Ingredients'].lower() in no_ingreds or "visit" in row['Ingredients'].lower() or "this ingredient list is subject to change" in row['Ingredients'].lower():
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

    row_clean = row['Ingredients'].replace('Rds Product Name:', ',')

    for ingred in row_clean.split(','):
        ingred = ingred.lower()
        # remove "... {Active Ingredients, May Contain, etc}:"
        if ":" in ingred:
            index = ingred.index(":")
            ingred = ingred[index+len(":"):]

        # remove "Please be aware that ingredient lists may change... up to date list of ingredients."
        if "please be aware" in ingred:
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

        ingred = ingred.replace("el estee lauderactive ingredients: ", "")
        ingred = ingred.replace("el estee lauderingredients: ", "")
        ingred = ingred.replace('cl cliniqueactive ingredient: ', "")

        ingreds_per_prod.append(ingred)

    # update ingredients in dataframe
    new_column = pd.Series([",".join(ingreds_per_prod)], name='Ingredients', index=[i])
    df.update(new_column)

df.to_csv("./backend/csv/cosmetics_clean.csv")