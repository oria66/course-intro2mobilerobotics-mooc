import numpy as npy
import matplotlib.pyplot as plt
import orthogonalDetection as orto

### Item A
#A=no A!=At
#B=yes eigenvalues lambda1=0.7, lambda2=0.05

### Item B
#u=3 greatest value

### Item C-D
mymatrix = 1./3.*npy.array([[2,2,-1],[2, -1, 2], [-1, 2, 2]])

print(orto.isOrthogonal(mymatrix))
