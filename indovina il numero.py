import random

# generiamo un numero random tra 1 e 10
n = random.randrange(1,11)

for i in range(2):
    x = int(input("Inserisci un numero compreso tra 1 e 10: "))
    
    # se ha indovinato
    if x==n:
        print("Hai indovinato al tentativo numero: ", i+1)
        
        # usciamo dal programma
        break
    
    # altrimenti se siamo ancora nel range
    elif i<1:
       
        # valutiamo se il numero è più basso di quello pensato dal computer
        if x<n:
            print("Inserisci un numero più alto")
        
        # valutiamo se il numero è più alto di quello pensato dal computer
        else:
            print("Inserisci un numero più basso")
            
    else:
        print("Mi spiace, hai esaurito i tentativi a disposizione")