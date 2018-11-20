from collections import namedtuple


class Recipe(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.instructions = []

    # TODO: Figure out if this should be static or private
    # If the build_ingredient function is only used by the Recipe class
    # it must be private and start with an underscore _build_igredient()
    @staticmethod
    def create_ingredient(self, name, quantity, measurement):
        Ingredient = namedtuple(
            'Ingredent', ['name', 'quantity', 'measurement']
        )
        ingredient = Ingredient(name, quantity, measurement)
        return ingredient

    def update_recipe_ingredients(self, ingredient):
        self.ingredients.append(ingredient)

    def update_recipe_instructions(self, instruction):
        self.instructions.append(instruction)

    def create_recipe(self):
        Recipe = namedtuple('Recipe', ['name', 'ingredients', 'instructions'])
        recipe = Recipe(self.name, self.ingredients, self.instructions)

        return recipe
