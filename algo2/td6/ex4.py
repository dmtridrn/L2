#Q1
def triDrapeau(T):
    bleus = []
    blancs = []
    rouges = []
    
    for element in T:
        if element.couleur == "bleu":
            bleus.append(element)
        elif element.couleur == "blanc":
            blancs.append(element)
        else:
            rouges.append(element)
    resultat = bleus + blancs + rouges
    return resultat

#Q2
def triBiCouleur(t):
    deb = 0
    fin = len(t) - 1
    curr = 0
    while curr <= fin:
        if t[curr].couleur == "bleu":
            t[curr], t[deb] = t[deb], t[curr]
            curr+=1
            deb+=1
        if t[curr].couleur == "rouge":
            t[curr], t[fin] = t[fin], t[curr]
            fin-=1
    return t

def triDrapeauHollandais(t):
    bleu = 0 
    blanc = 0
    rouge = len(t) - 1 
    
    while blanc <= rouge:
        if t[blanc].couleur == "bleu":
            t[bleu], t[blanc] = t[blanc], t[bleu]
            bleu += 1
            blanc += 1
        elif t[blanc].couleur == "blanc":
            blanc += 1
        else:
            t[blanc], t[rouge] = t[rouge], t[blanc]
            rouge -= 1
    return t