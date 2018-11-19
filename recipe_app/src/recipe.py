class Recipe(object):
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.instructions = []

    def build_ingredient(self, name, quantity, measurement):
        return {
            'name': name,
            'quantity': quantity,
            'measurement': measurement
        }

    def add_ingredient_to_recipe_ingredients(self, ingredient):
        self.ingredients.append(ingredient)

    def add_instruction_to_recipe_instructions(self, instruction):
        self.instructions.append(instruction)

    def build_recipe(self):
        recipe = {'recipe_name': self.name, 'ingredients': self.ingredients, 'instructions': self.instructions}
        return recipe