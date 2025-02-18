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

def exponentiation_binaire_iter(m, n):
    result = 1
    base = m
    while n > 0:
        if n % 2 == 1:
            result *= base
        base *= base
        n //= 2
    return result

if __name__ == "__main__":
    print(exponentiation_binaire_rec(15,50))
    print(10**10000)