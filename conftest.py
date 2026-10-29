import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING

@pytest.fixture
def create_bun():
    return Bun("black bun", 100.0)

@pytest.fixture
def create_ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "tartar cream", 40.0)
   