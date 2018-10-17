import pytest
import unittest


ingredients = {
    'flour': {'quantity': 1, 'measurement': 'kg'},
    'sugar': {'quantity': 500, 'measurement': 'g'},
    'pasta': {'quantity': 400, 'measurement': 'g'},
    'milk': {'quantity': 1, 'measurement': 'l'},
    'pasta_sauce': {'quantity': 200, 'measurement': 'ml'},
}

class TestIngredients(unittest.TestCase):
    def test_add_ingredient_adds_an_ingredient_to_available_ingredients(self):
        pass

    def test_delete_ingredient_removes_an_ingredient_from_available_ingredients(self):
        pass    

    def test_edit_ingredient_updates_the_ingredients_information(self):
        pass
    
    def test_get_ingredients_returns_all_available_ingredients(self):
        pass

    def test_get_missing_ingredients_returns_ingredients_missing_from_specific_recipe(self):
        pass