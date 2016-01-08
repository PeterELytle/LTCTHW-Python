from sys import argv
# This line says that the script will import argument variables from the system.
from os.path import exists
# This line says that the script will import the "exists" command from the operating system. (?)

script, from_file, to_file = argv
# This line says that thee are 3 argument variables to be defined by the user when launching the script.

#in_file = open(from_file)
#in_data = in_file.read()
in_data = open(from_file).read()
# This line defines the "in_data" variable as output of reading the output of opening the "from_file" variable. It condenses the above two lines into a single line.

#out_file = open(to_file, 'w')
#out_file.write(in_data)
open(to_file, 'w').write(in_data)
# This line opens the "to_file" variable, with write mode enabled, and then calls the write command on the output, writing the "in_data" variable into the "to_file" variable.

#out_file.close()
#in_file.close()
# These two close commands no longer need to be called, since "out_file" and "in_file" are no longer opened.

# from_file.close()
# to_file.close()
# Although "from_file" and "to_file" are both opened in the above lines, they apparently do not need to be closed. "AttributeError: 'str' object has no attribute 'close'"

# from sys import argv; script, from_file, to_file = argv; in_data = open(from_file).read(); open(to_file, 'w').write(in_data)
# This line is one of the study drills, attempting (successfully) to condense verbose code into one line. 
# As per JR, short code is not always cleaner code. 
