#This is a program written to explore the functionality of git by building a program from scratch
import numpy as np

def projUV(U,V):
    vu=np.inner(V,U)
    uu=np.inner(U,U)
    proj = (vu/uu)*U
    return proj
