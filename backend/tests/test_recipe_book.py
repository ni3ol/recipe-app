import unittest


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


class TestRecipeBook(unittest.TestCase):
    def test_create_recipe_adds_a_new_recipe_to_recipe_book(self):
        pass

    def test_view_recipes_returns_all_recipes(self):
        pass

    def test_view_recipe_returns_a_specific_recipe(self):
        pass

    def test_edit_recipe_updates_a_specific_recipe(self):
        pass

    def test_delete_recipe_removes_a_recipe_from_the_recipe_book(self):
        pass
