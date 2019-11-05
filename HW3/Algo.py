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


# Some code taken from https://gist.github.com/kachayev/5990802

def dijkstra1(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = hq.heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                c = float(c)
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    hq.heappush(q, (next, v2, path))

    return float("inf")


def dijkstra(edges, from_node, to_node):

    graph = defaultdict(list)
    for f, t, c in edges:
        graph[f].append((c, t))

    queue = [(0, from_node, ())]
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
                hq.heappush(queue, (cost + c, node2, path))

        if node1 == to_node:
            return cost, path

    return -1


def dijkstraTwo(graph, initial):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}

    nodes = set(graph.nodes)

    while nodes and h:
        current_weight, min_node = hq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = hq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, v]
            if v not in visited or weight < visited[v]:
                visited[v] = weight
                hq.heappush(h, (weight, v))
                path[v] = min_node

    return visited, path


edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 160),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

print(dijkstra(results, '0', '2'))
for i in range(1, int(nodes[0])):
    costs, paths = dijkstra(results, '0', str(i))
    print("shortest path to node " + str(i) + " is " + str(paths) + "Cost: " + str(costs))
