from PIL import Image, ImageFilter
from random import randint
images = ["./images/blur.png", "./images/grey.png", "./images/Watney.jpg"]
append_image = []
def iterate():
    generate_img_id = randint(0,5)
    for i in images:
        show = Image.open(i)
        show_filtered= show.filter(ImageFilter.BLUR)
        show_filtered.save(f'./images/{generate_img_id}.png', 'png')
        grey = show.convert('L')
        # save_grey_img = grey.save(f'./images/{generate_img_id}.png', 'png')
        append_image.append(grey)

iterate()
print(f'The Saved File name in list: {append_image}')
# show_appended_img = Image.open(append_image[0])
# show_appended_img.show()