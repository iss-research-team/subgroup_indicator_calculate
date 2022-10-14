import numpy as np
import networkx as nx

# arr = [1, 1, 4]
# print(np.std(arr,ddof=0))

pp = list()
nodes_index_1 = [1, 2, 3, 5, 9]
edges_1 = [(1,2), (5,3), (2,3)]
pp.append(nx.Graph())
pp[0].add_nodes_from(nodes_index_1)
pp[0].add_edges_from(edges_1)

tt = nx.degree(pp[0])
degree_dict = dict(tt)
print(degree_dict)
for neighber in nx.all_neighbors(pp[0],2):
    print(neighber)

# dict_ = {1:2,4:5}
# print(list(dict_.values()))