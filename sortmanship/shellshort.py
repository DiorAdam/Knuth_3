
def insertionSort(t):
    n = len(t)
    for i in range(1, n):
        j, a = i-1, t[i]
        while j >= 0 and t[j] > a:
            t[j], t[j+1] = t[j+1], t[j]
            j-=1
    print(t)


def increments(n):
    ans = []
    n//=2
    while n >0:
        ans.append(n)
        n//=2
    return ans



def insertShell(t, start, step):
    i = start + step
    while i < len(t):
        j, a = i-step, t[i]
        while j >= start and t[j] > a:
            t[j] , t[j+step] = t[j+step], t[j]
            j-=step
        i+=step
    


def shellSort(t, incr=None):
    n = len(t)
    if not incr:
        incr = increments(n)
    for x in incr:
        for k in range(n//x):
            insertShell(t,k,x)
        print(x, t)
    


u = [2,0,1,7,3,7,4,5,9,8,5,1]
klist = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]
shellSort(klist)
        

