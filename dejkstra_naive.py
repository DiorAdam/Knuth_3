

toy_map = { 'A': {'coords': (100, 100), 'next': {'B': 140, 'E': 200, 'F': 200}},
            'B': {'coords': (200, 140), 'next': {'A': 140, 'C': 260, 'F': 140}},
            'C': {'coords': (360,  40), 'next': {'B': 260, 'D': 360}},
            'D': {'coords': (320, 360), 'next': {'C': 360, 'F': 280}},
            'E': {'coords': ( 80, 280), 'next': {'A': 200, 'F': 120}},
            'F': {'coords': (160, 240), 'next': {'A': 200, 'B': 140, 'D': 280, 'E': 120}} }


def PCCs_naive(graph,s):
    frontier = [s]
    dist = {s: 0}

    while len(frontier)>0:

        ### extraction du noeud de la frontière ayant la distance minimal    ###
        x = extract_min_dist(frontier,dist)

        ### pour chaque voisin mise à jour de la frontière et de sa distance ###
        for y in graph[x]["next"]:
            if y not in dist:
                frontier.append(y)

            new_dist = dist[x] + graph[x]["next"][y]
            if y not in dist or dist[y] > new_dist:
                dist[y] = new_dist

    return dist

def extract_min_dist(frontier, dist):
    res = 0
    dmin = dist[frontier[0]]
    for k in range(len(frontier)):
        if dist[frontier[k]] < dmin:
            dmin = dist[frontier[k]]
            res = k
    return frontier.pop(res)

    
'''
print(PCC(toy_map, "A"))
'''