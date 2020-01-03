# use of csv to read in a file. N.B. is still a set of strings
import csv

def read_file(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        # get header from first row
        headers = next(reader)
        # get all the rows as a list
        data = list(reader)
    return data

def string2num(aList):
    new_matrix = []
    for item in aList:
        matrix_row = []
        for element in item:
            matrix_row.append(int(element))
        new_matrix.append(matrix_row)
    return new_matrix

def transpose(matrix):
    order = len(matrix[0])
    for i in range(order):
        for j in range(order):
            if j > i:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
    return matrix

string_matrix = read_file('matrix.csv')
y = string2num(string_matrix)
print(y)
print(type(y[0][0]))

z = transpose(y)
print(z)


