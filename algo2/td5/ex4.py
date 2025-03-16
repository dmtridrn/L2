def intersectionNaif(E,F):
    I = []
    for i in range(len(E)):
        if E[i] in F:
            I.append(E[i])  #O(n^2)
    return I


def intersectionTrie(E,F):
    i = 0
    j = 0
    I = []
    while i < len(E) and j < len(F):
        if E[i] == F[j]:
            I.append(E[i])
            i+=1
            j+=1
        elif E[i] < F[j]:
            i+=1
        else: 
            j+=1
    return I


a = [1,3,4,6,9]
b = [1,4,5,6,9]
print(intersectionTrie(a,b))
print(intersectionNaif(a,b))