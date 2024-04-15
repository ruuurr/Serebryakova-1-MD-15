def colors(color1, color2):
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        return "фиолетовый"
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        return "оранжевый"
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        return "зеленый"
    else:
        return "Ошибка: Введите два из основных цветов: 'красный', 'синий' или 'желтый'."

def main():
    color1 = input("первый цвет:").lower()
    color2 = input("второй цвет:").lower()

    result = colors(color1, color2)
    print(result)
if __name__ == "__main__":
    main()