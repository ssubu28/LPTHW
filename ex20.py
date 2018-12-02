# Calling argv module from sys package
from sys import argv

#Unpacking arguments from argv
script, input_file = argv

# Function definitions
def print_all(f):
    print f.read()

# seek resets the file pointer to the start of the file. Index 0 indicates start of file
def rewind(f):
    f.seek(0)

# Added a comma to test the extra /n which is added by the readline function
def print_a_line(line_count, f):
    print line_count, f.readline(),

# Creatign a file object by opening file
current_file = open(input_file)

print "First let's print the whole file:\n"

# Calling function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# Setting variable and printing each line of file from beginnning
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_file.close()
