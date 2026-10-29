import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    def test_ingredient_get_price(self, create_ingredient):
        assert create_ingredient.get_price() == 40.0

    def test_ingredient_get_name(self, create_ingredient):
            assert create_ingredient.get_name() == "tartar cream"

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "tartar cream", 40.0),
        (INGREDIENT_TYPE_FILLING, "meat", 450.0)
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
    