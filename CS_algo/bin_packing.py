def verifyBP(O, B, k, L):
    ############### TODO : complete code ##################### 
    # at most k bins
    if len(L) > k: 
        return False
    
    # L is a partition
    L_flat = [obj for bin in L for obj in bin]
    if sorted(O) != sorted(L_flat): 
        return False
    
    # It fits
    for bin in L: 
        if sum(bin) > B: 
            return False
    
    return True


def first_fit(O, B):
    L = []
    ############### TODO : complete code ##################### 
    for o in O:
        placed = False
        for bin in L:
            if sum(bin) + o <= B :
                placed = True
                bin.append(o)
                break
        if not placed :
            L.append([o])
    
    return L


def best_fit(O, B):
    L = []
    ############### TODO : complete code ##################### 
    for o in O:
        bf_bin = None
        min_space = B
        for bin in L:
            space = B - sum(bin)
            if o <= space and space < min_space :
                bf_bin = bin
                min_space = space
        if bf_bin == None:
            L.append([o])
        else:
            bf_bin.append(o)
    
    return L
