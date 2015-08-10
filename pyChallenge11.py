__author__ = 'Scott'
#pyChallenge 11
#url: http://www.pythonchallenge.com/pc/return/5808.html

#HINT: odd even

from PIL import Image

#open image
img = Image.open("cave.jpg")
img= img.convert("RGB")
new1 = Image.new("RGB", img.size)

#iterate through pixels
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if i % 2 == 0 and j % 2 ==0:
            new1.putpixel((i,j), img.getpixel((i, j)))
new1.show()

#Yeilds an image with the text: evil

#url: http://www.pythonchallenge.com/pc/return/evil.html