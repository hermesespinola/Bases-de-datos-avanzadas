from __future__ import division

from graph import *
from pprint import pprint

# damping factor
default_d = 0.85
# iterative error threashold
default_epsilon=2e-8

def page_rank(graph, I, C, PR, d=default_d, epsilon=default_epsilon):
    new_PR = {}
    for uid, node in graph.nodes.iteritems():
        new_PR[uid] = (1-d) + d * sum(map(lambda adj: PR[adj] / C[adj], I[uid]))
        i_err = map(lambda p: abs(p[0] - p[1]) / p[0], zip(new_PR.values(), PR.values()))
        if all(map(lambda err: err < epsilon, i_err)):
            PR = new_PR
            break
        PR.update(new_PR)
    return PR

if __name__ == '__main__':
    graph, start = Graph.from_csv('oatmeal_nodes.csv', 'oatmeal_edges.csv')
    # number of outgoing links (or votes) of each node
    C = {uid: len(node.adj) for uid, node in graph.nodes.iteritems()}
    # initial page rank values
    PR = {uid: 0 for uid, node in graph.nodes.iteritems()}

    # dict of incoming nodes to some other node
    I = {}
    for uid, node in graph.nodes.iteritems():
        for outgoing in node.adj:
            if outgoing not in I:
                I[outgoing] = [uid]
            else:
                I[outgoing].append(uid)

    def get_node_str(n):
        return "{0}".format(graph.nodes[n])

    PR = page_rank(graph, I, C, PR)
    max_uid, max_rank = max(PR.items(), key=lambda p: p[1])
    print "max rank node:\n", max_uid, graph.nodes[max_uid]
    print "rank:", max_rank, '\n'
    print "=================== voted for ==================="
    for n in map(get_node_str, graph.nodes[max_uid].adj):
        print n
    print "=================== voted by ==================="
    for n in map(get_node_str, I[max_uid]):
        print n

    min_uid, min_rank = min(PR.items(), key=lambda p: p[1])
    print "min rank node:", min_uid, graph.nodes[min_uid]
    print "rank:", min_rank
    print "=================== voted for ==================="
    for n in map(get_node_str, graph.nodes[min_uid].adj):
        print n
    print "=================== voted by ==================="
    for n in map(get_node_str, I[min_uid]):
        print n
