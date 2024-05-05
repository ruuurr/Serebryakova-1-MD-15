
from PIL import Image


image = Image.open("D:\IITA\pycharm\kotyonok_ra.jpg")


print("Размер изображения:", image.size)
print("Формат изображения:", image.format)
print("Цветовая модель:", image.mode)

image.save("kotyonok_ra.jpg")

image.show()