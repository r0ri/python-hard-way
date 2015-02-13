# import the argv feature from the sys module
from sys import argv

# unpack argv into two variables
script, filename = argv

# use the open command to open the file provided as an argument
txt = open(filename)

# print the filename
print "Here's your file %r:" % filename
# perform the function read on the file txt 
# with no parameters
print txt.read()

# raw_input prompt for new file
print "Type the filename again:"
file_again = raw_input("> ")

# open provided file
txt_again = open(file_again)

# use read command to print contents
print txt_again.read()

# close the files
txt.close()
txt_again.close()