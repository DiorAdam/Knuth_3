from heapq import *


toy_map = { 'A': {'coords': (100, 100), 'next': {'B': 140, 'E': 200, 'F': 200}},
            'B': {'coords': (200, 140), 'next': {'A': 140, 'C': 260, 'F': 140}},
            'C': {'coords': (360,  40), 'next': {'B': 260, 'D': 360}},
            'D': {'coords': (320, 360), 'next': {'C': 360, 'F': 280}},
            'E': {'coords': ( 80, 280), 'next': {'A': 200, 'F': 120}},
            'F': {'coords': (160, 240), 'next': {'A': 200, 'B': 140, 'D': 280, 'E': 120}} }




def PCCs_heap(graph,s):
    frontier = [(0,s)]
    heapify(frontier)
    extracted = {}
    dist = {s:0}
    while len(extracted)< len(graph):

        ### extraction du noeud de la frontière ayant la distance minimal    ###
        x = heappop(frontier)[1]
        while x in extracted:
            x = heappop(frontier)[1]
        extracted[x] = True
        ### pour chaque voisin mise à jour de la frontière et de sa distance ###
        for y in graph[x]["next"]:
            new_dist = dist[x] + graph[x]["next"][y]

            if y not in dist or dist[y] > new_dist:
                heappush(frontier, (new_dist, y) )
                dist[y] = new_dist
            
    return dist


#print(PCCs_heap(toy_map, "A"))


def all_distances(map, PCC= PCCs_heap):
    res = {}
    for s in map:
        dist = PCCs_heap(map, s)
        for y in dist:
            if (s,y) not in res:
                res[(s,y)] = dist[y]
    return res

#print(all_distances(toy_map))

