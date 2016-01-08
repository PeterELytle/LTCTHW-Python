from sys import argv
# This line says that the script will import the argument variables from the system (meaning the user will enter the variable definitions in-line when launching the script).

script, filename = argv
# This line says that there are two different argument variables, to be imported from the system (meaning the user will enter the variables in-line when launching the script)

import os
os.system('cls')
# Command supplied by Chris Beedy. It clears Powershell of previous text, but I'm not sure exactly how it works. It's importing something from the operating system, and then calling the system function on "os".

txt = open(filename)
# This line defines the "txt" variable as the output of opening "filename", which was defined earlier by argv.

print "Here's your file %r:" % filename
# This line displays some text and the variable defined as "filename".
print txt.read()
# This line calls the read command, without parameters, on the txt variable, which is defined as the open command on the variable "filename". In short, it opens "filename", reads it and displays the output.
txt.close()
# This line calls the close command, without parameters, on the output of the txt variable.


# print "Here's your file %r:" % filename
# print open(filename).read()
# open(filename).close()
# These 3 lines are my test of the transitive property of equality. I was seeing if the "txt" variable could be replaced with its definition. It can, the above 3 lines work just fine.

print "Type the filename again:"
# This line displays some text.
file_again = raw_input("> ")
# This line provides the user with a prompt, and uses the input to define the "file_again" variable.

txt_again = open(file_again)
# This line defines the "txt_again" variable as the "open(file_again)" command, using the definition of "file_again" as provided above by the user.

print txt_again.read()
# This line calls the read command, without parameters, on the "txt_again" variable (which is just the open(file_again) command, and "file_again" is the filename as supplied by the user) and displays the result.
txt_again.close()
# This line calls the close command, without parameters, on the output of the "txt_again" variable.
