__author__ = 'Scott'
# pyChallenge 2
# http://www.pythonchallenge.com/pc/def/ocr.html

import re

with open('trash1.txt', "r") as f:
    new = ""
    for line in f:
        x = re.findall(r'[^+-_\^\[\]!@#$&*(){} % \n]', line, flags=0)
        if x:
            new += x[0]

    print new

# OUTPUT
# equality
#url
# http://www.pythonchallenge.com/pc/def/equality.html
