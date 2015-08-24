__author__ = 'Scott'
#url: disproportional.hmtl
#Hint: call him
#Hint: phone that evil
#Hint: Bert is Evil was a hint from some previous level
#Hint clicking on the 5 button on the image yeilds a php page that has invalid xml
# why not use xmlrpclib to "PHONE" this server

import xmlrpclib
server = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print server.phone("Bert")
#Phoning Bert yeilds 555-ITALY

#555-48259???

#print server.phone("555-4829") yeilds
#He is not the evil

#url: italy.html ended up working