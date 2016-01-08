from sys import argv
# This line says that the script will import the argument variables from the system (meaning the user will enter the variable definitions in-line when launching this script).

script, first, second, third = argv
# This line says that there are 4 different argument variables, to be imported from the system (meaning the user will enter them when launching the script, on the same line).

print "The script is called:", script
# This line displays some text, and the script name.
print "Your first variable is:", first
# This line displays some text, and the "first" variable, defined by argv.
print "Your second variable is:", second
# This line displays some text, and the "second" variable, defined by argv.
print "Your third variable is:", third
# This line displays some text, and the "third" variable, defined by argv.

scripts = raw_input("How many scripts have you written? ")
# This line displays some texts, prompts the user for input and uses the input to define the "scripts" variable.

print "Congratulations on writing %s scripts." % scripts
# This line displays some text and the "scripts" variable.
