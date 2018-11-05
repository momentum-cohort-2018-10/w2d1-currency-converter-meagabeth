from currency_converter import convert
import pytest

rates = [
    ("USD", "EUR", 0.74),
    ("EUR", "JPY", 145.949)
    
    ]

def test_convert():
    assert convert(rates, 1, "USD", "EUR") == 0.74
    assert convert(rates, 10, "USD", "EUR") == 7.4
    assert convert(rates, 0.74, "EUR", "USD") == 1
    assert convert(rates, 1, "EUR", "EUR") == 1
    assert round(convert(rates, 1, "EUR", "JPY"), 2) == 145.95
    assert round(convert(rates, 145.949, "JPY", "EUR"), 2) == 1


def test_converting_with_no_rates():
    """
    Using rates defined below, raise a ValueError if called parameters do not match the truple(s) within the rates list.
    """
    rates = [("USD", "EUR", 0.74)]
    # we use pytest.raise(ValueError) since we don't have a non-test version of this function
    with pytest.raises(ValueError):
        # raises a ValueError because the following parameters don't match any of the truples in the list of conversion rates.
        convert(rates, value=10, original = "USD", to = "SWD")
    