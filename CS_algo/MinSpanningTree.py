import math
import numpy as np

def dijkstra(graph, d, a):
    parent = {}
    dist = {}
    
    # init
    for p in nodes(graph):
        parent[p], dist[p] = None, math.inf
    dist[d]=0
    
    frontier = [d]
    
    ############### TODO : complete code #####################
    while len(frontier) > 0 :
        min_node = frontier.pop(np.argmin([dist[x] for x in frontier]))
        
        if min_node == a: # we reach the arrival
            break       

        for y in neighbors(graph, min_node):
            # if (first time reached)
            if dist[y] == math.inf:
                frontier.append(y)
            # update
            new_dist = dist[min_node] + distance(graph,min_node,y)
            if dist[y] > new_dist:
                dist[y] = new_dist
                parent[y] = min_node
                
    # retrieve the path from the parent list
    if d == a:
        return []
    elif parent[a] == None:
        return None
    
    path = [a]
    current = a
    while parent[current] != None:
        current = parent[current]
        path.append(current)
    
    path.reverse();
    return path


def prim(graph, d):
    parent = {}
    dist = {}
    
    # init
    for p in nodes(graph):
        parent[p], dist[p] = None, math.inf
    dist[d]=0
    
    frontier = nodes(graph)
    
    ############### TODO : complete code #####################
    while len(frontier) > 0:
        min_node = frontier.pop(np.argmin([dist[x] for x in frontier]))

        for y in neighbors(graph,min_node):
            if y in frontier and distance(graph,min_node,y) < dist[y]:
                dist[y] = distance(graph,min_node,y)
                parent[y] = min_node
                
    # retrieve the edges from the parent list
    edges = []
    for u in nodes(graph):
        if parent[u] != None:
            edges.append((parent[u], u))
            
    return edges



def kruskal(graph):
    
    # we sort edges depending on their weight 
    edges = sorted([(i, j) for i in nodes(graph) for j in neighbors(graph,i) if i < j], 
                   key = lambda e : distance(graph, e[0], e[1]))

    # structure for union-find
    forest = {}
    for i in graph:
        forest[i] = i
    
    mst = []

    ############### TODO : complete code #####################
    for u,v in edges:
        t1 = forest[u]
        t2 = forest[v]
        if t1 != t2:
            mst.append((u, v))
            for i in forest:
                if forest[i] == t2:
                    forest[i] = t1
        if len(mst) == len(graph) - 1:
            return mst
        
    return mst

