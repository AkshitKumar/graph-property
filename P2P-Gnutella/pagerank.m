% Set the parameters
MAX_ITER = 100000;
% Load the saved PageRank Update matrix
L = load('p2p_pagerank.mat');
N = L.N;
[row,col] = size(N);
s = 0.85;
V = row;
x0 = (1 - s)/ V * ones([1,V]);
old = x0;
for k = 1:MAX_ITER
    new = x0 + s * old * N;
    old = new;
end