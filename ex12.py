age = raw_input("How old are you? ")
# This line displays some text and requests information from the user, defining the "age" variable with the user's input.

height = raw_input("How tall are you? ")
# This line displays some text and requests information from the user, defining the "height" variable with the user's input.

weight = raw_input("How much do you weigh? ")
# This line displays some text and requests information from the user, defining the "weight" variable with the user's input.

print "So, you're %s years old, %s tall and %s pounds heavy." % (age, height, weight)
# This line displays some text with 3 "%s" variables, and then defines the variables using the information provided by the user. Since the variables are "%s", single quotes in "height" will appear without an escape character.
