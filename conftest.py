import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from unittest.mock import Mock
from data.data_test import BUN_NAME, BUN_PRICE, SAUCE_NAME, SAUCE_PRICE, FILLING_NAME, FILLING_PRICE

@pytest.fixture
def create_bun():
    return Bun(BUN_NAME, BUN_PRICE)

@pytest.fixture
def create_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE)

@pytest.fixture
def create_burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun

@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_name.return_value = SAUCE_NAME
    sauce.get_price.return_value = SAUCE_PRICE
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce

@pytest.fixture
def mock_filling():
    sauce = Mock()
    sauce.get_name.return_value = FILLING_NAME
    sauce.get_price.return_value = FILLING_PRICE
    sauce.get_type.return_value = INGREDIENT_TYPE_FILLING
    return sauce
