import os
import requests

from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

MONGO_URI = os.environ.get("MONGO_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")


app.config["MONGODB_NAME"] = MONGODB_NAME
app.config["MONGO_URI"] = MONGO_URI

#create new instance of PyMongo
mongo = PyMongo(app)

@app.route('/')
def index():
    images = mongo.db.recipe.distinct('image_url')
    #print(*images)
    
    #For loop to iterate through the recipes
    #check image_url if it leeds somewhere (200)
    #if so, store in dictionary, else continue the iteration
    #send ditionary to view, carousel element
    return render_template('index.html', images=images)

@app.route('/view_recipes')
def view_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipe.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', recipes=mongo.db.recipe.find())


@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    recipes = mongo.db.recipe
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('view_recipes'))
    #Missing validation on server side. 




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)