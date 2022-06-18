import numpy as np

# a = numpy.array([[1,2,3],[4,5,6]], dtype=complex)
# print(a)

# a = numpy.array([[1,2,3],[5,6,7],[9,10,11],[12,13,14]])
#
# print(a.ndim)


# arr = numpy.empty((3,2), dtype = int, order='F')
# print(arr)


# arr = numpy.ones((3,2), dtype = int, order='C')
# print(arr)

# l=[1,2,3,4,5,6,7]
# a = numpy.asarray(l);
# print(type(a))
# print(a)\]

#
# l = 'hello world'
# print(type(l))
# a = numpy.frombuffer(l, dtype = "S1")
# print(a)
# print(type(a))

# l=(1,2,3,4,5,6,7)
# a = np.asarray(l);
# print(type(a))
# print(a)
#
#
# l=[[1,2,3,4,5,6,7],[8,9]]
# a = np.asarray(l)
# print(type(a))
# print(a)

# list = [0,2,4,6]
# it = iter(list)
# x = np.fromiter(it, dtype = complex)
# print(x)
# print(type(x))


# arr = np.arange(10,100,5)
# print(arr)

# arr = np.linspace(10, 20, 5, dtype=complex)
# print("The array over the given range is ",arr)

# arr = np.logspace(10, 20, endpoint = True)
# print("The array over the given range is ",arr)

# a = np.array([[1,2],[3,4],[5,6]])
# b = np.array([[1,2,3],[4,5,6]])
#
# ans = np.mat(b) * np.mat(a)
# print(ans)
#
# a = [[1,2],[3,4],[5,6]]
# b = [[1,2,3],[4,5,6]]
#
# ans = np.mat(b) * np.mat(a)
# print(ans)

# arr = np.logspace(10, 20, num = 5,base = 2, endpoint = True)
# print("The array over the given range is ",arr)
#
# a = np.array([1,2,3,4])
# b = np.array([[2,4,6,8],[1,2,3,4],[2,4,5,6]])
# print("\nprinting array a..")
# print(a)
# print("\nprinting array b..")
# print(b)
# print("\nAdding arrays a and b ..")
# c = a + b
# print(c)

# a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
# print("Printing array:")
# print(a)
# print("Iterating over the array:")
# for x in np.nditer(a):
#     print(x,end=' ')

# a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
# # print("Printing the array:")
# # print(a)
# print("Printing the transpose of the array:")
# at = a.T
# print(at)

# a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
# print("Printing the array:")
# print(a)
# print("Printing the transpose of the array:")
# at = a.T
# print(at)
#
# # this will be same as previous
# for x in np.nditer(at):
#     print("Iterating over the array:")
#     for x in np.nditer(a):
#         print(x, end=' ')

# a = np.array([[1, 2, 3, 4], [2, 4, 5, 6], [10, 20, 39, 3]])
#
# print("\nPrinting the original array:\n")
#
# print(a)
#
# print("\nIterating over the modified array\n")
#
# for x in np.nditer(a, op_flags=['readwrite']):
#     x = 3 * x
#     print(x, end=' ')


# arr = np.array([20], dtype=np.uint8)
# print("Binary representation:", np.binary_repr(20, 8))
# print("Binary representation: ", np.binary_repr(235, 8))
#

# print("left shift of 20 by 3 bits", np.right_shift(20, 3))
#
# print("Binary representation of 20 in 8 bits", np.binary_repr(20, 8))
#
# print("Binary representation of 160 in 8 bits", np.binary_repr(160, 8))


#
# print("Concatenating two string arrays:")
# print(np.char.add(['welcome','Hi'], [' to Javatpoint', ' read python'] ))
#
# print('concatenations')
# print(np.char.add(['hey','Hi'],['how are you', 'I am good']))
#
#
# print(np.char.multiply('hii', 4))
#
#
# print(np.char.center('world',25,'+'))
#
# print(np.char.capitalize('world od war'))
#
# print(np.char.title('world od war'))
#
# print(np.char.lower('WORLD of WAR'))
#
#
# print(np.char.split("Welcome To Javatpoint"),sep = " ")
#
# print(np.char.splitlines("Welcome To Javatpoint"))

# str = "Welcome to Javatpoint"
# print("Original String:",str)
# print(np.char.replace(str, "Welcome to","www."))
#
# enstr = np.char.encode("welcome to javatpoint")
# dstr =np.char.decode(enstr, 'cp500')
# print(enstr)
# print(dstr)

# arr = np.array([0, 30, 60, 90, 120, 150, 180])
# print("\nThe sin value of the angles",end = " ")
# print(np.sin(arr * np.pi/180))
# print("\nThe cosine value of the angles",end = " ")
# print(np.cos(arr * np.pi/180))
# print("\nThe tangent value of the angles",end = " ")
# print(np.tan(arr * np.pi/180))


c = np.arra([[20, 24], [21, 23]])

print(np.where(c > 20))

import cv2

a = cv2.imread()