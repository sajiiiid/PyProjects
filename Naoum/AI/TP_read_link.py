from bs4 import BeautifulSoup
import numpy as np
from urllib.request import Request, urlopen

''' Importation du site'''
valide = "abcdefghijklmnopqrstuvwxyz "
indice = {valide[i] : i for i in range(len(valide))}
url = "https://fr.wikipedia.org/wiki/Rabat"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()

## Pretraitement du texte:
S = ' '.join(BeautifulSoup(html, "html.parser").stripped_strings)
S = S.lower()
S = ' '.join(S.split())  # Keep single spaces between words
S = "".join(x for x in S if x in valide) #remove invalid letters
while '  ' in S:
    S = S.replace('  ', ' ')
#print(S)

'''Construction de la matrice de Stochastic'''
P = np.zeros((len(valide), len(valide)))
for i in range(len(S)-1):
    ix = indice[S[ i ] ]
    iy = indice[S[i+1] ]
    P[ix][iy] += 1

for i in range( len(P) ):
    NbrChar = sum(P[i])
    if NbrChar > 0:
        P[i] = P[i] / NbrChar

'''
while True:
    print( valide[i], end='' )           # just keep printing words based
    i = np.random.choice(len(P), p=P[i]) # on probabilities from the matrix
'''

''' --- Etape 2 : Tester la performance --- '''

# 1. Fetching a second text of the same nature
url2 = "https://fr.wikipedia.org/wiki/Casablanca"
req2 = Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
html2 = urlopen(req2).read()

# Preprocessing the second text exactly like the first one
S2 = ' '.join(BeautifulSoup(html2, "html.parser").stripped_strings)
S2 = S2.lower()
S2 = ' '.join(S2.split())
S2 = "".join(x for x in S2 if x in valide)
while '  ' in S2:
    S2 = S2.replace('  ', ' ')

# Steps 1 & 2: Initialize score and tentatives
score = 0.0
tentatives = 0

# Step 3: Loop through the second text
for i in range(len(S2) - 1):
    x = S2[i]
    y = S2[i + 1]

    # Get the indices of the characters in your matrix
    ix = indice[x]
    iy = indice[y]

    # Steps 4 & 5: Increment score by the probability P[x, y]
    score += P[ix][iy]

    # Step 6: Increment tentatives
    tentatives += 1

# Step 7: Global fraction of correct attempts
fraction = score / tentatives

print(f"Score total : {score}")
print(f"Nombre de tentatives : {tentatives}")
print(f"Fraction globale (Performance) : {fraction:.4f}")