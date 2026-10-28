prices = [25.00, 50.00, 75.00, 100.00, 150.00]

def discount(original):
    return original*0.8

discounted = list(map(discount, prices))
print(f"Original Prices: {prices}")
print(f"Sale Prices: {discounted}")