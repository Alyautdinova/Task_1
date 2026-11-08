import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.data_test import SAUCE_NAME, SAUCE_PRICE, FILLING_NAME, FILLING_PRICE

class TestIngredient:
    def test_ingredient_get_price(self, create_ingredient):
        assert create_ingredient.get_price() == SAUCE_PRICE

    def test_ingredient_get_name(self, create_ingredient):
        assert create_ingredient.get_name() == SAUCE_NAME

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE),
        (INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
    