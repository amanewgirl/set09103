#Just testing the ctrl-c command in python, an extension of exercise 16

from sys import argv

script, filename = argv

print "We're going to erase %r."% filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'r')

print "Truncating the file. Goodbye!"
target.truncate()
