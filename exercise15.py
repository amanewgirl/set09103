#Reading Files- Exercise 15 of learn Python the hard way

#the following isslightly customised to print the file passed in as an
#arguement at runtime
from sys import argv

script, file = argv

document_in_use = open(file)
print "You are going to see the contents of %r"% file
print  document_in_use.read()
print "."*30




# the following prints according to input after the script has been run
doc = raw_input("Please put the name of the file you want read here: ")

txt = open(doc)
print txt.read()
