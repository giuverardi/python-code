# creazione quadrato magico
# vincoli da ricordare: la matrice è quadrata, la somma di ogni riga, colonna e diagonale è un numero detto
# numero magico
# il prodotto del numero magico con l'ordine della matrice dà la somma degli elementri tra di loro
# l'ordine è il numero di righe o di colonne
# la somma degli elementi è dato dalla sommatoria degli elementi o più semplicemente n(n + 1) / 2

import numpy as np

# chiediamo all'utente di inserire l'ordine della matrice
N = int(input('Inserisci un numero dispari per il numero di righe della matrice quadrata: '))

# create matrix with zero elements
magic_square = np.zeros((N,N), dtype = int)

# inizializziamo le variabili n per inserire i valori da 1 a N**2
# inizializziamo i e j per muoverci sulla matrice
n = 1
i, j = 0, N//2

# doppio ciclo per trasformare gli elementi della matrice da 0 a 1
a = 1
SommaElementi = 0

for x in range(N**2):
    SommaElementi = SommaElementi + a
    a = a + 1

MagicNumber = SommaElementi / N

print('Il numero magico della matrice', N, 'x', N, 'è', MagicNumber)

# Create an N x N magic square. N must be odd.
while n <= N**2:
    magic_square[i, j] = n
    n += 1
    newi, newj = (i-1) % N, (j+1) % N
    if magic_square[newi, newj]:
        i += 1
    else:
        i, j = newi, newj

print(magic_square)
