from collections import defaultdict

def radixSort(t):  # radix sort based on the digits of the numbers written in base 10
    t = [str(x) for x in t]
    m = max([len(x) for x in t])
    for i in range(len(t)):
        t[i] = (m-len(t[i]))*'0' + t[i]
    digit = m-1
    while digit >=0:
        d = defaultdict(set)
        for x in t:
            d[int(x[digit])].add(x)
        j = 0
        for i in range(10):
            for x in d[i]:
                t[j] = x
                j+=1
        digit-=1
    t = [int(x) for x in t]
    #print(t)


t = [503, 87, 512, 61, 908, 170, 897, 275, 653, 426, 154, 509, 612, 677, 765, 703]

radixSort(t)




