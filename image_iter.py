from PIL import Image, ImageFilter
from random import randint
images = ["./images/blur.png", "./images/grey.png", "./images/Watney.jpg"]
append_image = []
def iterate():
    generate_img_id = randint(0,5)
    for i in images:
        show = Image.open(i)
        show_filtered= show.filter(ImageFilter.BLUR)
        grey = show_filtered.save(f'./images/{generate_img_id}.png', 'png')
        # grey = show.convert('L')
        append_image.append(grey)

iterate()
print("The Saved File name in list: ", append_image)
# show_appended_img = Image.open(append_image[0])
# show_appended_img.show()

def grey():
    show_img = Image.open(images[0])
    conver_show_img = show_img.convert('L')
    conver_show_img.save(f'./images/grey/{randint(0,5)}.png', 'png')
    conver_show_img.show()

grey()