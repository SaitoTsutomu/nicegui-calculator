import pytest

from nicegui_calculator import Calculator


@pytest.mark.parametrize(
    ("keys", "expected"),
    [
        ([*"12+3"], "12 + 3"),
        ([*"1+-2"], "1 - 2"),
        ([*"12", "AC", *"3*4="], "12"),
        ([*"3.14/2="], "1.57"),
        ([*"98", "+/-", *"+100="], "2"),
        ([*"10%-1="], "-0.9"),
        ([*"1+2*3-4/2="], "5.0"),
        ([*"2*3=4+5="], "9"),
    ],
)
def test_calc(keys, expected):
    actual = Calculator.calc(keys)
    assert actual == expected
