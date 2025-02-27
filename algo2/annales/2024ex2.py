def verif_tri_circulaire(t):
    k = 0
    for i in range(1, len(t)):
        if t[i] < t[i-1]:
            k = i
            break
    while t[k] < t[0]:
        if k == len(t)-1:
            return True
        k+=1
    return False
    
# optimal car on ne peut pas vérifier sans vérifier chaque élément, compléxité temps = O(n), 
# compléxité espace =  O(1)

def compare(i,t):
    if t[i] < t[i-1]:
        return 0
    else:
        


T = [10, 12, 2, 4, 6, 8]
print(verif_tri_circulaire(T))
print(compare(1,T))