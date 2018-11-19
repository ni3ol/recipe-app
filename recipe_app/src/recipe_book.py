# recipe_book = {
#     'Butternut soup': {
#         'ingredients': [{
#             'name': 'butternut',
#             'quantity': '400',
#             'measurement': 'grams'
#         },
#         {
#             'name': 'cream',
#             'quantity': '250',
#             'measurement': 'milligrams'
#         }],
#         'instructions': [
#             'Cut up the butternut into chunks.',
#             'Boil water and add butternut until soft.',
#             'Add coconut milk.'
#         ],
#     }
# }

class RecipeBook(object):
    def __init__(self, recipes={}):
        self.recipes = recipes
            
    def add_recipe_to_recipe_book(self, recipe):
        if recipe['recipe_name'] not in self.recipes:
            self.recipes[recipe['recipe_name']] = {
                'ingredients': recipe['ingredients'],
                'instructions': recipe['instructions']
            }
        
    def view_recipes(self):
        return self.recipes

    def view_recipe(self, name):
        return self.recipes[name]

    def edit_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {
            'ingredients': ingredients,
            'instructions': instructions
        }

    def delete_recipe(self, name):
        self.recipes.pop(name, None)