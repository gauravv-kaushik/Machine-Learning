import numpy 
arr = numpy.array([[-1, -2, 3, 4],
              [5, 6, -7, 8], 
              [9, -10, 11, -12]])
print("original matrix: ",arr)
print("Absolute matrix value: ",numpy.absolute(arr))
print("Negative matrix value: ",numpy.negative(arr))
ar = numpy.delete(arr,1,0)
ac = numpy.delete(arr,1,1)
print("Array after 2nd row deleted: ",ar)
print("Array after 2nd column deleted: ",ac)
nr = numpy.array([1,3,6,7])
nc = numpy.array([[4],[5],[2]])
print("Array after adding column: ",numpy.append(arr, nc, axis=1))
print("Array after adding row: ",numpy.r_[arr,[nr]])
print("Minimum and maximum value in the matrix: ",numpy.min(arr),numpy.max(arr))
print("Sum of all elements in the matrix: ",numpy.sum(arr))