import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from unittest.mock import Mock

@pytest.fixture
def create_bun():
    return Bun("black bun", 100.0)

@pytest.fixture
def create_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "tartar cream", 40.0)

@pytest.fixture
def create_burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50.0
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce

@pytest.fixture
def mock_filling():
    sauce = Mock()
    sauce.get_name.return_value = "meat cutlet"
    sauce.get_price.return_value = 450.0
    sauce.get_type.return_value = INGREDIENT_TYPE_FILLING
    return sauce