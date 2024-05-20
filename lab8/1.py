from PIL import Image


image = Image.open("kotyonok_ra.jpg")


cropped_image = image.crop((100, 100, 500, 500))


cropped_image.save("cut_kotyonok_ra.jpg")