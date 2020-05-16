import numpy as npy

### Item A
def diffdrive(x, y, theta, v_l, v_r, t, l):
    
    if(l==0):
        print("The longitude beetwen wheels can not be 0")
        return
    
    if(v_r==v_l):
        R = 0
    else:
        R = (l/2)*((v_l + v_r)/(v_r - v_l))

    iccX = x - R * npy.sin(theta)
    iccY = y + R * npy.cos(theta)

    omega = (v_r - v_l)/l

    A = npy.array([[npy.cos(omega*t), -npy.sin(omega*t), 0], [npy.sin(omega*t), npy.cos(omega*t), 0], [0,0,1]])

    v1 = npy.array([x-iccX,y-iccY,theta])    
    v2 = npy.array([iccX,iccY,omega*t])

    res = A.dot(v1) + v2

    x_n = res[0]
    y_n = res[1]
    theta_n = res[2]

    return x_n, y_n, theta_n