__author__ = 'Scott'
# pyChallenge 3
# http://www.pythonchallenge.com/pc/def/equality.html
# HINT: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

import re

with open('trash2.txt','r') as f:
    new=""
    for line in f:
        x = re.findall(r'[^A-Z]([A-Z]{3}([a-z]{1})[A-Z]{3})[^A-Z]', line, flags=0)
        if x:
            new += x[0][1]
    print new

#answer
# linkedlist
#url
# http://www.pythonchallenge.com/pc/def/linkedlist.html
# goes to linkedlist.php
# http://www.pythonchallenge.com/pc/def/linkedlist.php