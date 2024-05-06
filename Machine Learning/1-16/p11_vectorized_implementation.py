import numpy
d1 = numpy.array([[1,2,6],[5,6,2],[0,4,1]])
d2 = numpy.array([[6,3,1],[0,1,0],[5,7,7]])
print("Original matrices: \n",d1,"\nand\n",d2)
print("Transpose of matrices:\n ", d1.transpose(),"\nand\n", d2.transpose())
print("Matrix multiplication:\n ", numpy.multiply(d1,d2))
print("Matrix addition:\n ", numpy.add(d1,d2))
print("Matrix subtraction:\n ", numpy.subtract(d1,d2))