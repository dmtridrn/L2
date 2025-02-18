def exponentiation_binaire_rec(m,n):
    if n == 0:
        return 1
    elif n == 1:
        return m
    l = m*m
    s = exponentiation_binaire_rec(l,n//2)
    if n%2 == 0:
        return s
    else:
        return m*s

def algonaif(t,x):
    res = 0
    for i in range(0, len(t)):
        if(t[i] != 0):
            res+=t[i]*(exponentiation_binaire_rec(x,i))
        else:
            res+=(exponentiation_binaire_rec(x,i))
    print(res)

def horner(P,x):
    res = 0
    for coeff in P[::-1]:
        res = res * x + coeff
    print(res)

if __name__ == "__main__":
    t = [1,1,2,1,1]
    algonaif(t,3)
    horner(t,3)


