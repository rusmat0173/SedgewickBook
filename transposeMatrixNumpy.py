# Segdewick, Q1.3.33.
# Transposing square matrices without making another matrix.
# Doing in Python lists is way too much work!
# So done in Numpy, can also be done in csv (other file)

import numpy as np

data = np.loadtxt('matrix.csv', delimiter=',', skiprows=1)
print(data)

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

z = transpose(data)
print(z)