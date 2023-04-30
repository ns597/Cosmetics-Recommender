# import search
import numpy as np

# TODO: delete? no longer used
def top5category(category, ingredients, min_price, max_price, bad_ingreds):
    scores = []
    # print("items in", val['name'], ":", len(category))
    for val in category:
        name = val['name']
        price = val['price']
        if len(set(bad_ingreds).intersection(set(val['ingreds'].split(",")))) > 0:
            continue     
        name = val['name']
        price = val['price']
        if len(set(bad_ingreds).intersection(set(val['ingreds'].split(",")))) > 0:
            continue
        score = jaccard_similarity(val['ingreds'], ingredients)
        try:
            rank = float(val['rank'])
            # print(rank)
            price_weight = 0
            if price >= min_price and price <= max_price:
                price_weight = 1
            score = (0.8 * score) + (0.2 * rank) + price_weight
            scores.append((name, score, rank, val['price'], val['brand']))
        except:
            print("invalid rank/rating for product", name)
            scores.append((name, score, 0, val['price'], val['brand']))
    if (len(scores) == 0):
        return [('None found', 0)]
    scores.sort(key=lambda x: x[1], reverse=True)
    top5 = scores[:5]
    # top5 = list(map(lambda x: x[0], top5))
    return top5

from search import *
#CONSTANTS
# data, inv_idx, category_inv_idx, ingreds, prod_ingred_mat = process_csv("/Users/tanishakore/Desktop/Cosmetics-Recommender/cosmetics_clean.csv")
data, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, idx_to_ingred, prod_ingred_mat = process_csv("./csv/cosmetics_clean.csv")

# print(inv_idx)
def top5update(category, query, max_price, min_price, relevant=[], irrelevant=[]):
    #category: string indicating which category of products needed
    #max_price: double
    #min_price: double
    #query is the product ingredient matrix row corresponding to the query
    #relevant: list of indices within product ingredient matrix of relevant products
    #irrelevant: list of indices within product ingredient matrix of relevant products
    category_prods = category_filter(category)
    price_prods = list(price_filter(category_prods, max_price, min_price))
    # if relevant != [] or irrelevant!=[]:
    rel = index_to_query(relevant)
    irrel = index_to_query(irrelevant)
    q1 = rocchio(query, prod_ingred_mat, rel, irrel)
    scores = np.array(cosine_sim(q1, prod_ingred_mat, price_prods))
    ranks = np.array(data["Rank"].iloc[price_prods])
    scores = (0.8*scores) * (0.2*ranks)
    total_products= []
    print(price_prods)
    print(type(price_prods))
    for i,ind in enumerate(price_prods):
        name = data.at[ind, 'Name']
        score = scores[i]
        rank = ranks[i]
        price = data.at[ind, 'Price']
        brand = data.at[ind, 'Brand']
        total_products.append((name,score, rank,price,brand))
    total_products.sort(key=lambda x: x[1], reverse=True)
    return total_products[:5]

def cosine_sim(query, matr, products):
    #Expected Inputs:
    # query: vector (List) that matches the product's array from the Ingredient-Product Matrix (Ex: [1,0, .... 1])
    # matr: Ingredient-Product Matrix, matr[i] is the ingredient vector for the ith product in the matrix
    #Output: list of scores where product_scores[i] is the score of products[i]
    product_scores = []
    cos_sim = lambda a,b: np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b)) 
    for i in range(len(products)):
        score = cos_sim(matr[i], query) 
        product_scores.append(score)
    return product_scores


def category_filter(category):
    #returns set of indices in corresponding category
    indices = []
    d = category_inv_idx[category]
    for i in d:
        ind = d[i]
        indices = indices + ind
    return set(indices)

def price_filter(cat, maxp, minp):
    #returns set of indices in corresponding price range
    indices = cat.copy()
    for i in cat:
        if data["Price"][i]>maxp or data["Price"][i]<minp:
            indices.remove(i)
    return indices

def index_to_query(products):
    #converts list of indexes to list of vectors fro product ingredient matrix
    vectors = []
    for indice in products:
        vectors = vectors + [prod_ingred_mat[indice]]
    return vectors


def rocchio(query , matr, rel, irrel, a = 0.3,b = 0.3,c = 0.8):
    #Expected Inputs:
    # query: vector (List) that matches the product's array from the Ingredient-Product Matrix (Ex: [1,0, .... 1])
    # matr: Ingredient-Product Matrix, matr[i] is the ingredient vector for the ith product in the matrix
    # rel : list of vectors, representing ingredients of the products 
    # irrel : list of vectors, representing ingredients of the products 
    # Expected Output:
    # New query vector representing updated weights on products
    n = len(rel)
    m = len(irrel)
    query = np.array(query)
    dR = np.zeros((1,len(matr[0]) ))
    dNR= np.zeros((1,len(matr[0]) ))
    for v in rel:
        dR = np.add(dR, v)
    for v in irrel:
        dNR = np.add(v, dNR)
    # print(type(query))
    # print(type(dR))
    # print(type(dNR))
    total = (query * a) + (dR * b * (1/n)) - (dNR * c * (1/m))
    return np.clip(total,0, None)[0]



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

# returns top 5 most similar product names
def word_edit_distance(query):
    distances = [levenshtein_distance(name.lower(), query.lower()) for name in products]
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
    ingreds_list =  list(ingreds)
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
    return result


# cosmetics = pd.read_csv('cosmetics.csv')
# # print(cosmetics)

# #Types of input to initalize
# #limit to skin type first, then perform jaccard similarity on three groups
# skin_type_input = input("Input your skin type: ")
# prod_name = input("Input the name of product you have used an enjoyed: ")

# skin_type = cosmetics[cosmetics[skin_type_input.capitalize()]==1]
# product = cosmetics[cosmetics['Name']== prod_name]

# moisturizers = skin_type[skin_type['Label']=='Moisturizer']
# cleansers = skin_type[skin_type['Label']=='Cleanser']
# sunscreen =skin_type[skin_type['Label']=='Sun protect']
# treatment = skin_type[skin_type['Label']=='Treatment']

# first = moisturizers['Ingredients'][0]

# print("Moisturizers")
# top5category(moisturizers, product["Ingredients"])
# print("Cleansers")
# top5category(cleansers, product["Ingredients"])
# print("Sunscreen")
# top5category(sunscreen, product["Ingredients"])
# print("Treatment")
# top5category(treatment, product["Ingredients"])
