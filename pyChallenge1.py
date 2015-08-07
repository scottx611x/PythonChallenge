__author__ = 'Scott'
#pyChallenge 1
#http://www.pythonchallenge.com/pc/def/map.html

from string import maketrans

before = "abcdefghijklmnopqrstuvwxyz"
after = "cdefghijklmnopqrstuvwxyzab"
translator = maketrans(before, after)
with open('trash.txt', 'r') as f:
    for line in f:
        new = line.translate(translator)

#print new
#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

#url
x = "http://www.pythonchallenge.com/pc/def/map.html"

new = x.translate(translator)
print new

#http://www.pythonchallenge.com/pc/def/ocr.html