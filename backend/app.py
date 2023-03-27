import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
from helpers.similarity import top5category

# ROOT_PATH for linking with all your files. 
# Feel free to use a config.py or settings.py with a global export variable
os.environ['ROOT_PATH'] = os.path.abspath(os.path.join("..",os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
MYSQL_USER = "root"
MYSQL_USER_PASSWORD = "admin"
MYSQL_PORT = 3306
MYSQL_DATABASE = "kardashiandb"

mysql_engine = MySQLDatabaseHandler(MYSQL_USER,MYSQL_USER_PASSWORD,MYSQL_PORT,MYSQL_DATABASE)

# Path to init.sql file. This file can be replaced with your own file for testing on localhost, but do NOT move the init.sql file
mysql_engine.load_file_into_db()

app = Flask(__name__)
CORS(app)

# Sample search, the LIKE operator in this case is hard-coded, 
# but if you decide to use SQLAlchemy ORM framework, 
# there's a much better and cleaner way to do this
def sql_search(prod):
    # query_sql = f"""SELECT * FROM cosmetics WHERE LOWER( title ) LIKE '%%{prod.lower()}%%' limit 10"""
    query_sql = f"""SELECT Ingredients FROM cosmetics WHERE LOWER( title ) LIKE '%%{prod.lower()}%%' limit 1"""
    query_ingreds = mysql_engine.query_selector(query_sql)[0]

    m_query = f"""SELECT Name, Ingredients FROM cosmetics WHERE Label = 'Moisturizer'"""
    moisturizers = mysql_engine.query_selector(m_query)
    c_query = f"""SELECT Name, Ingredients FROM cosmetics WHERE Label = 'Cleanser'"""
    cleansers = mysql_engine.query_selector(c_query)
    s_query = f"""SELECT Name, Ingredients FROM cosmetics WHERE Label = 'Sunscreen'"""
    sunscreens = mysql_engine.query_selector(s_query)
    t_query = f"""SELECT Name, Ingredients FROM cosmetics WHERE Label = 'Treatment'"""
    treatments = mysql_engine.query_selector(t_query)

    routine = {}
    routine["Moisturizer"] = top5category(moisturizers, query_ingreds)
    routine["Cleanser"] = top5category(cleansers, query_ingreds)
    routine["Sunscreen"] = top5category(sunscreens, query_ingreds)
    routine["Treatment"] = top5category(treatments, query_ingreds)
    return json.dumps(routine)


@app.route("/")
def home():
    return render_template('base.html',title="sample html")

@app.route("/products")
def episodes_search():
    text = request.args.get("title")
    return sql_search(text)


# app.run(debug=True)