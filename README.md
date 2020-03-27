# SeeFood!

SeeFood is a website where people can store and share their favorite recipes. 
Here you can create your own recipes to share with others, find and locate new recipes, perhaps get some new inspiration
for tonights dinner. Create a user to handle your own recipes while enjoying the shared space with others!


## UX

### User Stories
* As a user, I want to search for a particular recipe to cook for my next meal.
* As a user, I want to locate my favorite recipes by keywords.
* As a user, I want to browse different recipes from different categories to find inspiration.
* As a user, I wish to store my own recipes in one location.
* As a user, I wish to share my favorite food with others. 
* As a user, I want to update my current recipes stored on the site. 
* As a user, I want to be able to remove my recipes if I don't want them published anymore.

#### Strategy/Scope
The main goal for this site is to allow the users to share and store their favorite food with others. How often do 
you make a great dinner on the fly and want to document what you have done and perhaps share it with others? Or maybe 
looking for ideas when you are stuck in a rutine of cooking the same meals week over week? The simplicity and availability 
of this app should make these thing easy to overcome. 
By using a clean and simple design, the user should find it easy to use, and wish to come back to browse and 
store even more of their recipes. 

#### Structure
* On the landing page, I want to quickly and efficiently describe what the website provides, and encourage
the user to sign up to the site. By using 
background images and a carousel at the bottom displaying food and some of the recipes that are available.
* The browse page should display the images with cards, the image of the recipe and some key information.
It should also have a search function.
* When a user is logged in they should be able to add a recipe, update their own and delete them. This is handled
using a form to fill in which is very similar between creating a recipe and updating one.
* The recipe itself is a page where all the information about how to cook the meal is displayed, 
with an image of the food as well, presented to the user.

#### Skeleton 

Wireframes made with Balsamiq:  

[Home Page, Desktop and Mobile view](https://github.com/HeimirDavid/recipe-application/blob/master/static/images/wireframes_ERD/index.png)  

[Recipe Page, Desktop and Mobile view](https://github.com/HeimirDavid/recipe-application/blob/master/static/images/wireframes_ERD/recipe.png)  

[Browse Recipes, Desktop and Mobile view](https://github.com/HeimirDavid/recipe-application/blob/master/static/images/wireframes_ERD/recipes.png)  

[Add Recipe Page, Desktop view](https://github.com/HeimirDavid/recipe-application/blob/master/static/images/wireframes_ERD/add_recipe.png)  

Entity Relationship Diagram made with lucidchart:

[ERD](https://github.com/HeimirDavid/recipe-application/blob/master/static/images/wireframes_ERD/seeFood-ERD.png)  
 

#### Surface
As a colour pallet I wanted to use bright colours, to match with the theme of bright images of food.
Since this is a cook book written by the users, i wanted the typography to be a bit handwritten to make it feel
more personal.

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Existing Features
* **Register** - Allows a user to create an account by filling out a form with their wished username and password.
* **Login** - By filling out a form with their username and password a user can use the full features of the site.
* **Browse Recipes** - Allows a user to look around and see what other people are sharing to the site.
* **Search Recipes** - A search function on the browse page allows a user to look up a recipe, 
or author by filling out the search field with a keyword and search for it.
* **Add Recipe** - Allows a logged in user to add a recipe to the site by filling out a form which ask for specific
information about the recipe. After form is filled out, just press the button "Add Recipe" and it's done.
* **Edit Recipe** - Allows a logged in user to edit/update their own recipes. As you have the recipe open, an "Edit"
button is displayed to the user. As it is pressed the recipe wished to update will have the same information filled out 
in the forms fields, but are availible to edit to what the user wish.
* **Delete Recipe** - Allows a logged in user to remove their own recipes by clicking the "Delete" button when they have
the wished recipe open. 

Feature 1 - allows users X to achieve Y, by having them fill out Z
...
For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
* **Save Recipes** - I wish to add the functionality to allow a user to store their favorite recipes in their own 
collection. Here you could store your favorite recipes and only view those. This would be their personal cookbook.
* **Hide Recipes** - I wish to make it availible for the logged in user to upload a recipe, store it in their saved 
recipe collection mentioned above, but not have it visible to the public.
* **Better Image Storage**: Right now the images are from a URL provided by the user. It would be more user friendly
to allow a user to upload an image file, maybye straight from their phone as not everyone have an uploaded image with 
an URL to provide.

### Technologies Used
**Main Languages Used**: HTML, CSS, Python and JavaScript
**Frameworks and Libraries**:
* **Flask 1.1.1** - link: https://palletsprojects.com/p/flask/  
* **PyMongo 3.10.1** - To work with the MongoDB database from python. 
  link: https://docs.mongodb.com/ecosystem/drivers/pymongo/  
* **flask-bcrypt 0.7.1** - Used to encrypt the passwords on the site.  
  link: https://flask-bcrypt.readthedocs.io/en/latest/  
* **glide.js** - Used for the carousel displaying the images on the home page.  
  link: https://glidejs.com/  
* **Materialize** - Used for it's grid system, forms, buttons and some general styles.  
  link: https://materializecss.com/  
* **JQuery** - Mainly used to simplify DOM manipulation.
* **Version Control and deployment** - Git was used for version control and Heroku to deploy the project.  
* **Balsamiq** - Used for wireframes.  
  link: https://balsamiq.com/  


## Testing
* **HTML** was tested using **validator W3C**. Warnings came up with "Bad Value" for all jinja code, which was ecpected and ignored.
One more warning was for two elements with the same ID, but since they are in a if else statement they also were ignored.
* **CSS** was tested using **Jigsaw**. One warning came up with text-color-decoration: none being invalid value which has been fixed.
* **JavaScript** was tested using **JSHint**. No severe warning or errors, just a few missing semicolons which has been fixed.

### Responsiveness
This site has been developed using Gitpod in Google Chrome and therefor it's responsiveness has mainly been tested using
Chrome Developer Tools. The responsiveness works fine on desktop computer and has been tested using both Chrome, 
Microsoft Edge and Safari.
It has also been tested on tablets, both IOS and Android, with Safari and Google Chrome. With google chrome it works
as intended but with **safari** there have been a **few issues** with the Browse recipes page.
 It was rendered as mobile view but after ading a breakpoint between mobile and tablet view it looks better.
The site has also been tested on a few different mobile devices on Chrome, Samsung Internet and Safari and works fine. 

### User Interaction
***All of these interactions have been manually tested:***
* **Home Page** - All buttons on the Home page brings a user to the correct places. Including the footers contact section that links to correct contact websites.
* **Main Navigation** - All the buttons bring a user to the correct  pages.
* **Add Recipe** - All the fields are possible to fill out. The required ones are blocking the user to continue if they
are not filled in, and to submit the recipe with the correct value and value types to the database works.
* **Update Recipe** - All the fields are prefilled with the correct data from the chosen recipe, and are able to edit
and submit. Then the user is redirected to the updated version of the recipe and works fine.
* **Register** - A user can register by filling out a username and password and confirming the password.
If a username already exists, the user is notified about this. Same goes if the passwords don't match.
As a user manage to register, they are logged in and a welcome message is displayed.
* **Login** - A user can log in if they have a registered account. This by simply filling out their username and password.
If the username or password is incorrect, this is displayed with a message to the user. When they log in they are notified 
by a welcome message. 
* **Logged in functionality** - Add a recipe is only available to logged in users and when you log in it will be 
availible to you in the main navigation. as you log out the button disapears.
* **User personal functionality** - A user is only able to delete or update a recipe they have created themself.


## Deployment
This project was deployed to the hosting platform **Heroku**.  
***The steps I took where:***
1. When logged in to the heroku platform, I created a new app called "seefood-application" and set it's region to Europe.
2. I logged in to Heroku in the Terminal window on Gitpod using `Heroku login` command.
3. Linked my Git repository (already existed) to heroku. 
This done by first copy the Heroku Git URL from this application settings page.
Then back to the terminal window on Gitpod, I typed in `git remote add heroku https://git.heroku.com/seefood-application.git`
4. Created a requirements.txt file through the terminal: `pip3 freeze > requirements.txt`
5. Created a Procfile to let heroku know how to run the program.
This done by typing the following command into the terminal window: `echo web: python app.py > Procfile`
6. I commited these changes and pushing it using these commands `git push heroku -u master`

### Environment Variables
1. After logging in to heroku dashboard I selected the application.
2. I located the settings and pressed Reveal Config Vars.
3. Set the IP to 0.0.0.0
4. set the PORT to 5000
5. Add the MONGODB_NAME variable and set its value to the database name.
6. Add the MONGO_URI variable and set its value.
7. Add the SECRET_KEY variable and set it's value.

## Local Deployment

***Control that you have following intalled on you computer (Windows):***
1. Latest version on Python.
2. Git.
3. Working IDE, preferably Visual Studio Code for these steps to work.
4. Visual studio extension for python. Named Python from Microsoft.

#### Clone The repository
1. Go to https://github.com/HeimirDavid/recipe-application
2. Press the button "Clone or Download" to the right.
3. Press "Use HTTPS" and copy the URL from the text field.
4. Create a folder for your workspace in Visual Studio Code.
5. Open a terminal window and navigate to the directory you wish to put this project.
6. type `git clone ` followed by the copied URL.

#### Set up the workspace
1. Open a terminal window from your computer.
2. Locate the workspace directory.
3. Create a viritual environment by typing `py -m venv env` into the command prompt. 
Folder "env" should now be installed in the workspace.
4. Activate the environment by typing `env\Scripts\activate`.
5. Install flask using pip: `pip install flask`.
6. Install the required packages from requirements.txt by typing `pip install -r requirements.txt`.
7. set an environment variable in the command prompt: `set FLASK_APP=app.py`.
8. Make sure to set up the mondoDB environment variables and then type `flask run` in the command prompt.
9. Open the URL provided in your browser and you should see the site up and running.

## Credits
* **The hamburger menu** styling and javascript came from this tutorial:  
https://www.youtube.com/watch?v=dIyVTjJAkLw  
* **The login and register** system was based upon two tutorials, mainly the first one linked below:  
https://www.youtube.com/watch?v=vVx1737auSE  
https://www.youtube.com/watch?v=CSHx6eCkmv0&t=324s  
* **The search functionality** is based upon this tutorial on how to use text index:  
https://www.youtube.com/watch?v=dTN8cBDEG_Q  
* The way to use **flash messages** came from this documentation:  
https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/  
* The Carousel and how to use glide.js comes from this tutorial:  
https://www.youtube.com/watch?v=kpAt25cOBrU  


### Content
Recipe Sources: 
* Thai Green Curry - **recipe:** https://www.bbcgoodfood.com/recipes/vegetarian-thai-green-curry
* Pad Thai With Tofu - **recipe:** https://minimalistbaker.com/easy-tofu-pad-thai/
* Pancakes - **recipe:** https://tasty.co/recipe?0=%2Fthe-fluffiest-vegan-pancakes&slug=the-fluffiest-vegan-pancakes&canonicalUrl=https%3A%2F%2Ftasty.co  
**Picture:** https://unsplash.com/photos/trt7eH46oRA
### Media
* The background image on the home page came from unsplash.   
link: https://unsplash.com/photos/sDbj1dFlFPU  
* Swedish Chocolate Balls image.    
link: https://bakeplaysmile.com/super-easy-super-delicious-rum-balls/  
* Balkan Veggie Soup, image from unsplash.  
link: https://unsplash.com/photos/3hi4Ckm-0v0  
* Advanced Avocado, picture from unsplash.  
link: https://unsplash.com/photos/9aOswReDKPo  

The photos used in this site were obtained from ...
### Acknowledgements
*For this project i recived inpiration from a few different projects:*
* Firstly, the **Task Manager** application that was the mini-project code along from Code Institute.
The CRUD operations where highly influenced by it.
* Secondly, two other projects made by other students who also choose the cookbook suggestion by Code Institute: 
link to the first prject: https://online-cookbook4.herokuapp.com/
link to the second project: https://data-centric-development.herokuapp.com/
* I also want to thank my mentor Moosa Hassan for his guidance and all the people on Code Institutes Slack channel for their help.
