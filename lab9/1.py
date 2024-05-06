from PIL import Image
import os

def chb(nach, kon):
    os.makedirs(kon)

    for filename in os.listdir(nach):
        if filename.endswith('.jpg'):

            nach_image = os.path.join(nach, filename)
            kon_image = os.path.join(kon, filename)

            image = Image.open(nach_image)
            chb_image = image.convert("L")

            chb_image.save(kon_image)



