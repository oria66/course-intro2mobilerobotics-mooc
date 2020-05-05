import numpy as npy
import matplotlib.pyplot as plt

### item E
npy.random.seed(1)

### item A
u = 5.0  		#mean
sigma = 2.0		#standard deviation
myListA = npy.random.normal(u, sigma, 100000)
print(myListA)

### item B
myListB = npy.random.uniform(0, 10, 100000)
print(myListB)

### item C
meanA = npy.mean(myListA)
meanB = npy.mean(myListB)
#Its expected that both means are equal, 'cause both distributions are simetric with equal mean
print(meanA)
print(meanB)

stdA = npy.std(myListA)
stdB = npy.std(myListB)
#Its expected that standard deviation differs
print(stdA)
print(stdB)

### item D
plt.hist(myListA, 40, density=True)
plt.hist(myListB, 40, density=True)
plt.show()