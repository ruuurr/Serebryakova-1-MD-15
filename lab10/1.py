import os
import json

data = {
    "products": [
        {
            "name": "шоколад",
            "price": 50,
            "available": True,
            "weight": 100
        },
        {
            "name": "кофе",
            "price": 100,
            "available": False,
            "weight": 250
        },
        {
            "name": "чай",
            "price": 70,
            "available": True,
            "weight": 50
        }
    ]
}


os.makedirs('json', exist_ok=True)

file_path = os.path.join('json', 'products.json')


with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)


for product in data['products']:
    name = product['name']
    price = product['price']
    weight = product['weight']
    availability = "в наличии" if product['available'] else "нет в наличии"

    print(f"название: {name}")
    print(f"цена: {price}")
    print(f"вес: {weight}")
    print(availability)
    print()