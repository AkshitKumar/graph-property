import numpy as np
import matplotlib.pyplot as plt

V = 10875 # number of nodes in the graph
A = np.zeros((V,V)) # adjacency matrix of the graph

with open('p2p-Gnutella04.txt') as f:
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