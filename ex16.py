# Part 1 - Using argv and multiple write functions

"""
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
"""

# Part 2 - Using single write function call and reading the new file after write has completed

filename = raw_input("Please enter a filename. ")
print "We're going to erase the contents of the file %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Tuncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

data = line1 + "\n" + line2 + "\n" + line3 + "\n"
print "I'm going to write these to the file."

target.write(data)
target.close()

target = open(raw_input("filename: "))

print target.read()

print "Closing the file."
target.close()
