#Complicated  Strings- exercise 8 for Python the Hard way

#Debugging by  saving the raw data of the variable
formatter = "%r %r %r %r" #THis is like saying, formatter consists of whatever
#4 variables you decide to substitute into it

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter) # so this will
#print out raw " formatter" four times
print formatter %(
      "I had this thing.",
      "That you could type up right.",
      "But it didn't sing.",
      "So I said goodnight."
      )
