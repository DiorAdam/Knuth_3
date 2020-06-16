

def invTable_perm(t):
    n = len(t)
    perm = []
    for k in range(n,0,-1):
        perm.insert(t[k-1],k)
    return perm


class Inversion:
    def __init__(self,t):
        self.perm = t

    def perm_invTable(self):
        def searchInsert(nums, target):
            i, j = 0, len(nums)-1
            while i<=j:
                mid = (i+j)//2
                if nums[mid] == target:
                    return mid
                elif (mid == len(nums)-1 and nums[mid]<target) or (mid <len(nums)-1 and nums[mid]<target < nums[mid+1]):
                    return mid+1
                elif nums[mid] < target:
                    i = mid+1
                else:
                    j= mid-1
            return mid

        n = len(self.perm)
        d = {}
        for i in range(n):
            d[self.perm[i]] = i
        ans = [0]*n
        place = [d[9]]
        for k in range(n-1,0,-1):
            ans[k-1] = searchInsert(place,d[k])
            place.insert(ans[k-1],d[k])
        return ans
        

    def fact(self):  
        n = len(self.perm)
        rest = set(range(1,n+1))
        ans = []
        while rest:
            a = min(rest)
            cycle = [a]
            u = self.perm[a-1]
            rest.remove(a)
            while u!=a:
                cycle.append(u)
                rest.remove(u)
                u = self.perm[u-1]
            ans.append(cycle)
        return ans




a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
t = Inversion([5, 9, 1, 8, 2, 6, 4, 7, 3])
print(t.fact())


