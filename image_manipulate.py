from PIL import Image, ImageFilter

img = Image.open("./images/Watney.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
grey_img = img.convert(mode='L')
grey_img.save("./images/grey.png", "png")
