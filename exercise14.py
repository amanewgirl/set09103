#Prompting and parsing- Exercise 14 of Learn Python the hard way

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script."% (user_name, script)
# 'user_name'was passed and script is passed in as the name of the script when you type in the run
#statement : python exercise14 user_name_arg """

print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)#this will insert '>' in the prompt

print "Where do live %s?" %user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# The use of %r makes sense as the variables being substituted in are raw
# inputs and need to be debugged to make sure the user actually put in dome
# input 
print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
