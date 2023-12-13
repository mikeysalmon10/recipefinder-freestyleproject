# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template
from app.recipe_finder import fetch_recipes

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/recipes", methods=["GET", "POST"])
def recipes():
    if request.method == "POST":
        ingredients = request.form.get("ingredients")  # Get ingredients from form
        ingredients_list = ingredients.split(',')  # Split ingredients into a list
        recipes_data = fetch_recipes(ingredients_list)  # Fetch recipes using the API
        return render_template("recipes.html", recipes=recipes_data["hits"])  # Render the recipes template with the data
    else:
        return render_template("home.html")  # Redirect to home if not a POST request
