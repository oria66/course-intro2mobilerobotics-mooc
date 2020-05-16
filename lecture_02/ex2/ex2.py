import numpy as npy
import differentialDrive

### Item B
l = 0.5

x_init = 1.5
y_init = 2.0
theta_init = npy.pi/2

#(a)
c1 = differentialDrive.diffdrive(x_init, y_init, theta_init, 0.3, 0.3, 3, l)
print(c1)

#(b)
c2 = differentialDrive.diffdrive(c1[0], c1[1], c1[2], 0.1, -0.1, 1, l)
print(c2)

#(c)
c3 = differentialDrive.diffdrive(c2[0], c2[1], c2[2], 0.2, 0, 2, l)
print(c3)
