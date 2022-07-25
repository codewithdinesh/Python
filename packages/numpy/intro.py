from math import ceil, floor
import numpy as np

print(floor(3.9))

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])


# # Printing type of arr object
# print("Array is of type: ", type(arr))

# # Printing array dimensions (axes)
# print("No. of dimensions: ", arr.ndim)

# # Printing shape of array
# print("Shape of array: ", arr.shape)

# # Printing size (total number of elements) of array
# print("Size of array: ", arr.size)

# # Printing type of elements in array
# print("Array stores elements of type: ", arr.dtype)


arr = np.array([[1, 2, 3], [4, 5, 6]])

arr2 = np.array([[1, 2, 1], [1, 4, 2]])

print("Array1: \n", arr)
print("Array2: \n", arr2)


# addition
print("Addition: \n", arr+arr2)

# addition with numpy function of numpy module
print("Addition with numpy.add()", np.add(arr, arr2))

# substraction
print("substraction: \n", arr-arr2)

# with subtract()
print("substraction with numpy.subtract():", np.subtract(arr, arr2))

# multiplication
print("multiplication: \n", arr*arr2)



# divition
print("Division: \n", arr/arr2)

# division with numpy.division()
print("Division with numpy.divide()\n", np.divide(arr, arr2))


# random with numpy
print(np.random.randint(10,30))
