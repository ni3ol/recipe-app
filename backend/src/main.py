from recipe_book import RecipeBook
from recipe import Recipe


# TODO: Use Click
def main():
    recipe_name = input('Recipe Name: ')
    recipe = Recipe(name=recipe_name)
    print('Ingredients:')
    name = input('Name: ')
    quantity = input('Quantity (eg 200): ')
    measurement = input('Measurement (eg grams): ')
    ingredient = recipe.build_ingredient(name, quantity, measurement)
    recipe.add_ingredient_to_recipe_ingredients(ingredient)
    print('Instructions:')
    instruction = input('Instruction: ')
    recipe.add_instruction_to_recipe_instructions(instruction)
    print('Recipe: ', recipe.build_recipe())

    recipe_book = RecipeBook()
    recipe_book.add_recipe_to_recipe_book(recipe.build_recipe())
    print('Recipe Book: ', recipe_book.view_recipes())


if __name__ == '__main__':
    main()
