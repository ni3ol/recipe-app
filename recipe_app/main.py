from recipe_book import RecipeBook

def main():
    recipe_book = RecipeBook()
    print('Hello! Welcome to your Recipe App!')
    print('What would you like to do?')
    print('-vr [RECIPE_NAME]       view list of recipes (or specific recipe) in app')
    print('-vsl [SHOPPING_LIST]    view list of shopping lists or specific list') 
    print('-asl [NAME]             add a new shopping list')

    command = input()
    print(command)



if __name__ == '__main__':
    main()