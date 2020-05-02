import myfirstscript
import numpy
import matplotlib.pyplot as plt

myListX=list(range(0, 360, 1))
myListY=[]

print(myListX)

for i in myListX:
	myListY.append(myfirstscript.mathFunction(numpy.deg2rad(myListX[i])))

plt.plot(myListX, myListY)
plt.ylabel('Function')
plt.savefig('image.png')