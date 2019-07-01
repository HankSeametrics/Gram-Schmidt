#This is a program written to explore the functionality of git by building a program from scratch
import numpy as np
import time

#Useful operators
def projUV(U,V):
    vu=np.dot(V,U)
    uu=np.dot(U,U)
    proj = (float(vu)/uu)*U
    time.sleep(30)
    return proj