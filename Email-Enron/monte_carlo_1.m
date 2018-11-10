% Load the adjacency matrix of the graph
L = load('enron_email_adjacency.mat');
N = load('neighbours.mat');
A = L.A;
Neighbors = N.M;
[row, col] = size(A);
V = row;
WALK_LEN = 10000000;
NUM_WALK = 10;
p = zeros([V,1]);

for j = 1:NUM_WALK
    current_node = randi(V);
    for k = 1:WALK_LEN
        p(current_node) = p(current_node) + 1; 
        neighbors = cell2mat(Neighbors(current_node));
        %neighbors = find(A(current_node, :) == 1);
        current_node = randsample(neighbors,1);
    end
end

p = p / (WALK_LEN * NUM_WALK);