def delenie(num):
    if num % 3 == 0:
        return True
    else:
        return False

num = int(input("введите число: "))
if delenie(num):
    print(f"{num} делится на 3")
else:
    print(f"{num} не делится на 3")