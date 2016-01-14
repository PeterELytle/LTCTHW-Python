# This line defines the "print_two" function, and it will have arguments.
def print_two(*args):
	# This line defines two arguments to be used in the function.
	arg1, arg2 = args
	# This line displays some text, and both variables (which are defined as the function arguments).
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# This line defines the "print_two_again" function, and it will have two arguments, named arg1 and arg2.
def print_two_again(arg1, arg2):
	# This line displays some text, and both variables (which are defined as the function arguments).
	print "arg1: %r, arg2: %r" %  (arg1, arg2)
	
# This line defines the "print_one" function, and it will have a single argument.
def print_one(arg1):
	# This line displays some text, and the variable (which is defined as the function argument).
	print "arg1: %r" % arg1
	
# This line defines the "print_none" argument. It has no arguments.
def print_none():
	# This line displays some text.
	print "I got nothin'."
	
# This line calls the "print_two" function, and defines its arguments.
print_two("Peter","Lytle")
# This line calls the "print_two_again" function, and defines its arguments.
print_two_again("John","Doe")
# This line calls the "print_one" function, and defines its argument.
print_one("First!")
# This line calls the "print_none" argument.
print_none()
