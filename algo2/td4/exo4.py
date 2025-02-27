#QUESTION1: 2, 5, 9, 11, 12

import random

def tab_alea(x, max):
    t = []
    for i in range(x-1):
        t.append(random.randint(1,max))
    return t

def min_local(t):
    if len(t) < 3:
        return
    for i in range(1,len(t)-1):
        if t[i] <= t[i+1] and t[i] <= t[i-1]:
            return t[i]
    return None

def local_minimum(T):
    n = len(T)
    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2
        if T[mid] <= T[mid - 1] and T[mid] <= T[mid + 1]:
            return mid
        elif T[mid] > T[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1


t = tab_alea(15,15)
print(t)
print(min_local(t))
    

    