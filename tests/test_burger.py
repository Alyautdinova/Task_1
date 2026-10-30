from data.data_test import BUN_NAME, BUN_PRICE, SAUCE_NAME, SAUCE_PRICE, FILLING_NAME, FILLING_PRICE

class TestBurger:
    def test_set_buns(self, create_burger, mock_bun):
        create_burger.set_buns(mock_bun)
        assert create_burger.bun == mock_bun

    def test_add_ingredient(self, create_burger, mock_sauce):
        create_burger.add_ingredient(mock_sauce)
        assert create_burger.ingredients[0] == mock_sauce

    def test_remove_ingredient(self, create_burger, mock_sauce):
        create_burger.add_ingredient(mock_sauce)
        create_burger.remove_ingredient(0)
        assert len(create_burger.ingredients) == 0

    def test_move_ingredient(self, create_burger, mock_filling, mock_sauce):
        create_burger.add_ingredient(mock_filling)
        create_burger.add_ingredient(mock_sauce)
        
        create_burger.move_ingredient(1, 0) 
        
        assert create_burger.ingredients[0] == mock_sauce
        assert create_burger.ingredients[1] == mock_filling

    def test_get_price(self, create_burger, mock_bun, mock_filling, mock_sauce):
        create_burger.set_buns(mock_bun) # 200 - за 2 булки
        create_burger.add_ingredient(mock_filling) # 200 + 450 = 650
        create_burger.add_ingredient(mock_sauce) # 650 + 40 = 690
        
        assert create_burger.get_price() == BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE

    def test_get_receipt(self, create_burger, mock_bun, mock_filling, mock_sauce):
        create_burger.set_buns(mock_bun)
        create_burger.add_ingredient(mock_sauce)
        create_burger.add_ingredient(mock_filling)
        
        expected_receipt = (
            f"(==== {BUN_NAME} ====)\n"
            f"= sauce {SAUCE_NAME} =\n"
            f"= filling {FILLING_NAME} =\n"
            f"(==== {BUN_NAME} ====)\n\n"
            f"Price: {BUN_PRICE * 2 + SAUCE_PRICE + FILLING_PRICE}"
        )
        
        assert create_burger.get_receipt() == expected_receipt
    