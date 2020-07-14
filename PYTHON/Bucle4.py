#Impresión de cualquier tabla de mult. con ciclo While
import os

os.system("cls")

estado = True
i = 1

while estado :
    TABLA = int(input(".:: Digite la tabla de multiplicar: "))

    if TABLA < 1 :
        print("::: Sólo se aceptan número mayores a cero :::")
        estado = True
    else :
        estado = False 

Li = int(input("Ingrese límite inferior: "))
Ls = int(input("Ingrese límite superior: "))

i = Li
while i <= Ls :
    print(TABLA, " x ", i, " = ", TABLA*i)
    i = i + 1