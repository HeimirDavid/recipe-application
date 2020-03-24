#SeeFood!

SeeFood is a website where people can store and share their favorite recipes. 
Here you can create your own recipes to share with others, find and locate new recipes, perhaps get some new inspiration
for tonights dinner. Create a user to handle your own recipes while enjoying the shared space with others!


##UX

###User Stories
* As a user, I want to search for a particular recipe to cook for my next meal.
* As a user, I want to locate my favorite recipes by keywords.
* As a user, I want to browse different recipes from different categories to find inspiration.
* As a user, I wish to store my own recipes in one location.
* As a user, I wish to share my favorite food with others. 
* As a user, I want to update my current recipes stored on the site. 
* As a user, I want to be able to remove my recipes if I don't want them published anymore.

####Strategy/Scope
The main goal for this site is to allow the users to share and store their favorite food with others.
By using a clean and simple design, the user should find it easy to use, and wish to come back to browse and 
store even more of their recipes. 

####Structure
* On the landing page, I want to quickly and efficiently describe what the website provides, and encourage
the user to sign up to the site. By using 
background images and a carousel at the bottom display some of the recipes that are available.
* The browse page should diplay the images with cards, the image of the recipe and some key information.
It should also have a search function.
* When a user is logged in they should be able to add a recipe, update their own and delete them. This is handled
using a form to fill in which is very similar between creating a recipe and updating one.
* The recipe itself is a page where all the information about how to cook the meal is displayed, 
with the image if the food as well presented to the user.

####Skeleton


####Surface
As a colour pallet i wanted to use bright colours, to match with the theme of bright images of food.
Since this is a cook book written by the users, i wanted the typography to be a bit handwritten to make it feel
more personal.

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:

As a user type, I want to perform an action, so that I can achieve a goal.
This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included as a pdf file in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

##Existing Features
* **Register** - Allows a user to create an account by filling out a form with their wished username and password
* **Login** - By filling out a form with their username and password a user can use the full features of the site.
* **Browse recipes** - Allows a user to look around and see what other people are sharing to the site.
* **Search recipes** - A search function on the browse page allows a user to look up a recipe, 
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

###Features Left to Implement
* **Save Recipes** - I wish to add the functionality to allow a user to store their favorite recipes in their own 
collection. Here you could store your favorite recipes and only view those. This would be their personal cookbook
* **Hide Recipes** - I wish to make it availible for the logged in user to upload a recipe, store it in their saved 
recipe collection mentioned above, but not have it visible for the public.
* **Better Image Storage**: Right now the images are from a URL provided by the user. It would be more user friendly
To allow a user to upload an image file, mayble straight from their phone as not everyone have an uploaded image with 
an URL to provide.

###Technologies Used
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



In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.


##Testing
**HTML** was tested using **validator W3C**. Warnings came up with "Bad Value" for all jinja code, which was ecpected and ignored.
One more warning was for two elements with the same ID, but since they are in a if else statement they also were ignored.
 **CSS** was tested using 
 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

Deployment
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.

Credits
Content
The text for section Y was copied from the Wikipedia article Z
Media
The photos used in this site were obtained from ...
Acknowledgements
I received inspiration for this project from X