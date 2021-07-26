import pytest
from stos import utworz_stos, na_stos, ze_stosu

def test_utworz_stos():
    pusty_stos = utworz_stos()
    assert pusty_stos.wierzch is None

@pytest.fixture
def pusty_stos():
    return utworz_stos()

def test_elem_na_pusty_stos():
    pusty_stos = utworz_stos()
    na_stos(pusty_stos, "Test")
    assert pusty_stos.wierzch.wartosc == "Test"
