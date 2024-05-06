import numpy
data1 = numpy.random.randint(10, size=(20))
data2 = numpy.random.randint(20, size=(15))
min = 1000
max = 0
for x in range(0,len(data1)):
    if(data1[x]<min):
        min = data1[x]
print(min)
y = 0
while (y<len(data2)):
    if(data2[y]>max):
        max = data2[y]
    y+= 1
print(y)