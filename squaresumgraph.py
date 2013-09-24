import networkx as nx
from scipy import *

def issquare(n):
    return int(sqrt(n)) == sqrt(n)

for N in range(30):
    G = nx.Graph()
    G.add_nodes_from(range(1,N+1))
    for i in G.nodes():
	for j in G.nodes():
	    if issquare(i+j):
		G.add_edge(i,j)

    candidates = {tuple(p)
		  for i in G.nodes()
		  for j in filter(lambda k: k>i, G.nodes())
		  for p in nx.all_simple_paths(G,source=i,target=j)
		  if len(set(p)) == G.order()}
    if len(candidates) > 0:
	print N, list(candidates)[0]
