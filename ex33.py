"""
i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
"""

# Using functions, variables and for loops
def funwhile(lim):
    nums = []
    for i in range(lim):
        nums.append(i)
    return nums

lim = raw_input("> ")
print "The numbers: "

numbers = funwhile(int(lim))

print numbers
