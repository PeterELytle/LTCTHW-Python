x= "There are %d types of people." % 10
# This line defines the variable "x" as a string of text containing another variable %d. Then it defines %d.

binary = "binary"
# This line defines the variable "binary".

do_not = "don't"
# This line defines the variable "do_not"

y = "Those who know %s and those who %s." % (binary, do_not)
# This line defines the variable y as a string of text containing 2 other variables. Then it defines the two variabes using variables defined previously.

print x
# This line displays the contents of variable x.

print y
# This line displays the contents of variable y.

print "I said: %r." % x
# This line displays some text, referencing a variable that displays more text.

print "I also said: '%s'" % y
# This line displays some text, referencing a variable that displays more text.

hilarious = False
# This line defines the variable "hilarious".

joke_evaluation = "Isn't that joke so funny?! %r."
# This line defines the variable "joke_evaluation", including an undefined variable.

print joke_evaluation % hilarious
# This line displays the output of the "joke_evaluation" variable, and defines it's nested variable.

w = "This is the left side of..."
# This line defines the variable "w" as a string of text.

e= "a string with a right side."
# This line defines the variable "e" as a string of text.

print w + e
# This line displays two variables.
