import numpy
from numpy import savetxt
arr = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
l = len(arr)
print(arr.shape)
print("Length of array: ",l)
file = open("data.txt","r")
print(file.readline())
file.close()
file = open("data.txt","w")
savetxt('data1.txt', arr, delimiter=',')
file.close()