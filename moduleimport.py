# this file uses demo.py file
import demo
import numpy as np
# import demo as d  # we can name another file as we wanted and do just the same work nothing will change

'''a = demo.add(2, 3)
print(a)'''


'''l1 = [10, 20, 30]
l2 = [12, 13, 14]
l3 = 5
print(l1+l2)
print(l1*l3)'''


'''a = np.array([12, 13, 14])
b = np.array([10, 20, 30])
print(type(a)) # it will tell ndarray=n dimentional array
print(a+b)
print(a*b)'''

arr = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
arr1 = np.array([10, 220, 330, 440, 550, 660])
print(type(arr))
print(arr1[0:2])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)
