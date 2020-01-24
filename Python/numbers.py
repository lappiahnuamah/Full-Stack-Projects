x = 'item one: {}, item two:{} '.format('sheep', 'goat');
print(x)

y= 'item one: {y}, item two:{y} '.format(x= 'sheep', y = 'goat');
print(y)

name = 'Heahoiwlwwi'
print(name[::2])

# List comprehension
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)

