
def insertion(tab, val):
    if not tab:
        tab.append([val])
        return
    i, j = 0, len(tab[0])
    while i < len(tab):
        j = min(j, len(tab[i])-1)
        while j>= 0 and tab[i][j] > val:
            j-=1
        if j == len(tab[i])-1:
            tab[i].append(val)
            break
        else:
            tab[i][j+1], val = val, tab[i][j+1]
        i+=1

    if i==len(tab):
        tab.append([val])

def deletion(tab, s):
    i, j = s, len(tab[s])
    val = tab[s].pop()
    if not tab[s]:
        tab.pop(s)
    i-=1
    while i>=0:
        while j < len(tab[i]) and tab[i][j] < val:
            j+=1
        val, tab[i][j-1] = tab[i][j-1], val
        i-=1

'''
t = [[1,3,5,9,12,16], [2,6,10,15], [4,13,14], [11], [17]]
t = []
p = [7,2,9,5,3]
for x in p:   
    insertion(t,x)

#deletion(t,3)
#deletion(t,3)
for x in t:
    print(x)
'''
