# list = [(value, form, to)]
rates = [
    ("USD", "EUR", 0.74),
    ("EUR", "JPY", 145.949)
    ]

def convert(list, value, original, to):
    if original == to:
        return value
    for conversion in rates:
        if original == conversion[0] and to == conversion[1]:
            return value * conversion[2]
        if original == conversion[1] and to == conversion[0]:
            return value / conversion[2]    