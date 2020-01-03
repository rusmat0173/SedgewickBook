# Sedgewick, Q1.4.29
# just have to find if a duplicate in an array of numbers
# I did this very efficiently by sorting a list of numbers

array = [1,2,4,6,7,9,1,8,8]

array.sort()
print(array)

for i in range(len(array)-1):
    if array[i] == array[i+1]:
        print('Duplicate exists')
        break

