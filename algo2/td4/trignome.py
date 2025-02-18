def tri(tab):
    i = 0
    cpt = 0
    while i < len(tab):
        if i == 0:
            i+=1
            cpt+=1
        if(tab[i-1] < tab[i] or tab[i-1] == tab[i]):
            i+=1
            cpt+=1
        elif(tab[i-1] > tab[i]):
            tab[i-1], tab[i] = tab[i], tab[i-1]
            i-=1
            cpt+=1
    print(cpt)
    return tab

tab = [1,2,3,4,5,6,7,8,9,10]
print(tri(tab))
        