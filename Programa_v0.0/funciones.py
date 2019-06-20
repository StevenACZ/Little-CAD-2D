import time
import os

#BORRAR PANTALLA "Import OS"
var = "cls"

#-------------FUNCIONES DE ANIMACION-------------
def steven_nombre():
    os.system(var)
    print("+----------+")
    print("|  CREADORES |")
    print("+----------+")


    time.sleep(1)
    os.system(var)
    print("+-------------------------+")
    print("| Steven Angel Coaila Zaa |")
    print("+-------------------------+")
    time.sleep(1)
    os.system(var)
    print("+------------------------------+")
    print("| Franco Matias Pacheco Espino |")
    print("+------------------------------+")
    time.sleep(1)
    os.system(var)
    print("+------------------------+")
    print("| Pedro Lizarbe Palacios |")
    print("| +----------------------+")
    time.sleep(1)
    os.system(var)

def abriendo_programa():
    print("+--------------------+")
    print("| ABRIENDO PROGRAMA. |")
    print("+--------------------+")
    time.sleep(1)
    os.system(var)
    print("+---------------------+")
    print("| ABRIENDO PROGRAMA.. |")
    print("+---------------------+")
    time.sleep(1)
    os.system(var)
    print("+----------------------+")
    print("| ABRIENDO PROGRAMA... |")
    print("+----------------------+")
    time.sleep(2)
    os.system(var)

def cerrando_programa():
    os.system(var)
    print("+--------------------+")
    print("| CERRANDO PROGRAMA. |")
    print("+--------------------+")
    time.sleep(1)
    os.system(var)
    print("+---------------------+")
    print("| CERRANDO PROGRAMA.. |")
    print("+---------------------+")
    time.sleep(1)
    os.system(var)
    print("+----------------------+")
    print("| CERRANDO PROGRAMA... |")
    print("+----------------------+")
    time.sleep(2)
    os.system(var)

#-----------FUNCIONES PRIMARIAS-------------
def crear_matriz(alto, largo):
    # CREANDO MATRIZ
    matriz = []
    for i in range(alto):  # ALTO
        matriz.append([])
        for j in range(largo):  # LARGO
            matriz[i].append(" ")
    return matriz

def generar_primer_cuadrante(alto, largo, matriz):
    # GENERAR LINEAS DEL PRIMER CUADRANTE
    for i in range(alto):  # ALTO
        if i != alto - 1:
            for j in range(largo):  # LARGO
                if j is 0:
                    matriz[i][j] = "."  # SIGNO DE LAS ESQUINAS
        else:
            for j in range(largo):  # LARGO
                matriz[i][j] = "."  # SIGNO DE LAS ESQUINAS

def imprimir_matriz(alto, largo, matriz):
    # IMPRIMIR MATRIZ
    for i in range(alto):
        for j in range(largo):  # LARGO
            print(matriz[i][j], end=" ")
        print()