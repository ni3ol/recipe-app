# ## Ingredients

# - I can add ingredients that are in the pantry/fridge.
# - I can remove ingredients that are used in a recipe.
# - I can edit which ingredients are available.
# - Ingredients can belong to a recipe and have a quantity and measurement.
# - I can see what ingredients we have in the pantry/fridge.
# - I can see what ingredients we are missing to make a specific meal.

ingredients = {
    'flour': {'quantity': 1, 'measurement': 'kg'},
    'sugar': {'quantity': 500, 'measurement': 'g'},
    'pasta': {'quantity': 400, 'measurement': 'g'},
    'milk': {'quantity': 1, 'measurement': 'l'},
    'pasta_sauce': {'quantity': 200, 'measurement': 'ml'},
}

def add_ingredient(ingredients, name, quantity, measurement):
    ingredients[name] = {'quantity': quantity, 'measurement': measurement}

def delete_ingredient(ingredients, name):
    ingredients.pop(name, None)

def use_ingredient(name, quantity, measurement):
    # update ingredient and delete if depleted.
    pass

def edit_ingredient(ingredients, name, quantity, measurement):
    ingredients[name] = {'quantity': quantity, 'measurement': measurement}

def get_ingredients(ingredients):
    return ingredients

def get_missing_ingredients(ingredients, recipe_ingredients):
    missing_ingredients = {}
    for ingredient in recipe_ingredients:
        if ingredient not in ingredients:
            missing_ingredients[ingredient] = {
                'quantity': ingredient['quantity'],
                'measurement': ingredient['measurement']
            }
        elif ingredient['quantity'] >= ingredients[ingredient]['quantity']:
            # TODO Add quantity difference to missing_ingredients
            missing_ingredients[ingredient] = {
                'quantity': ingredient['quantity'],
                'measurement': ingredient['measurement']
            }
    return missing_ingredients
