import unittest


ingredients = [
    {'name': 'flour', 'quantity': 1, 'measurement': 'kg'},
    {'name': 'sugar', 'quantity': 500, 'measurement': 'g'},
    {'name': 'pasta', 'quantity': 400, 'measurement': 'g'},
    {'name': 'milk', 'quantity': 1, 'measurement': 'l'},
    {'name': 'pasta_sauce', 'quantity': 200, 'measurement': 'ml'},
]


# TODO: Tests need renaming (CRUD)
class TestIngredients(unittest.TestCase):
    def test_add_ingredient_adds_an_ingredient_to_available_ingredients(self):
        pass

    def test_delete_ingredient_removes_an_ingredient_from_ingredients(self):
        pass

    def test_edit_ingredient_updates_the_ingredients_information(self):
        pass

    def test_get_ingredients_returns_all_available_ingredients(self):
        pass
