from praktikum.bun import Bun

class TestBun:
    def test_bun_get_name(self, create_bun):
        assert create_bun.get_name() == "black bun"

    def test_bun_get_price(self, create_bun):
        assert create_bun.get_price() == 100.0
