# splitting array in numpy - it is reverse to joining, it break the array

# array_split()

# split the array in 3 parts:
import numpy as np
x = np.array([1,2,3,4,5,6])
new_x = np.array_split(x, 3)
print(new_x)
'''
OutPut:
[array([1, 2]), array([3, 4]), array([5, 6])]
'''


# split array in 4 parts
import numpy as np
x = np.array([1,2,3,4,5,6])
new_x = np.array_split(x, 4)
print(new_x)
'''
OutPut:
[array([1, 2]), array([3, 4]), array([5]), array([6])]
'''


# print using index
print(new_x[0])  # [1 2]
print(new_x[1])  # [3 4]
print(new_x[2])  # [5]
print(new_x[3])  # [6]


# splitting 2-D array

# it splits this 2-D array into sub 2-D arrays
import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]])
new_x = np.array_split(x, 3)
print(new_x)
'''
Output:
[array([[1, 2, 3],
        [4, 5, 6]]), array([[ 7,  8,  9],
        [10, 11, 12]]), array([[13, 14, 15]])]
'''


# splitting 2-D arrays into three 2-D along with rows
import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
new_x = np.array_split(x, 3, axis=1)
print(new_x)
'''
Output:
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
'''


# alternate solution using hsplit() and its opposite hstack()

# hsplit() - it is same as splitting 2-D array along with rows
import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
new_x = np.hsplit(x, 3)
print(new_x)
'''
Output:
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
'''

# hstack() - `hstack` in numpy is a function that concatenates arrays horizontally, combining them side by side.
import numpy as np
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
new_x = np.hstack(x)
print(new_x)
'''
Output:
[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]
'''


