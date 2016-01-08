from sys import argv
# This line says that the script will import argument variables from the system.

script, filename = argv
# This line says that there are 2 argument variables to be defined by the user when launching the script.

import os
os.system('cls')
# This line clears Powershell.

txt = open(filename)
# This line defines the "txt" variable as the result of running the open command on the argv-defined "filename".

print "Lets look at %s." % filename
# This line displays some text and the "filename" variable.
print txt.read()
# This line calls the read command, without parameters, on the "txt" variable and displays the results.
txt.close()
# This line calls the close command, without parameters, on the "txt" variable.
