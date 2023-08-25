'''Q1'''
#Yes, there is a difference in the data types of the variables `list_` and `array_list`.

#The variable `list_` is a Python list, while the variable `array_list` is a NumPy array.

#You can use the `type()` function to print the data types of both variables. Here's the code to do that:

#```python
import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print("Data type of list_:", type(list_))
print("Data type of array_list:", type(array_list))

#When you run this code, it will output:
Data type of list_: <class 'list'>
Data type of array_list: <class 'numpy.ndarray'>

'''Q2'''
import numpy as np

list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_)

print("Data types in list_:")
for item in list_:
    print(type(item))

print("\nData types in array_list:")
for item in array_list:
    print(type(item))

'''Q3'''
'''In the given code, the elements of list_ are strings representing numbers ('1', '2', '3', '4', '5'). When you create array_list without specifying the dtype, the elements of the NumPy array are inferred to be of the data type numpy.str_ (NumPy string).

If you then make the following change:

python
Copy code'''
array_list = np.array(object=list_, dtype=int)
'''This code attempts to convert the elements of list_ from strings to integers using the specified dtype=int. However, since the strings contain non-numeric characters, this will result in a ValueError because the conversion cannot be performed directly.

If you want to convert the string representations of numbers in list_ to integers, you need to remove the single quotes around the numbers in the list_:

python
Copy code'''
list_ = ['1', '2', '3', '4', '5']
array_list = np.array(object=list_, dtype=int)

print("Data types in list_:")
for item in list_:
    print(type(item))

print("\nData types in array_list:")
for item in array_list:
    print(type(item))
'''After this change, both the list_ and the array_list will have elements with the same data type, which is numpy.int64.'''

'''Q4'''
import numpy as np

num_list = [[1, 2, 3], [4, 5, 6]]
num_array = np.array(object=num_list)

# (i) Find the shape of num_array
shape = num_array.shape
print("Shape of num_array:", shape)

# (ii) Find the size of num_array
size = num_array.size
print("Size of num_array:", size)

'''Q5'''
import numpy as np

# Create a 3x3 matrix of zeros
zero_matrix = np.zeros((3, 3))

print("Zero matrix:")
print(zero_matrix)

'''Q6'''
import numpy as np

# Create a 5x5 identity matrix
identity_matrix = np.eye(5)

print("Identity matrix:")
print(identity_matrix)
