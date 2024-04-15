def data(date):
    try:
        day, month, year = map(int, date.split('.'))
        if day * month == year % 100:
            return True
        else:
            return False
    except ValueError:
        return False


date = input("введите дату в формате 'дд.мм.гггг': ")
if data(date):
    print("это магическая дата!")
else:
    print("это не магическая дата")
