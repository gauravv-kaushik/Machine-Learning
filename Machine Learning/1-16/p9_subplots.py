import matplotlib.pyplot as plt
import numpy 
x = numpy.arange(0.0, 2.0, 0.01)
y = 1 + numpy.sin(2 * numpy.pi * x)
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)
ax1.plot(x, y, color="orange")
ax2.plot(x, y, color="green")
ax3.plot(x, y, color="blue")
ax4.plot(x, y, color="magenta")
ax5.plot(x, y, color="black")
ax6.plot(x, y, color="red")
plt.show()