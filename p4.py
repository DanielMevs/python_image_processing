import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

def convert_bw(matrix):#takes an image ndarry with shape (height, width, 3), dtype
    total = matrix[:,:,0] + matrix[:,:,1] + matrix[:,:,2]
    total = total/3
    return np.fromfunction(lambda x,y,z: total[x,y] , matrix.shape(), dtype=np.uint )
    #np.uint8
    #returns
