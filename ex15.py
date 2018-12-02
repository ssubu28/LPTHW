# Importing argv function from sys module
from sys import argv

# Unpacking the 2 arguments into variables script and filename
script,filename = argv

# Opening a file using its name and using a variable to hold the file (file pointer)
txt = open(filename)

# Printing a smaple line before file contents are printed
print "Here's your file %r:" % filename
# Printing file contents using read fucntion which can be used on a file pointer
print txt.read()

# Indicating that we are about to open a file again and print it
print "Type the filename again:"
# Reading user input to obtain filename
file_again = raw_input("> ")

# Opening file and holding the contents in txt_again variable (file pointer)
txt_again = open(file_again)

# Printing contents of the file using variable holding file contents
print txt_again.read()


txt.close()
txt_again.close()
