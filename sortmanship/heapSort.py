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
    return t
    


def isHeap(t):
    for k in range(2, len(t)+1):
        if t[k-1] > t[k//2-1]:
            return False
    return True


def heapSort(t):
    heapify(t)
    print(t)
    n = len(t)
    r = n-1
    while r > 0:
        t[0], t[r] = t[r], t[0]
        t[:r] = heapify(t[:r])
        '''
        a = t[0]
        k = 1
        while 2*k <= r:
            if t[2*k-1] > t[2*k]:
                t[k-1] = t[2*k-1]
                k = 2*k
            else:
                t[k-1] = t[2*k]
                k = 2*k+1
        for i in range(k,r+1):
            t[i-1],t[i] = t[i], t[i-1]
        t[r] = a
        print(t, isHeap(t[:r]))
        '''
        r-=1
            

    
t = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]

heapSort(t)
print(t)



