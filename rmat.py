import numpy as np

v = np.arange(0,4)
random_vector = np.random.exponential(1,4)
prob = random_vector/ (np.sum(random_vector))

n = 10
V = 2 ** n

def get_coordinates():
	P = 0 
	Q = (V ** 2) - 1
	s = np.random.choice(v, 10, p = prob)
	for i in s:
		T = int(((Q - P + 1)/4.0))
		P = P + T * i
		Q = P + T
	y = int(P / V)
	x = P - (y * V)
	return x,y

def generate_graph(V,type):
	if type == 's':
		E = int(3.0 * V / 4.0)
	elif type == 'd':
		E = int(3.0 * V * (V - 1) / 4.0)
	A = np.zeros((V,V))
	for i in range(E):
		x,y = get_coordinates()
		A[x,y] = 1
		A[y,x] = 1
	for i in range(V):
		A[i,i] = 0
	if type == 's':
		np.save('sparse_rmat.npy', A)
	elif type == 'd':
		np.save('dense_rmat.npy', A)
	return A

generate_graph(V,'s')
generate_graph(V,'d')