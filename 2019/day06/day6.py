import networkx as nx
with open('input.txt','r') as f:
    edges = [x.split(')') for x in f.read().split('\n')]
    G = nx.Graph()
    G.add_edges_from(edges)
print("PART1:",sum(nx.shortest_path_length(G,'COM').values()))
print("PART2:",nx.shortest_path_length(G,'YOU','SAN') - 2) # remove source and edge