import pandas as pd
import numpy as np
import re
from collections import defaultdict


def process_csv(filepath):
    # load in data
    df = pd.read_csv(filepath)

    # list of ingredient lists, list of products
    # prod_to_idx maps product names to their index
    ingreds, products, prod_to_idx, prod_to_cat = clean_ingreds_prods(df)

    # change all 0,0,0,0,0 products to 1,1,1,1,1
    for i, row in df.iterrows():
        if row['Combination'] == 0 and row['Dry'] == 0 and row['Normal'] == 0 and row['Oily'] == 0 and row['Sensitive'] == 0:
            df.loc[i, 'Combination'] = 1
            df.loc[i, 'Dry'] = 1
            df.loc[i, 'Normal'] = 1
            df.loc[i, 'Oily'] = 1
            df.loc[i, 'Sensitive'] = 1

    # TODO: fix ingredients list (organize alphabetically)

    # create inverted index for all ingredients to products they are in
    inv_idx = inverted_index(ingreds)
    # prune/remove common ingredients
    inv_idx = prune_ingreds(inv_idx, len(products))

    # create product - ingredient inverted index for each product category
    categories = df['Label'].unique()
    category_inv_idx = category_inverted_index(
        products, ingreds, categories, prod_to_cat)

    # create unique ingredients list
    ingreds_unique = list(set(np.hstack(ingreds)))
    ingred_to_idx, idx_to_ingred = ingredients_reverse_index(ingreds_unique)

    # create product - ingredient matrix
    prod_ingred_mat = product_ingredient_mat(products, inv_idx, ingreds_unique)

    return df, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, idx_to_ingred, prod_ingred_mat


def clean_ingreds_prods(df):
    ingreds_per_prod = defaultdict(list)
    prod_to_idx = {}
    prod_to_cat = {}
    idx_to_prod = []

    # first, drop all rows without ingredient list
    rows_to_drop = []
    for i, row in df.iterrows():
        if row['Ingredients'] == "#NAME?" or "visit" in row['Ingredients'].lower():
            rows_to_drop.append(i)
    for row in rows_to_drop:
        df.drop(row, inplace=True)

    for i, row in df.iterrows():
        idx_to_prod.append(row['Name'])
        prod_to_idx[row['Name']] = i
        prod_to_cat[row['Name']] = row['Label']

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

            # update ingredients in dataframe
            new_column = pd.Series([ingred], name='Ingredients', index=[i])
            df.update(new_column)

            ingreds_per_prod[i].append(ingred)
    # print(df)
    print(ingreds_per_prod)
    return ingreds_per_prod, idx_to_prod, prod_to_idx, prod_to_cat


def inverted_index(ingreds):
    """
    Returns a dictionary of each ingredient mapped to a list of
    the products that the ingredient appears in.
    """
    inverted_index = defaultdict(list)

    for prod_idx in ingreds.keys():
        ingred_list = ingreds[prod_idx]
        for ingred in ingred_list:
            if ingred in inverted_index:
                inverted_index[ingred].append(prod_idx)
            else:
                inverted_index[ingred] = [prod_idx]

    return inverted_index


def category_inverted_index(products, ingreds, categories, prod_to_cat):
    """
      Creates a dictionary of inverted indices where the key for each dictionary
      is the product category and each value is the inverted index for all
      products of that category.

      The inverted index is a dictionary of each ingredient mapped to a list of
      the products that the ingredient appears in.

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

    for category in categories:
        inverted_indices[category] = defaultdict(list)

    for i, prod_name in enumerate(products):
        for ingred in ingreds[i]:
            category = prod_to_cat[prod_name]
            if ingred in inverted_indices[category]:
                inverted_indices[category][ingred].append(i)
            else:
                inverted_indices[category][ingred] = [i]

    return inverted_indices


def ingredients_reverse_index(unique_ingreds):
    ingred_to_index = {}
    index_to_ingred = {}

    for i, ingred in enumerate(unique_ingreds):
        ingred_to_index[ingred] = i
        index_to_ingred[i] = ingred

    return ingred_to_index, index_to_ingred


def product_ingredient_mat(products, inverted_index, unique_ingreds):
    product_ingred_mat = np.zeros((len(products), len(unique_ingreds)))

    for i, prod_name in enumerate(products):
        for j, ingred in enumerate(unique_ingreds):
            if i in inverted_index[ingred]:
                product_ingred_mat[i][j] = 1

    return product_ingred_mat


def get_ingred_vectors(ingreds, liked, prod_to_idx, prod_ingred_mat):
    # returns a list of ingredient vectors for each product
    # prod_ingred_mat[i][j] is 1 if product i contains ingredient j, 0 o/w
    prod_ingred_mat = []
    for product in liked:
        idx = prod_to_idx[product]
        ingreds[idx] = prod_ingred_mat[idx]
    return prod_ingred_mat


def ingreds_of_prods(ingreds, liked, prod_to_idx):
    ingred_set = set()
    for product in liked:
        idx = prod_to_idx[product]
        ingred_set.update(ingreds[idx])
    return ingred_set


def prune_ingreds(inv_idx, num_prods, max_ratio=0.90):
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


# def cosine_similarity(query, inverted_index, prod_ingred_mat):
#   # run cosine similarity with query with given ingredients
#   return
