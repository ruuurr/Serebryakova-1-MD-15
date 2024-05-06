import csv

def soz_csv(file_path):
    data = [
        ["продукт", "количество", "цена"]
            [ "молоко", 2, 80 ]
             ["сыр", 1, 500]
             ["хлеб", 2, 70 ]
             ]
    with open(file_path, mode = 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

file_path = "csv"
create_csv_file(file_path)


def sravn(file_path):
    price = 0
    shop_list = []

with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        product = row[0]
        q = int(row[1])
        p = int(row[2])
        price += q * p
        shop_list.append(f"{product} - {q} za {p}")

        print("kupit nada:")
        for item in shop_list:
            print(item)
            print (f"summa: {price}")
            
