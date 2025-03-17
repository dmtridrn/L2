def foo(T, deb = 0, fin = None) :
    if fin == None : fin = len(T)
    if fin - deb < 2 : return T
    if fin - deb == 2 :
        if T[deb] > T[deb+1] :
            T[deb], T[deb+1] = T[deb+1], T[deb]
        return T
    un_tiers = (fin - deb) // 3
    b1, b2 = deb + un_tiers, fin - un_tiers
    foo(T, deb, b2)
    foo(T, b1, fin)
    foo(T, deb, b2)
    return T

print(foo([6,5,4,3,2,1]))

