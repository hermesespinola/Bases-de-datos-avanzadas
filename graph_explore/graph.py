import copy
import sets
import pandas as pd
import Queue
from pprint import pprint

tautology = lambda n: True
identity = lambda n: n

class Node(object):
    """docstring for Node."""
    def __init__(self, data = None, adj = []):
        self.data = data
        self.adj = adj

    def add_adjacent(self, uid):
        self.adj.append(uid)

    def add_adjacents(self, nodes_uid):
        self.adj += nodes_uid

    def __str__(self):
        return "{\n\t" + str(self.data).replace('\n', '\n\t') + "\n} -> " + str(self.adj)

class Graph(object):
    """Adjacency list graph."""
    def __init__(self, nodes = {}):
        self.nodes = nodes

    def add_node(self, uid, node):
        self.nodes[uid] = node

    @staticmethod
    def create_node(row):
        uid = row[0]
        node = Node(data = row[1])
        return uid, node

    def add_nodes(self, ids, nodes):
        self.nodes.update({uid: node for uid, node in zip(uid, node)})

    def get_node(self, uid):
        return self.nodes[uid]

    @staticmethod
    def from_csv(nodes_path, edges_path):
        nodes = pd.DataFrame.from_csv(nodes_path)
        edges = pd.DataFrame.from_csv(edges_path)

        nodes = dict(map(Graph.create_node, nodes.iterrows()))
        for node1, node2 in edges.itertuples():
            nodes[node1].add_adjacent(node2)
        start_uid = nodes.iterkeys().next()
        return Graph(nodes), start_uid

    def dfs(self, start_uid, node_filter=tautology, node_map=identity):
        result = Graph()
        stack = [start_uid] if node_filter(self.nodes[start_uid]) else []
        visited = set()

        while stack:
            current_uid = stack.pop()
            current = self.nodes[current_uid]
            if not current_uid in visited:
                new_adj = [uid for uid in current.adj if node_filter(self.nodes[uid]) and not uid in visited]
                new_node = node_map(copy.deepcopy(current))
                new_node.adj = new_adj
                visited.add(current_uid)
                stack += new_adj
                result.add_node(current_uid, new_node)

        return result

    def bfs(self, start_uid, node_filter=tautology, node_map=identity):
        result = Graph()
        queue = Queue.Queue()
        if node_filter(self.nodes[start_uid]):
            queue.put(start_uid)
        visited = set()

        while not queue.empty():
            current_uid = queue.get()
            current = self.nodes[current_uid]
            if not current_uid in visited:
                new_adj = [uid for uid in current.adj if node_filter(self.nodes[uid]) and not uid in visited]
                new_node = node_map(copy.deepcopy(current))
                new_node.adj = new_adj
                visited.add(current_uid)
                for uid in new_adj:
                    queue.put(uid)
                result.add_node(current_uid, new_node)

        return result

def print_graph(graph):
    for uid, node in graph.nodes.iteritems():
        print uid, node, '\n'
