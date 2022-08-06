from main import square
import pytest

def test_positivesquare():

    assert square(2) == 4
    assert square(3) == 9


def test_negativesquare():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zerosquare():
    assert square(0) == 0

def test_strsquare():
    with pytest.raises(TypeError):
        square("cow")