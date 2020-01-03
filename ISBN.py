# Sedgewick, Q1.3.33
# interesting problem as it mixes integers and strings
import sys

cl = sys.argv[1]
# cl is command line input. put numbers in without '...'

# add tenth digit to the right, this one gets over written with the check sum
cl_2 = cl + '0'
total = 0
order = len(cl_2)

# this is the (surprisingly short) guts of the matter, outputing the total
for i in range(order, 0, -1):
    total += i * int(cl_2[10 - i])

# now need to do the mod11 part
checksum = 11 - total % 11

# overwrite last letter in string with checksum. N.B. strings are immutable
isbn = cl_2[:order - 1] + str(checksum)
print(isbn)