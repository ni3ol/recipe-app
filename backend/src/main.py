import click
from recipe_book import RecipeBook
from recipe import Recipe


# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)

# if __name__ == '__main__':
#     hello()

# $ python hello.py --count=3
# Your name: John
# Hello John!
# Hello John!
# Hello John!

@click.command()
@click.option('--add_recipe', prompt='Name', help='Add new recipe with ingredients and instructions.')
def main(add_recipe):

    recipe = Recipe(name=add_recipe)
    ingredients_finished = 'n'
    while ingredients_finished == 'n':
        name = input('Ingredrient Name: ')
        quantity = input('Quantity (eg 200): ')
        measurement = input('Measurement (eg grams): ')
        ingredient = recipe.create_ingredient(name, quantity, measurement)
        recipe.update_recipe_ingredients(ingredient)
        ingredients_finished = input('Finished adding ingredients (y/n)? ')

    instructions_finished = 'n'
    while instructions_finished == 'n':
        instruction = input('Instruction: ')
        recipe.update_recipe_instructions(instruction)
        instructions_finished = input('Finished adding instructions (y/n)? ')

    print('Recipe: ', recipe.create_recipe())
    recipe_book = RecipeBook()
    recipe_book.create_recipe_in_recipe_book(recipe.create_recipe())
    print('Recipe Book: ', recipe_book.retrieve_recipes())


if __name__ == '__main__':
    main()
