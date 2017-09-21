import pandas as pd
from graph import *

if __name__ == '__main__':
    graph, start = Graph.from_csv('oatmeal_nodes.csv', 'oatmeal_edges.csv')
    dfs_graph = graph.dfs(start)
    bfs_graph = graph.bfs(start)
    print "graph vs dfs graph:", len(graph.nodes), len(dfs_graph.nodes), graph.nodes == dfs_graph.nodes
    print "graph vs bfs graph:", len(graph.nodes), len(bfs_graph.nodes), graph.nodes == bfs_graph.nodes
