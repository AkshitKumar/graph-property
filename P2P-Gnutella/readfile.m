T = importdata('p2p-Gnutella04.txt');
i = T(:,1);
j = T(:,2);
v = ones(size(i));
A = sparse(i,j,v);
out_degree = sum(A,2);
N = A ./ out_degree;
save('p2p_pagerank.mat','N');
save('p2p_adjacency.mat','A');