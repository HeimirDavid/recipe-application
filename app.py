import pymongo
import os, requests, validators
#import bcrypt

from flask import Flask, render_template, redirect, request, url_for, session, Markup, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)
bcrypt = Bcrypt(app)

MONGO_URI = os.environ.get("MONGO_URI")
MONGODB_NAME = os.environ.get("MONGODB_NAME")
SECRET_KEY = os.environ.get('SECRET_KEY')

app.config["MONGODB_NAME"] = MONGODB_NAME
app.config["MONGO_URI"] = MONGO_URI
app.config['SECRET_KEY'] = SECRET_KEY

# create new instance of PyMongo
mongo = PyMongo(app)

# Two collection varables, one with only the availible collections for the user (see delete_recipe)
coll = mongo.db.recipe
collStatusOne = coll.find({'status': 1})


@app.route('/')
def index():
    # collect all image_url keys from the collections
    imageUrls = collStatusOne.distinct('image_url')
    # create an empty list which later will store all recipes containing working image url's 
    recipes = []

    # iterate through the keys, and check if they have valid urls
    for image in imageUrls:
        valid = validators.url(image)
        if valid == True:
            try:  # If the URL is valid, try if it gets a 200 status code response
                request = requests.get(image)
                request.raise_for_status()
                if request.status_code == 200:
                    # Match the url's with it's matching document and store it in imageId
                    imageId = coll.find({'image_url': image})

                    # loop through the imageId and store the rows in a list which will be sent to view: recipies
                    for imageColl in imageId:
                        recipes.append(imageColl)
            # error message if the url didn't get a 200 response
            except requests.ConnectionError as err:
                print('Image could not load, Error Response: '+ str(err))

    return render_template('index.html',
                    recipes=recipes)


# route to browse recipes, sends along the valid recipes collection to view
@app.route('/view_recipes')
def view_recipes():
    return render_template("recipes.html", recipes=coll.find({'status': 1}))


# route to add recipe
@app.route('/add_recipe')
def add_recipe():
    # if the user is logged in they get redirected to the addrecipe page,
    # otherwise back to the home page with a flash message
    if 'username' in session:
        user = session['username']
        return render_template('addrecipe.html',
                        recipes=collStatusOne, user=user)
    else:
        session.pop('username',None)  
        flash("Login/Register to upload a recipe!")
        return redirect(url_for('index'))


# Insert recipe route.
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    # If the request is POST, assign the data in the form of a dictionary to new_recipe.
    # this is to be able to assign the ingredients a list and not string to the document.
    # make sure status is 1 so it will be displayed on the page, then insert the dictionary to the collection
    if request.method == 'POST':
        new_recipe = request.form.to_dict()
        ingredientsArray = request.form.getlist('ingredients')
        new_recipe["ingredients"] = ingredientsArray
        new_recipe.update({'status': 1}),
        new_recipe.update({'recipe_author': session['username']})
        coll.insert_one(new_recipe)

    return redirect(url_for('view_recipes'))


# redirect the user to display the recipe they chose by using it's id.
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    return render_template('recipe.html',
                        recipe=coll.find_one({'_id': ObjectId(recipe_id)}))


# redirect user to the edit page, use the recipes id and send along it's document
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    chosen_recipe = coll.find_one({'_id': ObjectId(recipe_id)})
    return render_template('updaterecipe.html',
                            cr=chosen_recipe)


# Locate the recipe using id, get the data from the form, and update it
# with the new data from the user. redirect to the updated recipe so the
# user can see his/hers changes.
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    #if 'username' in session:
    coll.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_author': session['username'],
        'image_url': request.form.get('image_url'),
        'cousine': request.form.get('cousine'),
        'cooking_time': request.form.get('cooking_time'),
        'servings': request.form.get('servings'),
        'category': request.form.get('category'),
        'ingredients': request.form.getlist('ingredients'),
        'instructions': request.form.get('instructions'),
        'summary': request.form.get('summary'),
        'action': request.form.get('action'),
        'status': 1
    })
    return redirect(url_for('recipe', recipe_id=recipe_id))
    #else:
        #flash("You must be logged in to update a recipe")
        #return redirect(url_for('index'))


# Delete function does not delete the recipe from the database but changes
# it's status to 2. Anything but a 1 will end up not displayed on the site.
@app.route('/delete_recipe/<recipe_id>', methods=["POST"])
def delete_recipe(recipe_id):
    if request.method == 'POST':
        # The way of updating the document came from this source:
        # https://kb.objectrocket.com/mongo-db/how-to-update-a-mongodb-document-in-python-356
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

# main info on how to use text index and search came from this tutorial:
# https://www.youtube.com/watch?v=dTN8cBDEG_Q
# The code below has been modified after my needs and so it works with pymongo
@app.route('/recipe_search', methods=["POST"])
def recipe_search():
    if request.method == 'POST':
        # Assign the text from the input from the user to a variable, search
        search = request.form.to_dict().get('icon_prefix')
        result = []
        print(search)

        # Create text index
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
        # Search through the collection and find the matches, 
        # assign it to 'searched_coll' and sort it by it's score value
        searched_coll = coll.find(
                                  {'$text': {'$search': search}},
                                  {'score': {'$meta': 'textScore'}}
                                ).sort([('score', {'$meta': 'textScore'})])
    # Iterate through the documents, and assign the ones with a status of 1 to 'result' which is sent to view
    for doc in searched_coll:
        if doc['status'] == 1:
            result.append(doc)

    return render_template('search.html',
                        recipes=result)



# -----------------------------------------------------------#
# -------            LOGIN SECTION
# -----------------------------------------------------------#

# The login and register function is very similar to the code from this tutorial:
## https://www.youtube.com/watch?v=vVx1737auSE
# it has been slightly modified for my needs, and use a different type of encryption,
# which I found in this tutorial: https://www.youtube.com/watch?v=CSHx6eCkmv0&t=324s

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        # Fetch the username the user typed in 
        login_user = users.find_one({'name': request.form['username']})

        # check if the username exist in the database
        if login_user: 
            # check if the users password match with the hashed one in the database
            if bcrypt.check_password_hash(login_user['password'], request.form['password']):

                # start a session with the username and welcome them back to the site
                session['username'] = request.form['username']
                flash("Welcome " + request.form['username'])
                return redirect(url_for('index'))

        # Let the user know they typed in the wrong password or username
        session.pop('username',None)  
        flash("Incorrect username or password")
        return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        # Fetch the username the user typed in the form
        existing_user = users.find_one({'name': request.form['register_name']})
        print(existing_user)

        # Check if username is availible
        if existing_user is None:
            # If so, check if the password and the confirmed password matches
            if request.form['register_password'] == request.form['re_pass']:
                # Encrypt their password, insert the username and password into the users collection,
                # start their session and redirect back to the home page with a welcome message
                hashpass = bcrypt.generate_password_hash(request.form['register_password']).decode('utf-8')
                users.insert({'name': request.form['register_name'], 'password': hashpass})
                session['username'] = request.form['register_name']
                flash("Welcome " + request.form['register_name'])
                return redirect(url_for('index'))
            else:
                flash("Passwords doesn't match")
                return redirect(url_for('index'))

        flash('That username is already taken')
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)