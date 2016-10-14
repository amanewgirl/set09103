# Exercise 12 of learning Python the hard way - Prompting people

#Putting text inside '()' will give users a hint of what to typ
y = raw_input("Name? ")

"""OR"""


age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh?") 

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
