products = [ 

    {"name": "Keyboard", "price": 45}, 

    {"name": "Monitor", "price": 180}, 

    {"name": "Mouse", "price": 25}, 

    {"name": "Headphones", "price": 75}, 

    {"name": "USB Drive", "price": 15}, 

    {"name": "Webcam", "price": 60} 

]

below50 = list(filter(lambda price: price["price"] < 50, products))
print("Products under $50")
for product in below50:
    print(f"{product["name"]} - ${product["price"]}")