#LIBRERIAS A USAR
from funciones import *
import time          #CALCULAR TIEMPO
import os            #LIMPIAR LA PANTALLA
import itertools     #MATRICES

#TIPO DE OS
var = "cls"

#NOMBRES
team_nombres()

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


#SECUENCIA WHILE "Seleccionando opcion"
while True:
    opcion = input("> Elija opcion: ")

    os.system(var)
    print("+-------------------+")
    print("| Opcion elegida:",opcion,"|")
    print("+-------------------+")
    time.sleep(1)
    os.system(var)

    if opcion == "1":
        print("EN PROCESO...")
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

        continue
    if opcion == "3":
        print("EN PROCESO...")
        continue
    if opcion == "4":
        print("EN PROCESO...")
        continue
    if opcion == "5":
        imprimir_matriz(alto, largo, matriz)  # IMPRIME LA MATRIZ
        continue
    if opcion == "6":
        print("EN PROCESO...")
        continue
    if opcion == "7":
        print("EN PROCESO...")
        continue
    if opcion == "0":
        #SALIR DEL PROGRAMA
        cerrando_programa()
        break


