import matplotlib.pyplot as plt
import numpy
xpoints = numpy.array([[0, 4],[2,3],[4,8]])
ypoints = numpy.array([[0, 15],[14,11],[3,1]])
data = numpy.array([[19, 14, 6, 36, 3],
                 [12, 12, 1, 32, 1],
                 [18, 25, 0, 33, 0],
                 [13, 19, 0, 32, 5],
                 [12, 14, 0, 33, 0],
                 [16, 14, 7, 30, 0],
                 [11, 18, 5, 31, 2],
                 [17, 11, 3, 46, 7]])
plt.plot(xpoints, ypoints)
plt.title("Matrix data")
plt.show()
x = numpy.arange(0,4*numpy.pi,0.1) 
y = numpy.sin(x)
z = numpy.cos(x)
plt.plot(x,y)
plt.xlabel("Sine Function")
plt.ylabel("Values")
plt.show()
plt.plot(x,z)
plt.xlabel("Cosine Function")
plt.ylabel("Values")
plt.show()
x = numpy.arange(data.shape[0])
dx = (numpy.arange(data.shape[1])-data.shape[1]/2.)/(data.shape[1]+2.)
d = 1./(data.shape[1]+2.)
fig, ax=plt.subplots()
for i in range(data.shape[1]):
    ax.bar(x+dx[i],data[:,i], width=d, label="label {}".format(i))
plt.legend(framealpha=1)
plt.show()
