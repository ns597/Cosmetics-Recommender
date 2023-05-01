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
df, ingreds, products, prod_to_idx, prod_to_cat, inv_idx, category_inv_idx, ingred_to_idx, idx_to_ingred, prod_ingred_mat = process_csv(
    "./csv/cosmetics_clean.csv")

app = Flask(__name__)
CORS(app)


def search_results(liked, disliked, skin_type, min_price, max_price):
    query = get_ingred_vectors(ingreds, liked, prod_to_idx, prod_ingred_mat)
    bad_ingreds = ingreds_of_prods(ingreds, disliked, prod_to_idx)

    routine = {}
    routine["Cleanser"] = top5update(
        "Cleanser", query, bad_ingreds, max_price, min_price)
    routine["Treatment"] = top5update(
        "Treatment", query, bad_ingreds, max_price, min_price)
    routine["Face Mask"] = top5update(
        "Face Mask", query, bad_ingreds, max_price, min_price)
    routine["Eye cream"] = top5update(
        "Eye cream", query, bad_ingreds, max_price, min_price)
    routine["Moisturizer"] = top5update(
        "Moisturizer", query, bad_ingreds, max_price, min_price)
    routine["Sunscreen"] = top5update(
        "Sunscreen", query, bad_ingreds, max_price, min_price)

    # print("routine", routine)

    keys = ["name", "score", "rank", "price", "brand", "label"]
    data = [[result[0], result[1], result[2], result[3], result[4], key]
            for key in routine for result in routine[key]]

    return json.dumps([dict(zip(keys, i)) for i in data])


@app.route("/")
def home():
    return render_template('base.html', title="sample html")


@app.route("/search")
def query_search():
    query = request.args.get("name")
    # return sql_product_name_query(name)
    top_5 = word_edit_distance(products, query)
    return json.dumps([prod["Name"] for prod in top_5])


@app.route("/products")
def products_search():
    liked = request.args.get("names").split(",")
    disliked = request.args.get("disliked").split(",")
    skin_type = request.args.get("skin")
    min_price = int(request.args.get("min_price"))
    max_price = int(request.args.get("max_price"))
    # return sql_search(liked, disliked, skin_type, min_price, max_price)
    return search_results(liked, disliked, skin_type, min_price, max_price)


# def sql_product_name_query(name):
#     if (len(name) == 0):
#         return json.dumps([])
#     query_sql = f"""SELECT Name FROM products WHERE LOWER( `Name` ) LIKE '%%{name.lower()}%%' limit 5"""
#     query = mysql_engine.query_selector(query_sql)
#     return json.dumps([prod["Name"] for prod in query])

# # Sample search, the LIKE operator in this case is hard-coded,
# # but if you decide to use SQLAlchemy ORM framework,
# # there's a much better and cleaner way to do this


# def sql_search(names, disliked, skin, min_price, max_price):
#     # query_sql = f"""SELECT Name, Label, Ingredients FROM products WHERE LOWER( Name ) LIKE '%%{episode.lower()}%%' limit 10"""

#     query_ingreds = set()
#     # To do: consider adding weights to ingredients that appear many times?

#     for name in names:
#         query_sql = f"""SELECT Ingredients FROM products WHERE LOWER( `Name` ) LIKE '%%{name.lower()}%%'"""
#         query = mysql_engine.query_selector(query_sql).fetchone()
#         print("ingreds:", query["Ingredients"].split(","))
#         query_ingreds.update(set(query["Ingredients"].split(",")))

#     print("query_ingreds:", query_ingreds)

#     keys = ["name", "ingreds", "rank", "price", "brand"]

#     if (skin == 'Oily'):
#         m_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Oily` = 1 AND `Label` = 'Moisturizer'"""
#         c_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Oily` = 1 AND `Label` = 'Cleanser'"""
#         s_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Oily` = 1 AND `Label` = 'Sun protect'"""
#         t_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Oily` = 1 AND `Label` = 'Treatment'"""
#     elif (skin == 'Dry'):
#         m_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Dry` = 1 AND `Label` = 'Moisturizer'"""
#         c_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Dry` = 1 AND `Label` = 'Cleanser'"""
#         s_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Dry` = 1 AND `Label` = 'Sun protect'"""
#         t_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Dry` = 1 AND `Label` = 'Treatment'"""
#     elif (skin == 'Combination'):
#         m_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Combination` = 1 AND `Label` = 'Moisturizer'"""
#         c_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Combination` = 1 AND `Label` = 'Cleanser'"""
#         s_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Combination` = 1 AND `Label` = 'Sun protect'"""
#         t_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Combination` = 1 AND `Label` = 'Treatment'"""
#     elif (skin == 'Normal'):
#         m_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Normal` = 1 AND `Label` = 'Moisturizer'"""
#         c_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Normal` = 1 AND `Label` = 'Cleanser'"""
#         s_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Normal` = 1 AND `Label` = 'Sun protect'"""
#         t_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Normal` = 1 AND `Label` = 'Treatment'"""
#     elif (skin == 'Sensitive'):
#         m_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Sensitive` = 1 AND `Label` = 'Moisturizer'"""
#         c_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Sensitive` = 1 AND `Label` = 'Cleanser'"""
#         s_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Sensitive` = 1 AND `Label` = 'Sun protect'"""
#         t_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Sensitive` = 1 AND `Label` = 'Treatment'"""
#     else:
#         m_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Label` = 'Moisturizer'"""
#         c_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Label` = 'Cleanser'"""
#         s_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Label` = 'Sun protect'"""
#         t_query = f"""SELECT `Name`, `Ingredients`, `Rank`, `Price`, `Brand` FROM `products` WHERE `Label` = 'Treatment'"""

#     moisturizers = [dict(zip(keys, i))
#                     for i in mysql_engine.query_selector(m_query)]
#     cleansers = [dict(zip(keys, i))
#                  for i in mysql_engine.query_selector(c_query)]
#     sunscreens = [dict(zip(keys, i))
#                   for i in mysql_engine.query_selector(s_query)]
#     treatments = [dict(zip(keys, i))
#                   for i in mysql_engine.query_selector(t_query)]

#     # print(moisturizers)

#     bad_ingreds = bool_and(query_ingreds)

#     routine = {}
#     routine["Moisturizer"] = top5category(
#         moisturizers, query_ingreds, min_price, max_price, bad_ingreds)
#     routine["Cleanser"] = top5category(
#         cleansers, query_ingreds, min_price, max_price, bad_ingreds)
#     routine["Sunscreen"] = top5category(
#         sunscreens, query_ingreds, min_price, max_price, bad_ingreds)
#     routine["Treatment"] = top5category(
#         treatments, query_ingreds, min_price, max_price, bad_ingreds)
#     # print("routine", routine)

#     # return json.dumps([dict(zip(keys, i)) for i in moisturizers])

#     # return json.dumps(routine)

#     keys = ["name", "score", "rank", "price", "brand", "label"]
#     data = [[result[0], result[1], result[2], result[3], result[4], key]
#             for key in routine for result in routine[key]]
#     # data = [routine["Moisturizer"], routine["Cleanser"], routine["Sunscreen"], routine["Treatment"]]

#     return json.dumps([dict(zip(keys, i)) for i in data])


app.run(debug=True)
