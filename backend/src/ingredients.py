# ## Ingredients

# - I can add ingredients that are in the pantry/fridge.
# - I can remove ingredients that are used in a recipe.
# - I can edit which ingredients are available.
# - Ingredients can belong to a recipe and have a quantity and measurement.
# - I can see what ingredients we have in the pantry/fridge.
# - I can see what ingredients we are missing to make a specific meal.

ingredients = [
    {'name': 'flour', 'quantity': 1, 'measurement': 'kg'},
    {'name': 'sugar', 'quantity': 500, 'measurement': 'g'},
    {'name': 'pasta', 'quantity': 400, 'measurement': 'g'},
    {'name': 'milk', 'quantity': 1, 'measurement': 'l'},
    {'name': 'pasta_sauce', 'quantity': 200, 'measurement': 'ml'},
]


def add_ingredient(ingredients, name, quantity, measurement):
    ingredient = {
        'name': name,
        'quantity': quantity,
        'measurement': measurement
    }
    ingredients.append(ingredient)


def use_ingredient(name, quantity, measurement):
    # update ingredient and delete if depleted.
    pass


def edit_ingredient(ingredients, name, quantity, measurement):
    pass


def get_ingredients(ingredients):
    return ingredients


def get_missing_ingredients(ingredients, recipe_ingredients):
    pass
