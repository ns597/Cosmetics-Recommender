import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
from helpers.similarity import *
from helpers.search import process_csv, get_ingred_vectors, ingreds_of_prods

# ROOT_PATH for linking with all your files.
# Feel free to use a config.py or settings.py with a global export variable
os.environ['ROOT_PATH'] = os.path.abspath(os.path.join("..", os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
# MYSQL_USER = "root"
# MYSQL_USER_PASSWORD = ""
# MYSQL_PORT = 3306
# MYSQL_DATABASE = "cosmetics"

# mysql_engine = MySQLDatabaseHandler(
#     MYSQL_USER, MYSQL_USER_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)

# Path to init.sql file. This file can be replaced with your own file for testing on localhost, but do NOT move the init.sql file
# mysql_engine.load_file_into_db()

# load csv file
# os.chdir('./backend')
df, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, prod_ingred_mat = get_matrices()
# print(sum(prod_ingred_mat[236]))

app = Flask(__name__)
CORS(app)


def search_results(liked, disliked, skin_type, min_price, max_price, relevant=[], irrelevant=[]):
    # print(np.sum(prod_ingred_mat))
    query = get_ingred_vectors(products, liked, prod_to_idx, prod_ingred_mat)
    print(relevant)
    rel = get_ingred_vectors(products, relevant, prod_to_idx, prod_ingred_mat)
    irrel = get_ingred_vectors(products, irrelevant, prod_to_idx, prod_ingred_mat)
    print(rel)
    # print(query)
    bad_ingreds = ingreds_of_prods(ingreds, disliked, prod_to_idx)
    # print(skin_type)
    skip = rel+irrel
    routine = {}
    routine["Cleanser"] = top5update(
        "Cleanser", skin_type, query, bad_ingreds, max_price, min_price, rel, irrel, skip)
    routine["Treatment"] = top5update(
        "Treatment", skin_type, query, bad_ingreds, max_price, min_price, rel, irrel, skip)
    routine["Moisturizer"] = top5update(
        "Moisturizer", skin_type, query, bad_ingreds, max_price, min_price, rel, irrel, skip)
    routine["Sun protect"] = top5update(
        "Sun protect", skin_type, query, bad_ingreds, max_price, min_price, rel, irrel, skip)

    # print("routine", routine['Cleanser'])
    keys = ["name", "score", "rank", "price", "brand", "skin_types", "label"]
    data = [[result[0], result[1], result[2], result[3], result[4], result[5], key]
            for key in routine for result in routine[key]]

    # print("routine", data)

    return json.dumps([dict(zip(keys, i)) for i in data])

@app.route("/")
def home():
    return render_template('base.html', title="sample html")


@app.route("/search")
def query_search():
    query = request.args.get("name")
    # return sql_product_name_query(name)
    top_5 = word_distance(query)
    return json.dumps(top_5)


@app.route("/products")
def products_search():
    liked = request.args.get("names").split(",")
    disliked = request.args.get("disliked").split(",")
    skin_type = request.args.get("skin")
    min_price = request.args.get("min_price")
    min_price = int(min_price) if min_price.isdigit() else 0
    max_price = request.args.get("max_price")
    max_price = int(max_price) if max_price.isdigit() else 9999999
    # return sql_search(liked, disliked, skin_type, min_price, max_price)
    # print(liked)
    # _,s, r, p, _(search_results(liked, disliked, skin_type, min_price, max_price))
    # v = search_results(liked, disliked, skin_type, min_price, max_price)
    # for i in v:
    #     print(type(i))
    return search_results(liked, disliked, skin_type, min_price, max_price)

@app.route("/regenerate")
def rocchio_search():
    liked = request.args.get("names").split(",")
    disliked = request.args.get("disliked").split(",")
    skin_type = request.args.get("skin")
    min_price = request.args.get("min_price")
    min_price = int(min_price) if min_price.isdigit() else 0
    max_price = request.args.get("max_price")
    max_price = int(max_price) if max_price.isdigit() else 9999999
    relevant = request.args.get("relevant")
    print(relevant)
    irrelevant = request.args.get("irrelevant")
    print(irrelevant)
    return search_results(liked, disliked, skin_type, min_price, max_price, relevant, irrelevant)


# app.run(debug=True)
