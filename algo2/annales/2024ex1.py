def distincts_naif(t):
    if not t:
        return 0
    count = 1
    for i in range(1, len(t)):
        est_distinct = True
        for j in range(i):
            if t[i] == t[j]:
                est_distinct = False
                break
        if est_distinct:
            count += 1
    return count

def distinct(t):
    s = set()
    for i in range(len(t)):
        s.add(t[i])
    return len(s)



tab = [0,1,2,3,3,4,3,7,5,60,3]
print(distincts_naif(tab))    
print(distinct(tab))     