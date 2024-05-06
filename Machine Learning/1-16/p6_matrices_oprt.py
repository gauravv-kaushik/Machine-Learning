import numpy 
arr1 = numpy.array([[1,2],[3,4]])
arr2 = numpy.array([[8,7],[6,5]])
print("arr1:", arr1, "\narr2:",arr2)
resadd = numpy.array([[0,0],[0,0]])
ressub = numpy.array([[0,0],[0,0]])
resmul = numpy.array([[0,0],[0,0]])
for i in range(len(arr1)):  
    for j in range(len(arr1[0])):
        resadd[i][j] = arr1[i][j] + arr2[i][j]
        ressub[i][j] = arr1[i][j] - arr2[i][j]
print("Matrix addition :",resadd)
print("Matrix subtraction :",ressub)
for i in range(len(arr1)):
   for j in range(len(arr2[0])):
      for k in range(len(arr2)):
         resmul[i][j] += arr1[i][k] * arr2[k][j]
print("Matrix multiplication: ",resmul)