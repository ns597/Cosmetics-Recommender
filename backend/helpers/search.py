import pandas as pd
import numpy as np
from collections import defaultdict


def process_csv(filepath):
    # load in data
    df = pd.read_csv(filepath)

    # list of ingredient lists, list of products
    # prod_to_idx maps product names to their index
    ingreds, products, prod_to_idx, prod_to_cat = clean_ingreds_prods(df)
    # print(ingreds)
    # print("INGREDIENT LIST")

    # TODO: fix ingredients list (organize alphabetically)
    alpha_ingreds = set([])
    for key in ingreds:
        # print(key)
        # print(ingreds[key])
        # print(prod_list)
        alpha_ingreds = alpha_ingreds.union(set(ingreds[key]))
    alpha_ingreds = list(alpha_ingreds)
    # print(alpha_ingreds)

    # create inverted index for all ingredients to products they are in
    inv_idx = inverted_index(ingreds)
    # print(inv_idx)
    # prune/remove common ingredients
    # inv_idx = prune_ingreds(inv_idx, len(products))

    # create product - ingredient inverted index for each product category
    categories = df['Label'].unique()
    category_inv_idx = category_inverted_index(
        products, ingreds, categories, prod_to_cat)

    # create unique ingredients list
    ingreds_unique = list(set(np.hstack(ingreds)))
    # print(ingreds_unique)
    ingreds_unique_names = list(map(lambda x: alpha_ingreds[x], ingreds_unique))
    # print(ingreds_unique_names)
    # print(ingreds_unique)
    # print(ingreds)
    ingred_to_idx, idx_to_ingred = ingredients_reverse_index(ingreds_unique)

    # create product - ingredient matrix
    prod_ingred_mat = product_ingredient_mat(products, inv_idx, ingreds_unique_names)

    return df, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, prod_ingred_mat


def clean_ingreds_prods(df):
    ingreds_per_prod = defaultdict(list)
    prod_to_idx = {}
    prod_to_cat = {}
    idx_to_prod = []

    for i, row in df.iterrows():
      prod_name = row['Brand'] + " " + row['Name']
      idx_to_prod.append(prod_name)
      prod_to_idx[prod_name] = i
      prod_to_cat[prod_name] = row['Label']
      for ingred in row['Ingredients'].split(','):
        ingreds_per_prod[i].append(ingred)
    # print(df)
    # print(ingreds_per_prod)
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
    # print(products)
    # print(inverted_index)
    # print(unique_ingreds)
    # print()
    for i, prod_name in enumerate(products):
        for j, ingred in enumerate(unique_ingreds):
            # ingred = unique_ingreds[ingred]
            # print(ingred)
            if i in inverted_index[ingred]:
                product_ingred_mat[i][j] = 1
    # print(np.sum(product_ingred_mat[265]))
    return product_ingred_mat


def get_ingred_vectors(products, liked, prod_to_idx, prod_ingred_mat):
    # returns a list of ingredient vectors for each product
    # liked_ingreds[i][j] is 1 if the i-th liked product contains ingredient j, 0 o/w
    print("Liked: ")
    print(liked)
    liked_ingreds = []
    liked = liked[1:]
    # print(products)
    for product in liked:
        # print(products.index(product))
        product = product.strip()
        if product in prod_to_idx:
            idx = prod_to_idx[product]
            liked_ingreds = liked_ingreds + [prod_ingred_mat[idx]]
        else:
            liked_ingreds =liked_ingreds
    # print("query is ")
    # print(len(liked_ingreds))
    return liked_ingreds


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
