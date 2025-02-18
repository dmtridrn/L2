def racine_1(n):
    i = 0
    carre = 1*1
    while carre <= n:
        if carre == n:
            return i
        i = i + 1
        carre = i*i
    return i-1

def racine_2(n):
    i, j = 0, n
    if n < 2:
        return n
    while j > i + 1:
        m = (i + j) // 2
        carre = m * m
        if carre == n:
            return m
        elif carre<n:
            i = m
        else:
            j = m
    return i


if __name__ == "__main__":
    print(racine_2(81))
