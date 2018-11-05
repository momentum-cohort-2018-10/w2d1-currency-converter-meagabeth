from currency_converter import convert

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


