# This is the "app/recipes_finder.py" file...

import requests
from app.edamam import API_KEY, APP_ID

def fetch_recipes(ingredients):
    # Make sure to request all the necessary fields from the API
    request_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={'%20'.join(ingredients)}&app_id={APP_ID}&app_key={API_KEY}&field=label&field=ingredientLines&field=image&field=url"
    response = requests.get(request_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
        
def display_recipe(recipe):
    print("Recipe:", recipe['label'])
    print("Calories:", recipe['calories'])
    print("Ingredients:", ', '.join(recipe['ingredientLines']))

if __name__ == "__main__":
    print("RECIPE FINDER...")

    ingredients = input("Enter the ingredients you have (separated by a comma): ").split(',')
    ingredients = [ingredient.strip() for ingredient in ingredients]
    print("Ingredients:", ', '.join(ingredients))

    recipes_data = fetch_recipes(ingredients)

    if recipes_data and "hits" in recipes_data:
        for i, item in enumerate(recipes_data["hits"], start=1):
            print("\nRecipe", i)
            display_recipe(item["recipe"])
    else:
        print("No recipes found.")
