def top5category(category, ingredients):
    # returns top 5 given a list and ingredients to match
    # go through whole list and get name + ingredient list
    # perform jaccard similarity and put into list of tuples (Name, Score)
    # sort by score and return top 5

    # category = category[['Name', 'Ingredients']]
    # category = category.to_numpy()

    print(category)
    print(ingredients)

    scores = []
    for val in category:
        name = val['name']
        score = jaccard_similarity(val['ingreds'], ingredients)
        scores.append((name, score))
    scores[0]
    scores.sort(key=lambda x: x[1])
    top5 = scores[0]
    # top5 = list(map(lambda x: x[0], top5))
    return top5


def jaccard_similarity(ingred, product):
    a = set(ingred.split(","))
    # print(list(a)[0])
    b = set(product[0].split(","))
    intersection = a.intersection(b)
    union = a.union(b)
    return (len(intersection) / len(union))


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
