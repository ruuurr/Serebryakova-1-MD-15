
from PIL import Image


original_image = Image.open("D:\IITA\pycharm\kotyonok_ra.jpg")

small_image = original_image.resize((original_image.width // 3, original_image.height // 3))

horizontal_mirror = original_image.transpose(Image.FLIP_LEFT_RIGHT)

vertical_mirror = original_image.transpose(Image.FLIP_TOP_BOTTOM)

small_image.save("small_kotyonok_ra.jpg")

horizontal_mirror.save("horizontal_kotyonok_ra.jpg")

vertical_mirror.save("vertical_kotyonok_ra.jpg")

