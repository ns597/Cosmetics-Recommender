import pandas as pd
import numpy as np
cosmetics = pd.read_csv('cosmetics.csv')  

#Types of input to initalize
#limit to skin type first, then perform jaccard similarity on three groups 
skin_type_input = input("Input your skin type: ")
prod_name = input("Input the name of product you have used an enjoyed: ")


skin_type = cosmetics[cosmetics[skin_type_input.capitalize()]==1]
product = cosmetics[cosmetics['Name']== prod_name]
ingredients = product['Ingredients']

moisturizers = skin_type[skin_type['Label']=='Moisturizer']
cleansers = skin_type[skin_type['Label']=='Cleanser']
other =skin_type[skin_type['Label']=='Other']

# for step in steps:

print(product )

def jaccard_similarity(ingred, products):
    intersection = set(ingred).intersection(set(products))
    union = set(ingred).union(set(products))
    return len(intersection) / len(union)
