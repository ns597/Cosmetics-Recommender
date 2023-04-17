def top5category(category, ingredients, min_price, max_price, bad_ingreds):
    scores = []
    # print("items in", val['name'], ":", len(category))
    for val in category:
        name = val['name']
        price = val['price']
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
            print("invalid ranking for product", name)
            scores.append((name, score, 0, val['price'], val['brand']))
    if (len(scores) == 0):
        return [('None found', 0)]
    scores.sort(key=lambda x: x[1], reverse=True)
    top5 = scores[:5]
    # top5 = list(map(lambda x: x[0], top5))
    return top5


def jaccard_similarity(ingred, product):
    a = set(ingred.split(","))
    # print(list(a)[0])
    b = product
    intersection = a.intersection(b)
    union = a.union(b)
    return (len(intersection) / len(union))

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
    i = j = 0
    while i < len(ingreds) and j < len(allergens):
        if ingreds[i] === allergens[j]
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
