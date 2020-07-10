def merge(t, a, b, c):
    u = t[a:c]
    i, k, j =a, a, b
    while i<b and j<c:
        if u[i-a] <= u[j-a]:
            t[k] = u[i-a]
            i+=1
        else:
            t[k] = u[j-a]
            j+=1
        k+=1
    if i == b:
        while k<c:
            t[k] = u[j-a]
            k+=1
            j+=1
    elif j==c:
        while k<c:
            t[k] = u[i-a]
            k+=1
            i+=1

 
def mergeSort(t, l, r, mem=set()):
    if not mem:
        i = 0
        while i+1<=len(t):
            mem.add((i,i+1))
            i+=1
    if (l,r) in mem:
        return l, r
    else:
        a, b = mergeSort(t, l, (l+r)//2, mem)
        c = mergeSort(t, (l+r)//2, r, mem)[1]
        merge(t, a, b, c)
        mem.add((l,r))
        return l, r

t = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]
mergeSort(t,0,len(t))
print(t)





