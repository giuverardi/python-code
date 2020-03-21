from math import *

class cubo:
    x = 0
    vol = 0
    
class sfera:
    r = 0
    d = 0
    circ = 0
    sup = 0
    vol = 0

cubo.x = float(input("Inserisci lato intero del cubo: "))
cubo.vol = (cubo.x)**3
sfera.r = cubo.x
sfera.circ = 2*pi*sfera.r
sfera.d = 2*sfera.r
sfera.sup = 4 * pi * (sfera.r)**2
sfera.vol = (4/3) * pi * (sfera.r)**3

print("Il volume del cubo è: ")
print(cubo.vol)
print("Una sfera con lo stesso raggio del lato del cubo ha superficie e volume: ")
print("Volume della sfera: ", sfera.sup, "Volume del cubo: ", sfera.vol)
if sfera.vol > cubo.vol:
    print("Il volume della sfera è maggiore del volume del cubo.")
elif cubo.vol > sfera.vol:
    print("Il volume della cubo è maggiore del volume della sfera.")
else:
    print("Il volume della sfera è uguale al volume del cubo.")
