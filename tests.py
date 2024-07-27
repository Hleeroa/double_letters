import pytest
from main import double_letters


@pytest.mark.parametrize('string,expected', (['L e o P e t e r s o n',
                         'LL  ee  oo  PP  ee  tt  ee  rr  ss  oo  nn'], ))
def test_double_letters(string, expected):
    actual = double_letters(string)
    assert actual == expected
