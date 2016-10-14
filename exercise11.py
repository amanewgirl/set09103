# Strings with raw input- from exercise 11 of Learning Python the Hard way

print "How old are you?", #The commas act like ';'
age = raw_input()
print "How tall are you?",
height = raw_input() #Stops to take in inout from command line/ user input
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

