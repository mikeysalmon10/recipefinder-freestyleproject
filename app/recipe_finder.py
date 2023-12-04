import requests
from app.edamam import API_KEY,APP_ID


def get_ingredients():
    # Function to get user input for ingredients
    ingredients = input("Enter the ingredients you have (separated by a comma): ")
    return [ingredient.strip() for ingredient in ingredients.split(',')]

def fetch_recipes(ingredients):
    request_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={'%20'.join(ingredients)}&app_id={APP_ID}&app_key={API_KEY}"
    response = requests.get(request_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_recipes(recipes):
    if recipes and "hits" in recipes:
        for recipe in recipes["hits"]:
            print(f"Recipe: {recipe['recipe']['label']}")
            print(f"URL: {recipe['recipe']['url']}\n")
    else:
        print("No recipes found.")

def main():
    ingredients = get_ingredients()
    recipes = fetch_recipes(ingredients)
    display_recipes(recipes)

if __name__ == '__main__':
    main()
