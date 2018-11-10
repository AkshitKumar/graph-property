T = importdata('Email-Enron.txt');
i = T(:,1);
j = T(:,2);
v = ones(size(i));
A = sparse(i,j,v);
out_degree = sum(A,2);
N = A ./ out_degree;
save('enron_email_pagerank.mat','N');
save('enron_email_adjacency.mat','A');