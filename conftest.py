import pytest
from praktikum.bun import Bun

@pytest.fixture
def create_bun():
    return Bun("black bun", 100.0)
    