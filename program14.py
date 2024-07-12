import numpy as np
num = np.array([[2,3,4], [4,5,6], [8,8,9]])
print("original array")
print(num)
print("the array after sorting by row:")
print(np.sort(num))
print("the array after sorting in colmun:")
print(np.sort(num, axis = 0))