#Exercise 16 from Learn Python the Hard way- Reading and writing

from sys import argv

script, filename = argv

print "Opening the file: "
target = open(filename, 'w')

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write this to the file %s." %filename
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "This end the writing segment of this exercise, please hold on for other options"
print "In the mean time I will close this file"
target.close()
