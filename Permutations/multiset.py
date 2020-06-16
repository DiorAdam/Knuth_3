from collections import defaultdict



def fact(multiset):
    ind_inv = defaultdict(list)
    pos = defaultdict(int)
    n = len(multiset)
    for i in range(n):
        ind_inv[multiset[i]].append(i)
    ans = []
    rest = set(range(n))
    while rest:
        i, a = min([(i,multiset[i]) for i in rest], key = lambda x:x[1])
        rest.remove(i)
        cycle = [(a,0)]
        i, u = ind_inv[a][pos[0]]
        
