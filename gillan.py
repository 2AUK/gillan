#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


# Define some grid
radius = 20.48
npts = 8192
nbasis = 4
dx = radius/npts
i = np.arange(0.5, npts)
x = np.arange(0.5, npts) * dx
nodes = np.linspace(1, (npts/2)+1, num=nbasis)
print(nodes)
nodes = np.round(nodes).astype(int)
#nodes = np.asarray([2, 4, 6, 8])
i_nodes = i[nodes]
print(i_nodes)
# Define nodes along a subset of the grid for the roof functions
P = np.zeros((npts, nbasis), dtype=np.float64)
print(i)
P[0, 0] = 1
for idx in range(1, npts):
    print(idx)
    if 0.0 <= i[idx] <= i_nodes[0]:
        P[idx, 0] = (i_nodes[0] - i[idx])/(i_nodes[0])

for a in range(1, nbasis):
    for idx in range(0, npts):
        if i_nodes[a-2] <= i[idx] <= i_nodes[a-1]:
            P[idx, a] = (i[idx] - i_nodes[a-2])/(i_nodes[a-1] - i_nodes[a-2])
        elif i_nodes[a-1] <= i[idx] <= i_nodes[a]:
            P[idx, a] = (i_nodes[a] - i[idx])/(i_nodes[a] - i_nodes[a-1])

R = np.zeros((nbasis, nbasis), dtype=np.float64)
Pa = P.copy()
Pb = P.copy()
for a in range(nbasis):
    for b in range(nbasis):
        R[a, b] = (Pa[a] * Pb[b]).sum()
B = np.linalg.inv(R)
Q = np.zeros_like(P)
for a in range(nbasis):
    for b in range(nbasis):
        Q[:,a] = (B[a,b] * P[:,b])

print(R)
print(B)
print(Q)
print(Q.shape)
for a in range(nbasis):
    plt.plot(i, Q[:,a])
plt.show()
kron = np.zeros_like(R)
for a in range(nbasis):
    for b in range(nbasis):
        kron[a,b] = (Q[:,a] * P[:,b]).sum()

print(kron)
