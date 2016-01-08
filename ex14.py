from sys import argv
# This line says that the script will import the argument variables from the system (meaning the user will enter the variable definitions in-line when launching the script).

script, user_name = argv
# This line says that there are two different argument variables, to be imported from the system (meaning the user will enter the variable definitions in-line when launching the script).
prompt = '> '
# This line defines the prompt given to users as "> ".

print "Hello %s, I'm the %s script." % (user_name, script)
# This line displays some text and 2 variables, as defined by argv.
print "I'd like to ask you a few questions."
# This line displays some text.
print "Do you like me %s?" % user_name
# This line displays some text and a variable, as defined by argv.
likes = raw_input(prompt)
# This line provides the user with a prompt, and uses the input to define the "likes" variable.

print "Where do you live %s?" % user_name
# This line displays some text and a variable, as defined by argv.
lives = raw_input(prompt)
# This line provides the user with a prompt, and uses the input to define the "lives" variable.

print "What kind of computer do you have?"
# This line displays some text.
computer = raw_input(prompt)
# This line provides the user with a prompt, and uses the input to defines the "computer" variable.

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that us.
And you have a %s computer. Nice.
""" % (likes, lives, computer)
# This line displays a few lines of text and 3 variables, defined earlier by the user.
