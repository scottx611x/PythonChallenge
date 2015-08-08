__author__ = 'Scott'
#pyChallenge 6
#url: http://www.pythonchallenge.com/pc/def/channel.html

#HINT: now there are pairs
#HINT: zip

# pants.html
#HINT: amazing. zoom in
#url: http://www.pythonchallenge.com/pc/def/channel.zip -> downloads a zip file

#IN ZIP
#welcome to my zipped list.

#hint1: start from 90052
#hint2: answer is inside the zip

import re
from zipfile import ZipFile

global nothing, comments

nextNothing = ""
comments = ""
zf = ZipFile("channel.zip")

def getComment(info):
        global comments
        comments = comments + info.comment

with open('channel/90052.txt', 'r') as f:
    getComment(zf.getinfo("90052.txt"))
    for line in f:
        nothing = re.findall(r'[0-9]+', line)
    nextNothing = nextNothing + str(nothing[0])

while True:
    with open("channel/%s.txt" % nextNothing, "r") as file:
        getComment(zf.getinfo("%s.txt" % nextNothing))
        nextNothing = ""
        for line in file:
            nothing = re.findall(r'[0-9]+', line)
            nextNothing = nextNothing + str(nothing[0])
#GIVES: Collect the comments.
    print comments

#****************************************************************
#****************************************************************
#**                                                            **
#**   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
#**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
#**   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
#**   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
#**   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
#**   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
#**   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
#**   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
#**                                                            **
#*****************************************
#****************************************************************

#url http://www.pythonchallenge.com/pc/def/oxygen.html