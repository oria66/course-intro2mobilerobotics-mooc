import numpy as npy

def homegenousMatrix(x, y, theta):
    return npy.array([[npy.cos(theta), -npy.sin(theta), x], [npy.sin(theta), npy.cos(theta), y], [0,0,1]])