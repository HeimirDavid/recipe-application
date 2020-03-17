import pymongo
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

coll = mongo.db.recipe
cur = coll.find()


collStatusOne = coll.find({'status': 1})




@app.route('/')
def index():
    # collect all image_url keys from the collections
    imageUrls = collStatusOne.distinct('image_url')
    validUrls = []
    images = []

    # iterate through the keys, and check if they have valid urls
    for image in imageUrls:
        valid=validators.url(image)
        if valid==True:
            validUrls.append(image)
            print('Valid Url')
        else:
            print('Invalid url')
        
    # iterate through the valid urls and check if the status code is 200, store 200 status code urls in images list
    for image in validUrls:
        try:
            request = requests.get(image)
            request.raise_for_status()
            if request.status_code == 200:
                print('status 200!')
                images.append(image)
        except requests.ConnectionError as err:
            print('Image could not load, Error Response: '+ str(err))

    recipes = []
    
    for i in images:
        imageId = coll.find({'image_url': i})
        for y in imageId:
            recipes.append(y)
 
    return render_template('index.html',
                        recipes=recipes)


@app.route('/view_recipes')
def view_recipes():
    return render_template("recipes.html", recipes=coll.find({'status': 1}))


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html', recipes=collStatusOne)


@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
    if request.method == 'POST':
        new_recipe = request.form.to_dict()
        ingredientsArray = request.form.getlist('ingredients')
        new_recipe["ingredients"] = ingredientsArray

        new_recipe.update({'status': 1})
        print(type(ingredientsArray))
        print(new_recipe)

        coll.insert_one(new_recipe)
        
    return redirect(url_for('view_recipes'))
    #Missing validation on server side. 


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    return render_template('recipe.html', recipe=coll.find_one({'_id': ObjectId(recipe_id)}))


@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    chosen_recipe = coll.find_one({'_id': ObjectId(recipe_id)})
    return render_template('updaterecipe.html',
                            cr=chosen_recipe)


@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    coll.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_author': request.form.get('recipe_author'),
        'image_url': request.form.get('image_url'),
        'cousine': request.form.get('cousine'),
        'cooking_time': request.form.get('cooking_time'),
        'servings': request.form.get('servings'),
        'ingredients': request.form.getlist('ingredients'),
        'instructions': request.form.get('instructions'),
        'summary': request.form.get('summary'),
        'action':request.form.get('action'),
        'status': 1
    })
    return redirect(url_for('recipe', recipe_id=recipe_id))


@app.route('/delete_recipe/<recipe_id>', methods=["POST"])
def delete_recipe(recipe_id):
    if request.method == 'POST':
        #https://kb.objectrocket.com/mongo-db/how-to-update-a-mongodb-document-in-python-356
        coll.find_one_and_update(
            {'_id': ObjectId(recipe_id)},
            {"$set":
                {'status': 2}
            }, upsert=True
        )
        
    return redirect(url_for('view_recipes'))




# -----------------------------------------------------------#
# -------            SEARCH SECTION
# -----------------------------------------------------------#

@app.route('/recipe_search', methods=["POST"])
def recipe_search():
    if request.method == 'POST':
        search = request.form.to_dict().get('icon_prefix')
        result = []
        print(search)

        coll.create_index([ 
                            ('recipe_name', pymongo.TEXT),
                            ('recipe_author', pymongo.TEXT),
                            ('cousine', pymongo.TEXT),
                            ('cooking_time', pymongo.TEXT),
                            ('servings', pymongo.TEXT),
                            ('ingredients', pymongo.TEXT),
                            ('instructions', pymongo.TEXT),
                            ('summary', pymongo.TEXT)
                        ])

        searched_coll = coll.find(
                                  {'$text': {'$search': search}},
                                  {'$score': {'$meta': 'textScore'}}
                                )

    for doc in searched_coll:
        if doc['status'] == 1:
            result.append(doc)

    print(result)        

    return render_template('recipesearch.html',
                        recipes=result)





if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)