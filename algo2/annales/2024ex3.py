def foo(T, deb, fin) :
    if fin-deb <=1 : return
    m = (deb+fin)//2
    foo(T, deb, m)
    foo(T, m, fin)
    if T[m-1] > T[fin-1] :
        T[m-1], T[fin-1] = T[fin-1], T[m-1]
    foo(T, deb, fin-1)
    return T

print(foo([4, 3, 2, 1], 0, 4))