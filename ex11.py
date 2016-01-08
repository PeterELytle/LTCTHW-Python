print "How old are you?",
# This line displays some text, and uses a comma to make the next command appear on the same line.

age = raw_input()
# This line accepts user input and stores it as the definition for the variable "age".

print "How tall are you?",
# This line displays some text, and uses a comma to make the next command appear on the same line.

height = raw_input()
# This line accepts user input and stores it as the definition for the variable "height".

print "How much do you weigh?",
# This line displays some text, and uses a comma to make the next command appear on the same line.

weight = raw_input()
# This line accepts user input and stores it as the definition for the variable "weight".

print "So, you're %r years old, %r tall and %r pounds heavy." % (age, height, weight)
# This line displays some text with 3 variables, and then defines the variables using the definitions set by the user. Since the variables are "%r", any single quotes in the "height" variable will appear with an escape character.
