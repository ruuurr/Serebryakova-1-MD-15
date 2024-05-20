cards = {
    "день дождения": "dr.jpg",
    "новый год": "sng.jpg",
    "8 Марта": "s8.jpg",
    "1 мая": "s1maya.png",
    "23 февраля": "s23.jpg",

}

holiday = input("праздник, для которого нужна открытка: ")


if holiday in cards:
  
    card_path = cards[holiday]
    card_image = Image.open(card_path)
    card_image.show()
else:
    print("открытка не найдена.")