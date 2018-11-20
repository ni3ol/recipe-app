import unittest


shopping_list = [
    {
        'slug': 'woolworths',
        'name': 'Woolworths Shopping List',
        'ingredients': [
            {
                'slug': 'lindt_chocolate',
                'name': 'Lindt chocolate',
                'quantity': 200,
                'measurement': 'g',
            },
            {
                'slug': 'orange_juice',
                'name': 'Freshly Squeezed Orange Juice',
                'quantity': 500,
                'measurement': 'ml',
            },
            {
                'slug': 'lettuce',
                'name': 'Butter Lettuce',
                'quantity': 200,
                'measurement': 'g',
            },
        ]

    },
]


# TODO: Tests need renaming (CRUD)
class TestShoppingList(unittest.TestCase):
    def test_get_shopping_list_returns_the_items_for_a_specific_recipe(self):
        pass

    def test_add_item_to_shopping_list_adds_ingredient_to_list(self):
        pass

    def test_edit_shopping_list_updates_a_shopping_list(self):
        pass

    def test_create_shopping_list_makes_a_new_shopping_list(self):
        pass

    def test_delete_item_from_shopping_list_removes_item_from_list(self):
        pass

    def test_delete_shopping_list_deletes_a_shopping_list(self):
        pass
