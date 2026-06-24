'''1. Heladería: sabor más pedido 
Una heladería quiere registrar 5 pedidos. 
 Por cada cliente, el programa debe pedir el sabor elegido: 
 vainilla 
 chocolate 
 fresa 
Al final debe mostrar cuántas veces se pidió cada sabor. 
Practica: ciclos, condicionales, contadores.'''

import os
os.system("clear")

menu="""Menú
Elija un sabor
1. Vainilla
2. Chocolate
3. Fresa"""

eleccion="He elegido la opción de"

for i in range(5):
    while True:
        try:
            print(menu)
            sabor=int(input("¿Qué sabor desea? "))
            print()

            if sabor == 1:
                print(f"{eleccion} vainilla")
                break

            elif sabor == 2:
                print(f"{eleccion} chocolate")
                break

            elif sabor == 3:
                print(f"{eleccion} fresa")
                break

            else: 
                print("Opción inválida, intente de nuevo")
                print()

        except ValueError:
            print("¡Error!, escriba un número")
            print()

    if 0 < sabor < 4 :
        cantidad=int(input("¿Cuántos helados deseas? "))


#Hacer una lista con diccionarios dentro que indiquen qué sabor se pidió y la cantidad