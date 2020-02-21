# from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
#filtered_img = img.filter(ImageFilter.SHARPEN)
#BLUR, SHARPEN, SMOOTH
# filtered_img = img.convert('L')
# # resize = filtered_img.resize((300, 300)) resize image
# # resize.save("resize.png", 'png')
# # crooked = filtered_img.rotate(180) rotates image
# # crooked.save("grey.png", 'png')
# #filtered_img.save("grey.png", 'png') # saves image to new file
# #filtered_img.show()
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save("region.png", 'png')

# img = Image.open('./astro.jpg')
# img.thumbnail((400, 380)) # will never go over 400, 400 but keeps aspect ratio
# img.save('thumbnail.jpg')