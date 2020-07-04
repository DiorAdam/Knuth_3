def binlist(t):
    n = len(bin(max(t)))-2
    d = {}
    for i in range(len(t)):
        s = bin(t[i])[2:]
        a = t[i]
        t[i] = (n-len(s))*'0' + s
        d[t[i]] = a
    return d


def radixSort(t, l, r, u=0):
    m = len(t[0])
    if r-l <=1 or u >=m:
        return
    s = l
    for i in range(l,r):
        if t[i][u] == '0':
            t[i], t[s] = t[s], t[i]
            s+=1
    radixSort(t, l, s, u+1)
    radixSort(t, s, r, u+1)



klist = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]

d = binlist(klist)
radixSort(klist,0,len(klist))
print([d[x] for x in klist])
