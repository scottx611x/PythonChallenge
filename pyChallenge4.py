import urllib2

__author__ = 'Scott'
# pyChallenge 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# HINT: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# HINT: and the next nothing is: 44827

import re, requests
from bs4 import BeautifulSoup

r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' % 44827)
soup = BeautifulSoup(r.content,"html.parser")
print "SOUP: ", soup
nothing = re.findall(r'[0-9]+', str(soup))
print "NOTHING: ", nothing[0]
while True:

    r = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing[0])
    soup = BeautifulSoup(r.content,"html.parser")
    nothing = re.findall(r'[0-9]+', str(soup))
    print "NOTHING:", nothing[0]


#answer peak.html
#url HINT: http://www.pythonchallenge.com/pc/def/peak.html