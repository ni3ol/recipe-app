# ## Recipes

# - I can create recipes that have names and ingredients of a certain quanitity and measurement.
# - I can see an index view where the names of all the recipes are visible.
# - I can click into any of those recipes to view it.
# - I can edit these recipes.
# - I can delete these recipes.

# ingredients : [{
#     name:
#     quanitity:
#     measurement:
# }]

recipe_book = {
    'Butternut soup': {
        'ingredients': {
            'butternut': {
                'quanitity': 200,
                'measurement': 'g'
            },
            'coconut_milk': {
                'quantity': 330,
                'measurement': 'ml'
            }
        },
        'instructions': [
            'Cut up the butternut into chunks.',
            'Boil water and add butternut until soft',
            'Add coconut milk'
        ]
    }
}

class RecipeBook(object):
    def __init__(self, recipes={}):
        self.recipes = recipes
            
    def create_recipe(self, name, ingredients, instructions):
        pass
        
    def view_recipes(self):
        return self.recipes

    def view_recipe(self, name):
        return self.recipes[name]

    def edit_recipe(self, name, ingredients):
        self.recipes[name] = ingredients

    def delete_recipe(self, name):
        self.recipes.pop(name, None)