import pandas as pd
from graph import *

if __name__ == '__main__':
    graph, start = Graph.from_csv('oatmeal_nodes.csv', 'oatmeal_edges.csv')
    dfs_graph = graph.dfs(start)
    bfs_graph = graph.bfs(start)

    print "======================== GRAPH ======================================"
    print_graph(graph)
    print "====================== DFS GRAPH ===================================="
    print_graph(dfs_graph)
    print "====================== BFS GRAPH ===================================="
    print_graph(bfs_graph)

    print "A random node:"
    print "Graph", graph.get_node(48261298954)
    print "dfs", dfs_graph.get_node(48261298954)
    print "bfs", bfs_graph.get_node(48261298954)
