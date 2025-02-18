def est_premier(p):
    if p == 1: return False
    for i in range(2,p):
        if(p % i == 0):
            return False
    return True

def eratosthene(n):
    tab = [False, False] + [True]*(n-1)
    for i in range(2,n+1):
        if(tab[i]):
            for k in range(2*i, n+1, i):
                tab[k] = False
    print(tab)

if __name__ == "__main__":
    eratosthene(10)
    [ p for p,b in enumerate(eratosthene(10**6)) if b ]
