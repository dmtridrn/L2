def estUneMontagne(t):
    i = 0
    while t[i+1] > t[i]:
        i+=1
    while i < len(t)-1:
        if t[i+1] >= t[i]:
            return False
        i+=1
    return True

def pied(t):
    return min(t[0], t[len(t)-1])

def sommet(t):
    deb = 0
    fin = len(t) - 1
    while deb <= fin:
        mid = (deb + fin) // 2
        if t[mid-1] < t[mid] and t[mid+1] < t[mid]:
            return t[mid]
        elif t[mid-1] < t[mid] and t[mid+1] > t[mid]:
            deb = mid + 1
        else:
            fin = mid - 1
    return None

def nivelle(t):
    i = k = 0
    j = len(t) - 1
    res = [0] * len(t)
    while t[i+1] > t[i] and t[j-1] > t[j]:
        if t[i] <= t[j]:
            res[k] = t[i]
            i+=1
        else:
            res[k] = t[j]
            j-=1
        k+=1
    while t[i+1] > t[i]:
        res[k] = t[i]
        i+=1
        k+=1
    while t[j-1] > t[j]:
        res[k] = t[j]
        j-=1
        k+=1
    res[k] = sommet(t)
    return res


a = [1,2,3,4,7,6,5,4,3,2]
print(nivelle(a))

