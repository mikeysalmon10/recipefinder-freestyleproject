# This is the "app/recipes_finder.py" file...

import requests
from app.edamam import API_KEY, APP_ID

def fetch_recipes(ingredients):
    request_url = f"https://api.edamam.com/api/recipes/v2?type=public&q={'%20'.join(ingredients)}&app_id={APP_ID}&app_key={API_KEY}&field=label&field=ingredientLines&field=image&field=url&field=totalNutrients&field=cuisineType&field=mealType"
    response = requests.get(request_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

        
def display_recipe(recipe):
    print("Recipe:", recipe['label'])

    print("Ingredients:", ', '.join(recipe['ingredientLines']))

    if 'cuisineType' in recipe:
        print("Cuisine Type:", ', '.join(recipe['cuisineType']))
    else:
        print("Cuisine Type: Not available")

    if 'mealType' in recipe:
        print("Meal Type:", ', '.join(recipe['mealType']))
    else:
        print("Meal Type: Not available")

    if 'totalNutrients' in recipe:
        print("Nutritional Information:")
        nutrients = recipe['totalNutrients']

        # Extracting energy (calories), fat, carbohydrates, and protein
        energy = nutrients.get('ENERC_KCAL', None)
        fat = nutrients.get('FAT', None)
        carbs = nutrients.get('CHOCDF', None)
        protein = nutrients.get('PROCNT', None)

        # Displaying the energy as calories
        if energy:
            print(f"Calories: {energy['quantity']} {energy['unit']}")
        else:
            print("Calories: Not available")

        # Displaying other macronutrients
        for nutrient, value in {'Fat': fat, 'Carbohydrates': carbs, 'Protein': protein}.items():
            if value:
                print(f"{nutrient}: {value['quantity']} {value['unit']}")
            else:
                print(f"{nutrient}: Not available")
    else:
        print("Nutritional Information: Not available")


def display_instructions(recipe):
    if 'instructions' in recipe:
        print("Instructions:", recipe['instructions'])
    else:
        print("No instructions available for this recipe.")

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
            display_instructions(item["recipe"])
    else:
        print("No recipes found.")
