from PIL import Image
image = Image.open("monro.jpg")
width, height = image.size
red_channel, green_channel, blue_channel = image.split()

image = red_channel
new_red_image = red_channel.crop((50, 0, width, height))
image1 = red_channel
new_red_image1 = red_channel.crop((25, 0, width - 25, height))
image_red_blend = Image.blend(new_red_image, new_red_image1, 0.5)

image2 = blue_channel
new_blue_image = blue_channel.crop((0, 0, width - 50, height))
image3 = blue_channel
new_blue_image1 = blue_channel.crop((25, 0, width - 25, height))
image_blue_blend = Image.blend(new_blue_image, new_blue_image1, 0.5)

image4 = green_channel
new_green_image = green_channel.crop((25, 0, width - 25, height))

new_image5 = Image.merge("RGB", (image_red_blend, new_green_image, image_blue_blend))

max_size = (80, 80)
new_image5.thumbnail(max_size)

new_image5.save("monro_blend.jpg")
