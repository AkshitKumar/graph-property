import numpy as np
import matplotlib.pyplot as plt

V = 36692 # number of nodes in the graph
A = np.zeros((V,V)) # adjacency matrix of the graph

with open('Email-Enron.txt') as f:
	lines = f.readlines()
	
for line in lines:
	line = line.rstrip()
	i,j = line.split('\t')
	A[int(i)-1,int(j)-1] = 1

out_degree_vector = A.sum(axis = 1)
in_degree_vector = A.sum(axis = 0)
mean_out_degree = np.mean(out_degree_vector)
mean_in_degree = np.mean(in_degree_vector)

ind = np.where(out_degree_vector == 0)

N = A / out_degree_vector[:,None]
print np.mean(N.sum(axis = 1))
'''
plt.figure()
plt.plot(np.arange(1,V+1), out_degree_vector)
plt.figure()
plt.plot(np.arange(1,V+1), in_degree_vector)
plt.show()
'''

# Perform Scaled PageRank Update
s = 0.85
N_tilde = s * N + (1 - s) * (1.0 / V) * np.ones((V,V))
N_tilde_transpose = N_tilde.transpose()
r = (1/V) * np.ones((V,1))
for i in range(10):
	r = N_tilde_transpose * r
	print i

print r