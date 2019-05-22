#! /bin/env python
# coding:utf-8

from random import randrange as rand
import matplotlib.pyplot as plt
import networkx as nx
import pydot

G = {}
N = 10


def gen_graph():
    global G, graph, pos
    G[0] = []
    for i in range(1, N):
        j = 0
        G[i] = []
        while(j == 0):
            for k in range(i):
                if(rand(2) == 0):
                    G[k].append(i)
                    G[i].append(k)
                    j += 1
    graph = nx.Graph()
    for i in G:
        graph.add_node(i)
    for i in G:
        for j in G[i]:
            graph.add_edge(i, j)
    pos = nx.spring_layout(graph, k=5.)


def my_draw_graph():
    nx.draw(graph, pos)
    plt.show()


if __name__ == '__main__':
    gen_graph()
    print pos
    my_draw_graph()
