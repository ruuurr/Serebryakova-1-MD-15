def delna100(number):
    try:
        result = 100 / number
        return result
    except ZeroDivisionError:
        return "на ноль делить нельзя"
    except ValueError:
        return

def main():
    try:
        num = float(input("введите число:"))
        result = delna100(num)
        print(f"результат: {result}")
    except ValueError:
        print("ошибка. введено не число")

if __name__ == "__main__":
    main()