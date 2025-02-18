def occurence_naif(tab, x):
    cpt = 0
    for i in tab:
        if i == x:
            cpt += 1
    return cpt

tab = [1,5,6,9,8,5,4,7,4,5,2,3,6,9,8,5]
print(occurence_naif(tab, 2))
    