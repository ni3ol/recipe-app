# From Pierre's review:

New lines at end of file. Spaces after hashes Check with Flake8.

Consider second datastructure over first.
ingredients = {
  'flour': {...},
}
vs

ingredients = [
{ name: 'flour', ...}
]

Don't get confused between imperative and functional programming.
In an imperative style you accept the ingredients list as an argument, and modify that list of ingredients.
In a functional style, we also accept the ingredients list as an argument, but we make a copy and leave the original ingredients alone. We also return our new list, so the caller now has two copies, the original, and the modified one.

Use a program readable key (often called a slug) and a human readable name in representing data

Introduce idea of food list so that can use inheritence for shopping list, which might have prices etc.

Make use of # TODOS: in code

Need to deal with measurement abstraction consistently.
my_flour = { brand: 'knor', quantity: 0.200 } # 200g of flour.
Then backend doesnt care about measurement

Use Click for CLI interaction before working on Frontend.

Consider when to use private and static methods.
The build ingredient function should be static, because you don't need a Recipe to build an ingredient.
Then you can build ingredients without making a 'dummy recipe' just to throw it away.
One reason to not do this, is if the build_ingredient function is only used by the Recipe class, but then it must be private and start with an underscore _build_igredient()

Use namedtuples over dicts where there is a shape
Ingredient = namedtuple('Ingredent', ['name', 'quantity', 'measurement'])

flour = Ingredient('flour', 60, 'g')

print(flour.name, flour.quantity, flour.measurement)

Use CRUD in naming