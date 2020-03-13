import os, requests, validators

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
    #collect all image_url keys from the collections
    imageUrls = mongo.db.recipe.distinct('image_url')
    validUrls = []
    images = []
    
    #iterate through the keys, and check if they have valid urls
    for image in imageUrls:
        valid=validators.url(image)
        if valid==True:
            validUrls.append(image)
            print('Valid Url')
        else:
            print('Invalid url')

    #iterate through the valid urls and check if the status code is 200
    for image in validUrls:
        try:
            request = requests.get(image)
            request.raise_for_status()
            if request.status_code == 200:
                print('status 200!')
                images.append(image)
        except requests.ConnectionError as err:
            print('Image could not load, Error Response: '+ str(err))

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