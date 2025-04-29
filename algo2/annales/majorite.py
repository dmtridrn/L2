def trouveMajoriteNaif(t):
    max = len(t)//2
    for elt in t:
        cpt = 0
        for elt2 in t:
            if elt2 == elt:
                cpt +=1
                if cpt > max:
                    return elt
    return None

def trouveMajoriteComparables(t):
    r = sorted(t)
    cpt = 1
    max = len(t) // 2
    for i in range(len(r) - 1):
        if r[i] == r[i + 1]:
            cpt += 1
            if cpt > max:
                return r[i]
        else:
            cpt = 1
    return None



