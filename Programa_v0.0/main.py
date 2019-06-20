#LIBRERIAS A USAR
from funciones import *
import time
import os
import itertools

#TIPO DE OS
var = "cls"

#DESARROLLAOR = D
#CLIENTE = C

modo = input("> ")

if modo == "C":
    #NOMBRE "Steven Angel Coaila Zaa"
    steven_nombre()

    #ABRIENDO PROGRAMA
    abriendo_programa()

#MENU OPCIONES
opciones = ["1. Agregar una linea               ",
            "2. Agregar una elipse o circulo    ",
            "3. Agregar un rectangulo o cuadrado",
            "4. Agregar un triangulo            ",
            "5. Mostrar un dibujo               ",
            "6. Leer un dibujo                  ",
            "7. Grabar un dibujo                ",
            "-----------------------------------",
            "0. Salir del programa              "
            ]

Tabla = """
+-------------------------------------+
|                 Menú                |
|-------------------------------------|
{}
+-------------------------------------+\n
"""

#IMPRIMIENDO TABLA
Tabla = (Tabla.format("\n".join("| {} |".format(fila)
for fila in opciones)))
print(Tabla)




#SECUENTA WHILE "Seleccionando opcion"
while True:
    opcion = input("> Elija opcion: ")

    os.system(var)
    print("+-------------------+")
    print("| Opcion elegida:",opcion,"|")
    print("+-------------------+")
    time.sleep(1)
    os.system(var)

    if opcion == "1":
        #RECTA
        alto = 20 #82
        largo = 20 #42

        matriz = crear_matriz(alto, largo) #GENERA LA MATRIZ
        generar_primer_cuadrante(alto, largo, matriz) #CREA EL PRIMER CUADRANTE

        for x, y in itertools.product(range(20), range(20)):  # RANGO DE LA RECTA (ALTO, LARGO)
            ecuacion = y = -1 * x + 19  # ECUACION DE LA RECTA
            if ecuacion >= 1 and ecuacion <= 19:  # LARGO X ALTURA (VISIBLE)
                matriz[x][y] = "X"  # SIMBOLO DE LA ECUACION

        imprimir_matriz(alto, largo, matriz) #IMPRIME LA MATRIZ
        continue
    if opcion == "2":
        #POSICIONES
        radio = float(input("> Ingrese radio: "))
        posicion_x = float(input("> Ingrese posicion 'X': "))
        posicion_y = float(input("> Ingrese posicion 'Y': "))

        # CIRCULO
        alto = 42
        largo = 82

        matriz = crear_matriz(alto, largo)  # GENERA LA MATRIZ
        generar_primer_cuadrante(alto, largo, matriz)  # CREA EL PRIMER CUADRANTE

        for x, y in itertools.product(range(alto), range(largo)):
            ecuacion = (x - posicion_y) ** 2 + (y - posicion_x) ** 2  # Con eso se mueve el circulo
            if ecuacion >= radio and ecuacion <= radio * 2:
                matriz[x][y] = "X"

        imprimir_matriz(alto, largo, matriz)  # IMPRIME LA MATRIZ

        continue
    if opcion == "5":
        # DIBUJO
        alto = 42
        largo = 82

        matriz = crear_matriz(alto, largo)  # GENERA LA MATRIZ
        generar_primer_cuadrante(alto, largo, matriz)  # CREA EL PRIMER CUADRANTE

        # CARA
        for x, y in itertools.product(range(alto), range(largo)):
            ecuacion = (x - 20) ** 2 + (y - 40) ** 2
            if ecuacion >= 170 and ecuacion <= 200:
                matriz[x][y] = "X"

        # OJOS
        for x, y in itertools.product(range(alto), range(largo)):
            ecuacion = (x - 15) ** 2 + (y - 33) ** 2
            if ecuacion >= 2 and ecuacion <= 5:
                matriz[x][y] = "X"
        for x, y in itertools.product(range(alto), range(largo)):
            ecuacion = (x - 15) ** 2 + (y - 47) ** 2
            if ecuacion >= 2 and ecuacion <= 5:
                matriz[x][y] = "X"

        # BOCA
        for x, y in itertools.product(range(alto), range(largo)):
            ecuacion = (x - 23) ** 2 / 6 + (y - 40) ** 2
            if ecuacion >= 4 and ecuacion <= 9:
                matriz[x][y] = "X"

        imprimir_matriz(alto, largo, matriz)  # IMPRIME LA MATRIZ
        continue
    if opcion == "0":
        #SALIR DEL PROGRAMA
        cerrando_programa()
        break



