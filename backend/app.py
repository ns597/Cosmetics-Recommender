import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
from helpers.similarity import top5category

# ROOT_PATH for linking with all your files.
# Feel free to use a config.py or settings.py with a global export variable
os.environ['ROOT_PATH'] = os.path.abspath(os.path.join("..", os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
MYSQL_USER = "root"
MYSQL_USER_PASSWORD = "sydneyho967"
MYSQL_PORT = 3306
MYSQL_DATABASE = "cosmetics"

mysql_engine = MySQLDatabaseHandler(
    MYSQL_USER, MYSQL_USER_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)

# Path to init.sql file. This file can be replaced with your own file for testing on localhost, but do NOT move the init.sql file
mysql_engine.load_file_into_db()

app = Flask(__name__)
CORS(app)

# Sample search, the LIKE operator in this case is hard-coded,
# but if you decide to use SQLAlchemy ORM framework,
# there's a much better and cleaner way to do this


def sql_search(name, skin):
    """
    It takes in a product name and a skin type, and returns a dictionary of the top
    5 products in each category (moisturizer, cleanser, sunscreen, treatment) that
    are most similar to the product name

    :param name: the name of the product you're looking for
    :param skin: the skin type of the user
    :return: A dictionary of lists of dictionaries.
    """
    # query_sql = f"""SELECT * FROM cosmetics WHERE LOWER( title ) LIKE '%%{prod.lower()}%%' limit 10"""
    # mysql_engine.validate_connection()
    query_sql = f"""SELECT Ingredients FROM products WHERE LOWER( Name ) = '%%{name.lower()}%%'"""
    query_ingreds = mysql_engine.query_selector(query_sql)
    print(query_ingreds)

    query_ingreds = query_ingreds.fetchone()

    m_query = f"""SELECT Name, Ingredients FROM products WHERE '%%{skin}%%' = 1 AND Label = 'Moisturizer'"""
    # mysql_engine.validate_connection()
    moisturizers = mysql_engine.query_selector(m_query)
    c_query = f"""SELECT Name, Ingredients FROM products WHERE '%%{skin}%%' = 1 AND Label = 'Cleanser'"""
    # mysql_engine.validate_connection()
    cleansers = mysql_engine.query_selector(c_query)
    s_query = f"""SELECT Name, Ingredients FROM products WHERE '%%{skin}%%' = 1 AND Label = 'Sun protect'"""
    # mysql_engine.validate_connection()
    sunscreens = mysql_engine.query_selector(s_query)
    t_query = f"""SELECT Name, Ingredients FROM products WHERE '%%{skin}%%' = 1 AND Label = 'Treatment'"""
    # mysql_engine.validate_connection()
    treatments = mysql_engine.query_selector(t_query)

    routine = {}
    routine["Moisturizer"] = top5category(moisturizers, query_ingreds)
    routine["Cleanser"] = top5category(cleansers, query_ingreds)
    routine["Sunscreen"] = top5category(sunscreens, query_ingreds)
    routine["Treatment"] = top5category(treatments, query_ingreds)
    print("routine", routine)

    # keys = ["Name", "Ingredients"]
    # return json.dumps([dict(zip(keys, i)) for i in moisturizers])

    return json.dumps(routine)


@app.route("/")
def home():
    return render_template('base.html', title="sample html")


@app.route("/product")
def product_search():
    skin_type = request.args.get("skin")
    product_name = request.args.get("name")
    # print(request.args.get("skin_type"))
    # print(request.args.get("product_name"))
    return sql_search("Glam Purifying Moisturizer", "Dry")
    # return render_template('base.html', title="sample html", context={'json': json_info})


app.run(debug=True)
