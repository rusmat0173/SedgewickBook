# Segdewick, Q1.3.33.
# Transposing square matrices without making another matrix.
# Doing in Python lists is way too much work!
# So done in csv, can also be done in Numpy (other file)

import csv

# read csv file and turn into a list (strings). Note header in file is blank row
def read_file(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get header from first row
        headers = next(reader)
        # get all the rows as a list
        data = list(reader)
    return data

# turns list of strings into numbers (can be int or float)
def string2num(aList):
    new_matrix = []
    for item in aList:
        matrix_row = []
        for element in item:
            matrix_row.append(int(element))
        new_matrix.append(matrix_row)
    return new_matrix

# transpose matrix (nested list)
def transpose(matrix):
    order = len(matrix[0])
    for i in range(order):
        for j in range(order):
            if j > i:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    return matrix

# action below here
string_matrix = read_file('matrix.csv')
y = string2num(string_matrix)
print(y)
print(type(y[0][0]))

z = transpose(y)
print(z)