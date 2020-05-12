import numpy as npy
import matplotlib.pyplot as plt
import math
import os
import homogenous

os.chdir("/home/homero/course-intro2mobilerobotics-mooc/lecture_01/ex3/")

### Item A
scan = npy.loadtxt('laserscan.txt')
angle = npy.linspace(-npy.pi/2, npy.pi/2, npy.shape(scan)[0], endpoint='true')

scanX2 = npy.multiply(scan,npy.cos(angle))
scanY2 = npy.multiply(scan,npy.sin(angle))

#plt.plot(scanX2, scanY2, 'ro')
#plt.gca().set_aspect('equal', adjustable='box')
#plt.show()

### Item B
# I think that if the scanner is single return it can't be two points in the same vision path. However if the scanner is Doble Return this is completely normal.

### Item C
#Homogenous Matrice form World to Robot
theta01 = npy.pi/4
x01 = 1.0
y01 = 0.5
A01 = homogenous.homegenousMatrix(x01, y01, theta01)

#Homogenous Matrice form Robot to Laser
theta12 = npy.pi
x12 = 0.2
y12 = 0.0
A12 = homogenous.homegenousMatrix(x12, y12, theta12)

vect = npy.array([scanX2,scanY2,npy.ones(361)])

A = A01.dot(A12.dot(vect))

Alaser = A01.dot(npy.array([x12*npy.cos(theta12),y12*npy.sin(theta12),1]))

plt.plot(A[0,:], A[1,:], 'ro')
plt.plot(x01, y01,'*')
plt.plot(Alaser[0], Alaser[1],'bo')
plt.gca().set_aspect('equal', adjustable='box')
plt.show()