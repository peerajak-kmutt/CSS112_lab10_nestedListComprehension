import numpy as np
"""
n=3
onesk = np.ones((n,n))
print(onesk)
"""

#[[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]

"""
print('We want this matrix\n')
print(np.array([[1.,0.,0.],[1.,1.,0.],[1.,1.,1.]]))
"""
#We want this matrix
#
#[[1. 0. 0.]
# [1. 1. 0.]
# [1. 1. 1.]]
'''
zero_xyindx = [(0,1),(0,2),(1,2)]
xyindx = tuple(zip(*zero_xyindx))
print(xyindx)
print('Notice ((all x),(all y))')
'''
#((0, 0, 1), (1, 2, 2))
#Notice ((all x),(all y))
'''
onesk[xyindx] = 0
print(onesk)
'''
#[[1. 0. 0.]
# [1. 1. 0.]
# [1. 1. 1.]]

def Problem1(n): 
    onesk = np.ones((n,n))
    indx = #Your code here
    xyindx = tuple(zip(*indx))
    onesk[xyindx] = 0
    return onesk
