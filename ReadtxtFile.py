"""
Excellent resources:
https://www.w3schools.com/python/python_file_open.asp

A text file is a poor way to read-in a matrix! (Where matrix is a nested Python list.)
"""
# simple open file object and get out a string
f = open('matrix.txt')
for line in f:
    print(line)
print(type(line), '\n')

# simple print, for file with several lines. Good practice to close file
f = open("matrix.txt", "r")
for x in f:
  print(x)
f.close()



