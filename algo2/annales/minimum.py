def rechercheMinimumLocal(t):
    deb = 1
    fin = len(t) - 2
    while deb <= fin:
        mid = (deb + fin)//2
        if t[mid]<=t[mid-1] and t[mid]<=t[mid+1]:
            return mid
        elif t[mid - 1] > t[mid]:
            deb = mid+1
        else:
            fin = mid-1

def fusionSansDoublon(e, f):
    i, j = 0, 0
    res = []
    while i < len(e) and j < len(f):
        if e[i] == f[j]:
            res.append(e[i])
            i += 1
            j += 1
        elif e[i] > f[j]:
            res.append(f[j]) 
            j += 1
        else:
            res.append(e[i])
            i += 1
    
    while i < len(e):
        res.append(e[i])
        i += 1
    
    while j < len(f):
        res.append(f[j])
        j += 1
    
    return res


t = [1,3,5,7,9]
r = [2,4,6,8,10]
s = [9,8,7,6,5,4,3,2,1,1]

print(rechercheMinimumLocal(s))        
