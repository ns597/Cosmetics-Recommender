from helpers.search import *
import numpy as np
import os

# CONSTANTS
# os.chdir('./backend')
# data, inv_idx, category_inv_idx, ingreds, prod_ingred_mat = process_csv("/Users/tanishakore/Desktop/Cosmetics-Recommender/cosmetics_clean.csv")
cur_path = os.path.dirname(__file__)
path = os.path.join(cur_path, '..', 'csv', 'cosmetics_clean.csv')
data, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, prod_ingred_mat = process_csv(
    path)


# print(inv_idx)

def get_matrices():
    return data, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, prod_ingred_mat

def top5update(category, skin_type, query, bad_ingreds, max_price=100, min_price=0, relevant=[], irrelevant=[], skip=[]):
    # category: string indicating which category of products needed
    # max_price: double
    # min_price: double
    # query is a list of vectors from the product ingredient matrix row corresponding to each query
    # relevant: list of vectors from product ingredient matrix of relevant products
    # irrelevant: list of vectors from product ingredient matrix of relevant products
    skips=[]
    for word in skip:
        skips = skips+[word.strip()]
    # print(skip)
    category_prods = category_filter(category)
    skin_prods = skin_type_filter(category_prods, skin_type)
    safe_prods = list(allergen_filter(skin_prods, list(bad_ingreds)))
    price_prods = list(price_filter(safe_prods, max_price, min_price))
    # print(category_prods)
    rel = relevant
    irrel = irrelevant
    try:
        q1 = list(map(lambda x: rocchio(x, prod_ingred_mat, rel, irrel), query))
    except:
        q1 = query
    scores = np.array(cosine_sim(q1, prod_ingred_mat, price_prods))
    # print(scores)
    ranks = np.array(data["Rank"].iloc[price_prods])
    # print(scores)
    # print(scores)
    scores = (0.8*scores) + (0.2*ranks) 
    total_products = []
    # print(price_prods)
    # print(type(price_prods))
    # q = np.where((data==query).all(axis=1))[0][0]
    # print(price_prods)
    # print("INDEXES")
    for i, ind in enumerate(price_prods):
        # print(i)
        # print(ind)
        name = data.at[ind, "Name"]
        score = scores[i]
        # print(scores)
        if np.isnan(scores[i]):
            score = 0.0
        else:
            score = float(scores[i])
        rank = float(ranks[i])
        price = data.at[ind, 'Price']
        price = float(price)
        brand = data.at[ind, 'Brand']
        skin_types = []
        if data.at[i, 'Oily'] == 1: skin_types.append('Oily')
        if data.at[i, 'Dry'] == 1: skin_types.append('Dry')
        if data.at[i, 'Combination'] == 1: skin_types.append('Combination')
        if data.at[i, 'Normal'] == 1: skin_types.append('Normal')
        if data.at[i, 'Sensitive'] == 1: skin_types.append('Sensitive')
        total_products.append((name, score, rank, price, brand, skin_types))
    total_products.sort(key=lambda x: x[1], reverse=True)
    for i in total_products:
        if i[0] in skips:
            total_products.remove(i)
    return total_products[:5]

def cos_sim(a, b):
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0 or np.isnan(norm_a) or np.isnan(norm_b):
            return 0.0
        else:
            return np.dot(a, b) / (norm_a * norm_b)
def cosine_sim(query, matr, products):
    # Expected Inputs:
    # query: vector (List) that matches the product's array from the Ingredient-Product Matrix (Ex: [1,0, .... 1])
    # matr: Ingredient-Product Matrix, matr[i] is the ingredient vector for the ith product in the matrix
    # Output: list of scores where product_scores[i] is the score of products[i]
    product_scores = []
    # def cos_sim(a, b): return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    for i in range(len(products)):
        score = 0
        for j in query: 
            s = cos_sim(matr[i], j)
            score = score+s
        # print(sum(score))
        product_scores.append(score)
    return product_scores


def rocchio(query, matr, rel, irrel, a=0.3, b=0.3, c=0.8):
    # Expected Inputs:
    # query: vector (List) that matches the product's array from the Ingredient-Product Matrix (Ex: [1,0, .... 1])
    # matr: Ingredient-Product Matrix, matr[i] is the ingredient vector for the ith product in the matrix
    # rel : list of vectors, representing ingredients of the products
    # irrel : list of vectors, representing ingredients of the products
    # Expected Output:
    # New query vector representing updated weights on products
    n = len(rel)
    m = len(irrel)
    query = np.array(query)
    dR = np.zeros((1, len(matr[0])))
    dNR = np.zeros((1, len(matr[0])))
    for v in rel:
        dR = np.add(dR, v)
    for v in irrel:
        dNR = np.add(v, dNR)
    # print(type(query))
    # print(type(dR))
    # print(type(dNR))
    # print(type(dNR))
    if n==0 and m==0:
        total = a*query
    elif n==0:
        total = (np.array(query) * a)  - (np.array(dNR) * c * (1/m))
    elif m==0:
        total = (np.array(query) * a) + (np.array(dR) * b * (1/n))  
    else:
        total = (np.array(query) * a) + (np.array(dR) * b * (1/n))  - (np.array(dNR) * c * (1/m))
    # total = query 
    # print(query)
    return np.clip(total, 0, None)


def category_filter(category):
    indices = []
    d = category_inv_idx[category]
    for i in d:
        ind = d[i]
        indices = indices + ind
    return set(indices)


def price_filter(prods, maxp, minp):    
    indices = prods.copy() 
    for i in prods:
        if int(data.at[i, "Price"]) > maxp or int(data.at[i, "Price"]) < minp:
            indices.remove(i) 
    return indices 

def skin_type_filter(prods, skin_type):    
    indices = prods.copy() 
    for i in prods:
        if data.at[i, skin_type]!=1:
            indices.remove(i) 
    return indices 

 
def allergen_filter(prods, bad_ingreds):
    allergens = set(bool_and(bad_ingreds))
    indices = prods.copy() 
    for p in prods: 
        if len(allergens.intersection(set(ingreds[p]))) > 0:
            indices.remove(p)
    # print(indices)
    return indices


def name_to_query(products):
    vectors = []
    for indice in products:
        vectors = vectors + [prod_ingred_mat[indice]]
    return vectors


def jaccard_similarity(ingred, product):
    a = set(ingred.split(","))
    # print(list(a)[0])
    b = product
    intersection = a.intersection(b)
    union = a.union(b)
    return (len(intersection) / len(union))


def levenshtein_distance(s1, s2):
    # Initialize a 2D matrix to store the edit distances
    m = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        m[i][0] = i
    for j in range(len(s2) + 1):
        m[0][j] = j

    # Compute the edit distances
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                m[i][j] = m[i - 1][j - 1]
            else:
                m[i][j] = min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]) + 1

    return m[len(s1)][len(s2)]

def word_similarity_score(product, query):
    score = 0
    q_words = query.split(" ")
    for word in product.split(" "):
        if word in q_words:
            score += 1
    return score

# returns top 5 most similar product names
def word_distance(query):
    distances = [levenshtein_distance(
        name.lower(), query.lower()) for name in products]
    sorted_names = [name for _, name in sorted(zip(distances, products))]
    return sorted_names[:5]


# sourced from the FDA https://www.fda.gov/cosmetics/cosmetic-ingredients/allergens-cosmetics
allergens = ["Latex",
             "Amyl cinnamal",
             "Amylcinnamyl alcohol",
             "Anisyl alcohol",
             "Benzyl alcohol",
             "Benzyl benzoate",
             "Benzyl cinnamate",
             "Benzyl salicylate",
             "Cinnamyl alcohol",
             "Cinnamaldehyde",
             "Citral",
             "Citronellol",
             "Coumarin",
             "Eugenol",
             "Farnesol",
             "Geraniol",
             "Hexyl cinnamaladehyde",
             "Hydroxycitronellal",
             "Hydroxyisohexyl 3-cyclohexene carboxaldehyde",
             "Lyral",
             "Isoeugenol",
             "Lilial",
             "d-Limonene",
             "Linalool",
             "Methyl 2-octynoate",
             "g-Methylionone",
             "Oak moss extract",
             "Tree moss extract",
             "Methylisothiazolinone",
             "Methylchloroisothiazolinone",
             "Formaldehyde",
             "Bronopol",
             "5-bromo-5-nitro-1,3-dioxane",
             "Diazolidinyl urea",
             "DMDM hydantoin",
             "Imidazolidinyl urea",
             "Sodium hydroxymethylglycinate",
             "Quaternium-15",
             "p-phenylenediamine",
             "Coal-tar",
             "Nickel",
             "Gold"]

# takes in list of ingredients, ands with common allergens
# to remove allergic products from recommendations


def bool_and(ingreds):
    result = []
    ingreds_list = list(ingreds)
    i = j = 0
    while i < len(ingreds) and j < len(allergens):
        if ingreds_list[i].lower() == allergens[j].lower():
            result.append(ingreds[i])
            i += 1
            j += 1
        elif i <= j:
            i += 1
        else:
            j += 1
    # print(i)
    return result


#CODE BELOW USED FOR TESTING ONLY
# CATEGORY = "Moisturizer"
# QUERY = [prod_ingred_mat[1], prod_ingred_mat[2], prod_ingred_mat[3]]
# RELEVANT = [prod_ingred_mat[4], prod_ingred_mat[5], prod_ingred_mat[6]]
# IRRELEVANT = [prod_ingred_mat[7], prod_ingred_mat[8], prod_ingred_mat[9]]
# # IRRELEVANT = []
# MAX_PRICE = 250
# MIN_PRICE = 75
# RESULTS = top5update(CATEGORY, QUERY, MAX_PRICE, MIN_PRICE, RELEVANT, IRRELEVANT)
# print(RESULTS)
