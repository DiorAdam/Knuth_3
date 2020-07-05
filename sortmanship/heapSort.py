def heapify(t):
    n = len(t)
    l = n//2+1
    while l>1:
        l-=1
        i = l
        while True:
            j = 2*i
            if j>n: break
            if j < n and t[j]  > t[j-1]:
                j+=1
            if t[i-1] < t[j-1]:
                t[i-1], t[j-1] = t[j-1], t[i-1]
                i = j
            else: break
    


def isHeap(t):
    for k in range(2, len(t)+1):
        if t[k-1] > t[k//2-1]:
            return False
    return True
    
t = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]

heapify(t)
print(isHeap(t))
print(t)



