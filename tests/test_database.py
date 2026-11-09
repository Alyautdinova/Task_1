from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()

        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

        assert buns[0].get_price() == 100.0
        assert buns[1].get_price() == 200.0
        assert buns[2].get_price() == 300.0

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        for ingredient in ingredients[:3]: 
            assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        for ingredient in ingredients[3:]:
            assert ingredient.get_type() == INGREDIENT_TYPE_FILLING

        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[5].get_name() == "sausage"

        assert ingredients[0].get_price() == 100.0
        assert ingredients[1].get_price() == 200.0
        assert ingredients[2].get_price() == 300.0
        assert ingredients[3].get_price() == 100.0
        assert ingredients[4].get_price() == 200.0
        assert ingredients[5].get_price() == 300.0
    