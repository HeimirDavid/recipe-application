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

#create new instance of PyMongo
mongo = PyMongo(app)

#Two collection varables, one with only the availible collections for the user (see delete_recipe)
coll = mongo.db.recipe
collStatusOne = coll.find({'status': 1})

#login_btn = Markup('<a>Login/Signup</a>')
#logout_btn = Markup('<a href="/logout">Logout</a>')


@app.route('/')
def index():
    # collect all image_url keys from the collections
    imageUrls = collStatusOne.distinct('image_url')
    validUrls = []
    images = []

    if 'username' in session:
        print(session['username'])
    else:
        print("not logged in")


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

    #Empty list that the valid images will add into, with the rest of the info from it's matching document
    recipes = []
    
    #itterate through the valid images and find it's matching document
    for i in images:    
        imageId = coll.find({'image_url': i})
        for y in imageId:
            recipes.append(y)

    if 'username' in session:
        return render_template('index.html',
                        recipes=recipes) #loginOut_btn=logout_btn)
    else:
        session.pop('username', None)
        return render_template('index.html',
                        recipes=recipes) #, loginOut_btn=login_btn)
 
    

#route to browse recipes, sends along the valid recipes collection to view
@app.route('/view_recipes')
def view_recipes():
    return render_template("recipes.html", recipes=coll.find({'status': 1}))

#route to add recipe
@app.route('/add_recipe')
def add_recipe():
    if 'username' in session:
        user = session['username']
        return render_template('addrecipe.html',
                        recipes=collStatusOne, user=user) #, loginOut_btn=logout_btn)
    else:
        session.pop('username',None)  
        flash("Login/Register to upload a recipe!")
        return redirect(url_for('index'))
    #return render_template('addrecipe.html', recipes=collStatusOne)

#Insert recipe route. 
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    #If the request is POST, assign the data in the form of a dictionary to new_recipe variable.
    #this is to be able to assign the ingredients a list and not string to the document
    #make sure status is 1 so it will be displayed on the page, then insert the dictionary to the collection
    if request.method == 'POST':
        new_recipe = request.form.to_dict()
        ingredientsArray = request.form.getlist('ingredients')
        new_recipe["ingredients"] = ingredientsArray
        new_recipe.update({'status': 1}),
        new_recipe.update({'recipe_author': session['username']})
        coll.insert_one(new_recipe)
        
    return redirect(url_for('view_recipes'))
    #Missing validation on server side. 

#redirect the user to display the recipe they chose by using it's id.
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    if 'username' in session:
        return render_template('recipe.html', #loggedIn=True, think is unneccessary
                        recipe=coll.find_one({'_id': ObjectId(recipe_id)})) #, loginOut_btn=logout_btn)
    else:
        session.pop('username',None)  
        flash("Login/Register to upload a recipe!")
        return render_template('recipe.html',loggedIn=False,
                    recipe=coll.find_one({'_id': ObjectId(recipe_id)})) #, loginOut_btn=login_btn)
    #return render_template('recipe.html', recipe=coll.find_one({'_id': ObjectId(recipe_id)}))


#redirect user to edit page, use the recipes id and send along it's document
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    chosen_recipe = coll.find_one({'_id': ObjectId(recipe_id)})
    return render_template('updaterecipe.html',
                            cr=chosen_recipe)

#Locate the recipe using id, get the data from the form, and update it
#with the new data from the user. redirect to the updated recipe so the 
#user can see his/hers changes.
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
        'category': request.form.get('category'),
        'ingredients': request.form.getlist('ingredients'),
        'instructions': request.form.get('instructions'),
        'summary': request.form.get('summary'),
        'action':request.form.get('action'),
        'status': 1
    })
    return redirect(url_for('recipe', recipe_id=recipe_id))

#Delete function does not delete the recipe from the database but changes
#it's status to 2. Anything but a 1 will end up not displayed on the site.
@app.route('/delete_recipe/<recipe_id>', methods=["POST"])
def delete_recipe(recipe_id):
    if request.method == 'POST':
        #The way of updating the document came from this source:
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

#main info on how to use text index and search came from this tutorial:
#https://www.youtube.com/watch?v=dTN8cBDEG_Q
#The code below has been modified after my needs and so it works with pymongo
@app.route('/recipe_search', methods=["POST"])
def recipe_search():
    if request.method == 'POST':
        #Assign the text from the input from the user to a variable, search
        search = request.form.to_dict().get('icon_prefix')
        result = []
        print(search)
        
        #Create text index
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
        #Search through the collection and find the matches, 
        #assign it to 'searched_coll' and sort it by it's score value
        searched_coll = coll.find(
                                  {'$text': {'$search': search}},
                                  {'score': {'$meta': 'textScore'}}
                                ).sort([('score', {'$meta': 'textScore'})])
    #Iterate through the documents, and assign the ones with a status of 1 to 'result' which is sent to view
    for doc in searched_coll:
        if doc['status'] == 1:
            result.append(doc)

    return render_template('recipesearch.html',
                        recipes=result)



# -----------------------------------------------------------#
# -------            LOGIN SECTION
# -----------------------------------------------------------#

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        login_user = users.find_one({'name': request.form['username']})

        print(login_user)

        if login_user:
            if bcrypt.check_password_hash(login_user['password'], request.form['password']):
                print('It Matches!')
                session['username'] = request.form['username']

                flash("Welcome " + request.form['username'])
                return redirect(url_for('index'))

            #else:
            #    return redirect(url_for('index')) What to doo...
        session.pop('username',None)  
        flash("Incorrect username or password")
        return redirect(url_for('index'))
        



@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['register_name']})
        print(existing_user)

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form['register_password']).decode('utf-8')
            users.insert({'name': request.form['register_name'], 'password': hashpass})
            session['username'] = request.form['register_name']
            
            flash("Welcome " + request.form['register_name'])
            return redirect(url_for('index'))
            #return 'You are now registered and logged in!' #Will have to be changed to the page the user is at

        flash('That username is already taken')
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('username',None)  
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)