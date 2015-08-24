__author__ = 'Scott'
# pyChallenge 12
# url:http://www.pythonchallenge.com/pc/return/evil.html
# HINT: dealing evil
# HINT: http://www.pythonchallenge.com/pc/return/evil2.jpg reutrns an image that says: not jpg, gfx
# HINT: (2 .jpgs, 2 .pngs and 1 .gif).


#Unshuffle data into 2 pngs, 2 jpgs and one gif

with open('evil2.gfx','rb') as f, open('one.jpg','wb') as one, open('two.png','wb') as two, open('three.gif','wb') as three, open('four.png','wb') as four, open('five.jpg','wb')as five:

    for i in range(0,67575,5):
        one.write(f.read(1))
        two.write(f.read(1))
        three.write(f.read(1))
        four.write(f.read(1))
        five.write(f.read(1))

#yields 5 images with the letters dis pro port ional ity
#new url = http://www.pythonchallenge.com/pc/return/disproportional.html