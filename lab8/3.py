
name = input("введите имя человека, которого вы хотите поздравить: ")

from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(kotyonok_ra.jpg)


font_path = "arial.ttf"
font = ImageFont.truetype(font_path, size=30)


text = f"{name}, поздравляю!"
text_width, text_height = draw.textsize(text, font)
image_width, image_height = kotyonok_ra.size
text_position = ((image_width - text_width) // 2, image_height - text_height - 20)


draw.text(text_position, text, fill="red", font=font)


card_image.save("пkotyonok_ra.png")