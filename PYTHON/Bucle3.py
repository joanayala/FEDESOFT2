#Impresión de la table del 9 con ciclo While
import os

os.system("cls")

TABLA = 9
i = 1

while i <= 10 :
    print(TABLA, " x ", i, " = ", TABLA*i)
    i = i + 1