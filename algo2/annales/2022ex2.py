def maille(t):
    mini = max(t) - min(t)
    for i in range(len(t)):
        for j in range(len(t)):
            if t[i]>=t[j] and i != j:
                tmp = t[i] - t[j]
                if tmp < mini:
                    mini = tmp
    return mini




def meilleureMaille(t):
    t.sort()
    mini = float('inf')
    print(mini)
    for i in range(len(t)-1):
        if t[i] >= t[i+1]:
            temp = t[i] - t[i+1]
            if temp < mini:
                mini = temp
    return mini






