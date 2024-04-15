def vbor_seat_type(num):
    kupe_seat = [i for i in range(1, 36)]
    bokovoe_seat = [i for i in range(36, 54)]

    if num in kupe_seat:
        if num % 2 == 0:
            return "купе - верхнее"
        else:
            return "купе - нижнее"
    elif num in bokovoe_seat:
        if num % 2 == 0:
            return "боковое верхнее"
        else:
            return "боковое нижнее"
    else:
        return "некорректный номер"


num = int(input("ведите номер места в вагоне: "))

seat_type = vbor_seat_type(num)
print("Тип места:", seat_type)