# creazione quadrato magico
# vincoli da ricordare: la matrice è quadrata, la somma di ogni riga, colonna e diagonale è un numero detto
# numero magico
# il prodotto del numero magico con l'ordine della matrice dà la somma degli elementri tra di loro
# l'ordine è il numero di righe o di colonne
# la somma degli elementi è dato dalla sommatoria degli elementi o più semplicemente n(n + 1) / 2

import numpy as np

# creiamo la lista vuota che conterrà l'elenco dei numeri della matrice
list_number = []

row = int(input('Inserisci il numero di righe per creare la matrice quadrata superiore a zero: '))
col = row

# create matrix with zero elements
m=np.zeros((row, col))

# doppio ciclo per trasformare gli elementi della matrice da 0 a 1
a = 1
SommaElementi = 0

for y in range(col):
    for x in range(row):
        SommaElementi=SommaElementi + a
        list_number.append(a)
        a = a + 1

MagicNumber = SommaElementi/row

print(m)
print(list_number)
print('Il numero magico della matrice', row, 'x', row, 'è', MagicNumber)

col, row = 3, 3

# cc è la colonna centrale
cc = int((col - 1) / 2)

# create matrix with zero elements
m = np.zeros((row, col))

m[0, cc] = 1
m[row - 1, cc + 1] = 2
m[row - 1, cc + 1] = 2

print(m)
