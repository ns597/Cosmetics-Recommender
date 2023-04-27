import pandas as pd
import numpy as np
from collections import defaultdict

def process_csv(file):
  # load in data
  df = pd.read_csv(file)

  # change all 0,0,0,0,0 products to 1,1,1,1,1
  for i, row in df.iterrows():
    if row['Combination'] == 0 and row['Dry'] == 0 and row['Normal'] == 0 and row['Oily'] == 0 and row['Sensitive'] == 0:
      df.loc[i, 'Combination'] = 1
      df.loc[i, 'Dry'] = 1
      df.loc[i, 'Normal'] = 1
      df.loc[i, 'Oily'] = 1
      df.loc[i, 'Sensitive'] = 1


  # TODO: fix ingredients list (organize alphabetically)

  # create inverted index for all products
  inv_idx = inverted_index(df)

  # create product - ingredient inverted index for each product category
  category_inv_idx = category_inverted_index(df)
  
  # create unique ingredients list
  ingreds = ingredients_list(df)

  # create product - ingredient matrix     
  prod_ingred_mat = product_ingredient_mat(df, inv_idx, ingreds)

  return df, inv_idx, category_inv_idx, ingreds, prod_ingred_mat

def inverted_index(df):
  inverted_index = defaultdict(list)

  for i, row in df.iterrows():
    for ingred in row['Ingredients'].split(','):
      inverted_index[ingred].append(i)

  return inverted_index

def category_inverted_index(df):
  """
    Creates a dictionary of inverted indices where the key for each dictionary
    is the product category and each value is the inverted index for all
    products of that category

    Example:
    ```
    inverted_indices = {
      'Moisturizers': 
        {'water': [1,2,3]}
      'Cleansers':
        {'water': [7,8,9]}
      ...                      
    }
    ``` 
  """
  inverted_indices = {}
  
  for category in df['Label'].unique():
    inverted_indices[category] = defaultdict(list)

  for i, row in df.iterrows():
    for ingred in row['Ingredients'].split(','):
      inverted_indices[row['Label']][ingred].append(i)

  return inverted_indices

def ingredients_list(df):
  ingreds = set()

  for i, row in df.iterrows():
    ingredients = row['Ingredients'].split(',')
    ingreds.update(ingredients)
  
  return ingreds

def ingredients_reverse_index(ingreds):
  ingred_to_index = {}
  index_to_ingred = {}
  
  for i, ingred in enumerate(ingreds):
    ingred_to_index[ingred] = i
    index_to_ingred[i] = ingred
  
  return ingred_to_index, index_to_ingred

def product_ingredient_mat(df, inverted_index, ingreds):
  product_ingred_mat = np.zeros((len(df), len(ingreds)))

  for i in df.index:
    for j, ingred in enumerate(ingreds):
      if i in inverted_index[ingred]:
        product_ingred_mat[i][j] = 1
  
  return product_ingred_mat

def liked_ingreds(df, liked):
  ingreds = set()
  
  for product in liked:
    row = df[df['Name'] == product]
    ingreds.update(row['Ingredients'].split(','))

  return ingreds

def prune_ingreds(inv_idx, num_prods, max_ratio = 0.90):
  """
    Removes ingredients that occur in more than 90% of products and returns a 
    new inverted index without these ingredients
  """
  
  pruned_inv_idx = defaultdict(list)

  for ingred, prods in inv_idx.items():
    ratio = len(inv_idx[ingred]) / num_prods
    if ratio < max_ratio:
      pruned_inv_idx[ingred] = prods
  
  return pruned_inv_idx


def cosine_similarity(query, inverted_index, prod_ingred_mat):
  # run cosine similarity with query with given ingredients
  return 




