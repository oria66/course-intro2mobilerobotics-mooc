import numpy as npy

def isOrthogonal(x):

    if(len(x.shape) !=2):
        print("This object might not be an array")
        return False

    if(x.shape[0] != x.shape[1]):
        print("The array is not square")
        return False

    xI = npy.dot(x,x.transpose())

    # Here we do not use array_equals because the floating precision comparison
    return npy.allclose(xI, npy.identity(x.shape[0]))