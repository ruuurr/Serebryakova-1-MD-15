import os
import json


initial_data = {
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


if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=4)




def read_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)



def get_user_data():
    name = input("введите название продукта: ")
    price = float(input("введите цену продукта: "))
    available = input("продукт в наличии? (да/нет): ").strip().lower() == 'да'
    weight = float(input("введите вес продукта (в граммах): "))
    return {"name": name, "price": price, "available": available, "weight": weight}



def write_data_to_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)



def print_data(data):
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


def main():

    data = read_data_from_file(file_path)

    new_data = get_user_data()
    data['products'].append(new_data)


    write_data_to_file(data, file_path)


    print("данные в файле JSON:")
    print_data(data)


if __name__ == "__main__":
    main()