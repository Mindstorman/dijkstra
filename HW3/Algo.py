import csv
import math
import sys
import heapq as hq
from collections import defaultdict

results = []
nodes = 0
distanceList = []
costList = []

with open('data.dat', newline='') as f:
    reader = csv.reader(f, delimiter=' ')
    firstLine = True
    for row in reader:
        if firstLine:
            firstLine = False
            nodes = row
        else:
            results.append(tuple(row))


# Inspiration https://gist.github.com/kachayev/5990802

def dijkstra(edges, from_node, to_node):

    graph = defaultdict(list)
    for f, t, c in edges:
        graph[f].append((c, t))
        graph[t].append((c, f))


    queue = [(0.0, from_node, ())]
    visited = set()
    distance = {from_node: 0}


    while queue:
        (cost, node1, path) = hq.heappop(queue)
        if node1 in visited:
            continue

        visited.add(node1)
        path += (node1,)

        for c, node2 in graph.get(node1, ()):
            c = float(c)
            if node2 in visited:
                continue

            if node2 not in distance or cost + c < distance[node2]:
                distance[node2] = cost + c
                hq.heappush(queue, (float(cost + c), node2, path))

        if node1 == to_node:
            return cost, path

    return -1


for i in range(1, int(nodes[0])):
    costs, paths = dijkstra(results, '0', str(i))

    if ( costs >= 0):
        output = ""
        for p in paths:
            output += str(p) + '->'

        output = output[:-2]
        
    else:
        costs = "N/A"
        paths = "N/A"
    
    print("shortest path to node " + str(i) + " is " + str(output) + " with cost: " + str(costs))
