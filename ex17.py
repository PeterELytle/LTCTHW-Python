from sys import argv
# This line says that the script will import argument variables from the system (provided by the user when launching the script).
from os.path import exists
# This line imports the exists command from the operating system(?).

import os
os.system('cls')
# Command supplied by Chris Beedy. It clears Powershell of previous text, but I'm not sure exactly how it works. It's importing something from the operating system, and then calling the system function on "os".

script, from_file, to_file = argv
# This line says that there are 3 argument variables to be defined by the user when launching the script.

print "Copying from %s to %s." % (from_file, to_file)
# Displays some text and 2 of the argument variables.

# We could do these two on one line. How? By replacing in_file with the definition. See line ???
in_file = open(from_file)
# This line defines the "in_file" variable as the output of opening the "from_file" variable.
in_data = in_file.read()
# This line defines the "in_data" variables as the result of calling the read command, without parameters, on the "in_file" variable.


print "The input file is %d bytes long." % len(indata)
# This line displays some text, and displays the output of running the len funtion on the "indata" variable.

print "Does the output file exist? %r." % exists(to_file)
# This line dusplays some text, and the output of running the exists command on the "to_file" variable.
print "Ready? Press RETURN to continue, or CTRL+C to abort."
# This line displays some text.
raw_input()
# This line accepts the users input before continuing.

out_file = open(to_file, 'w')
# This line defines the "out_file" variable as the result of opening the "to_file" variable with write mode enabled.
out_file.write(in_data)
# This line calls the write command on the "out_file" variable, and writes the content of "in_data" to "out_file".

print "Alright, all done."
# This line displays some text.

out_file.close()
# This line calls the close command on "out_file".
in_file.close()
# This line calls the close command on "in_file".
