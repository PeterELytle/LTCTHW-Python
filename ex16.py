from sys import argv
# This line says that the script will import the argument variables from the system (meaning the user will enter the variable definitions in-line when launching the script).

script, filename = argv
# This line says that there are two different argument variables to be imported from the system.

import os
os.system('cls')
# Command supplied by Chris Beedy. It clears Powershell of previous text, but I'm not sure exactly how it works. It's importing something from the operating system, and then calling the system function on "os".

print "we're going to erase %r." % filename
# This line prints some text and the variable "filename", defined by argv.
print "If you don't want to do that, press CTRL+C (^C)."
# This line displays some text.
print "If you want to do that, press RETURN."
# This line displays some text.

raw_input("?")
# This line provides a prompt to the user, giving them a chance to proceed or back out of the script.

print "Opening the file..."
# This line displays some text.
target = open(filename, 'w')
# This line defines the "target" variable as the result of running the open command, with write mode enabled, on the "filename" variable.

print "Truncating the file. Goodbye!"
# This line displays some text.
target.truncate()
# This line runs the truncate command (which empties the file), without parameters, on the "target" variable.

print "Now I'm going to ask you for three lines."
# This line displays some text.

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
# These 3 lines provide the user with a prompt, and the input of each line defines a variable.
lines = "%s\n%s\n%s" % (line1, line2, line3)
# This line, of my own creation, defines the "lines" variable as 3 formats, separated by "\n" escape characters, with each format defined by one of the variables defined by the above prompts.

print "I'm going to write these to a file."
# This line displays some text.

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
# These 6 lines constitute the original code provided by the lesson that write each of the user-defined variables to the file defined by "target", and separate each variable with a new line.

target.write(lines)
# This line, of my own creation, writes the "lines" variable to the "target" variable (which is the argv-defined file, opened with write permissions).

print "And finally, we close it."
# This line displays some text.
target.close()
# This line closes the "target" file.
