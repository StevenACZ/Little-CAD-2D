def crear_lista(largo):
    lista = []
    for i in range(largo):
        lista.append(" ")
    return lista


def crear_matriz(largo, alto):
    matriz = []
    for i in range(alto):
        matriz.append(crear_lista(largo))
    return matriz


def lienzo(largo, alto):
    matriz_lienzo = crear_matriz(largo, alto)
    for i in range(alto):
        for j in range(largo):
            if j == 0 or j == largo - 1 or i == 0 or i == alto - 1:
                matriz_lienzo[i][j] = "."
            else:
                matriz_lienzo[i][j] = " "

    return matriz_lienzo

global lienzoNuevo
lienzoNuevo = lienzo(82,42)
opcion = 10
while opcion != 0:

    menu = "\nMENU\n" \
           "1. Agregar una linea\n" \
           "2. Agregar una elipse o circulo\n" \
           "3. Agregar un rectangulo o un cuadrado\n" \
           "4. Agregar un triangulo\n" \
           "5. Mostrar un dibujo\n" \
           "6. Leer un dibujo\n" \
           "7. Grabar un dibujo\n" \
           "\n" \
           "0. Salir del programa\n\n"

    submenu2 = "\n\n1 Agregar una elipse\n" \
               "2 Agregar un circulo\n\n"

    submenu3 = "\n\n1 Agregar una rectangulo\n" \
               "2 Agregar un cuadrado\n\n"

    submenu7 = "\n\n1 ¿Continuar trabajando en el archivo?\n" \
               "2 ¿Crear nuevo archivo?\n\n"



    def plotear(x, y, lienzoPlotear):
        lienzoPlotear[y][x] = "X"
        return lienzoPlotear


    def imprimir(matriz_final):
        for i in range(matriz_final.__len__()):
            for j in range(matriz_final[i].__len__()):
                print(matriz_final[matriz_final.__len__() - 1 - i][j], end=' ')
            print("")


    def recta(*lista):
        global lienzoNuevo
        try:
            if lista.__len__()<1:
                input_string = input("'Recta'\nIntroduzca los puntos P0(X0,Y0) y P1(X1,Y1) separados por espacios \n")
                lista = input_string.split()
            if lista.__len__()<5:
                a=1
            else:
                lienzoNuevo = lista[4]
            X0 = int(lista[0])
            Y0 = int(lista[1])
            X1 = int(lista[2])
            Y1 = int(lista[3])
            if Y1 == Y0:
                for x in range(min(X0, X1), max(X0, X1)+1):
                    lienzoNuevo = plotear(x, Y1, lienzoNuevo)
            if X1 != X0:
                m = ((Y1-Y0)/(X1-X0))
                for y in range(min(Y0, Y1), max(Y0, Y1)):
                    for x in range(min(X0, X1), max(X0, X1)+1):
                        if (y - Y1) == int(m * (x-X1)):
                            lienzoNuevo = plotear(x, y, lienzoNuevo)
            else:
                for y in range(min(Y0, Y1), max(Y0, Y1)+1):
                    lienzoNuevo = plotear(X1, y, lienzoNuevo)
            return lienzoNuevo
        except:
            print("\n¡Introduzca valores válidos!\n")


    def triangulo():
        global lienzoNuevo
        try:
            input_string = input("'Triangulo'\nIntroduzca el punto inferior izquierdo P0(X0,Y0) y luego\nla medida de la base y la altura separados por espacios: \n\n")
            lista = input_string.split()
            X0 = int(lista[0])
            Y0 = int(lista[1])
            base = int(lista[2])
            altura = int(lista[3])
            lienzoNuevo = recta(X0, Y0, int((2*X0+base-1)/2), Y0+altura)
            lienzoNuevo = recta(int((2*X0+base-1)/2), Y0+altura, X0+base-1, Y0, lienzoNuevo)
            lienzoNuevo = recta(X0, Y0, X0+base-1, Y0, lienzoNuevo)
            return lienzoNuevo
        except:
            print("\n¡Introduzca valores válidos!\n")

    def rectangulo(*lista):
        try:
            if lista.__len__()<1:
                input_string = input("'Rectangulo'\nIntroduzca el punto inferior izquierdo P0(X0,Y0) y luego\nla medida de la base y la altura, separados por espacios: \n\n")
                lista = input_string.split()
            X0 = int(lista[0])
            Y0 = int(lista[1])
            base = int(lista[2])
            altura = int(lista[3])
            lienzoNuevo = recta(X0, Y0, X0, Y0+altura-1)
            lienzoNuevo = recta(X0, Y0+altura-1, X0+base-1, Y0+altura-1, lienzoNuevo)
            lienzoNuevo = recta(X0+base-1, Y0, X0+base-1, Y0+altura-1, lienzoNuevo)
            lienzoNuevo = recta(X0, Y0, X0+base-1, Y0, lienzoNuevo)
            return lienzoNuevo
        except:
            print("\n¡Introduzca valores válidos!\n")


    def cuadrado():
        global lienzoNuevo
        try:
            input_string = input("'Cuadrado'\nIntroduzca el punto inferior izquierdo P0(X0,Y0) y \nluego la medida del lado, separados por espacios: \n\n")

            lista = input_string.split()
            X0 = int(lista[0])
            Y0 = int(lista[1])
            lado = int(lista[2])
            lienzoNuevo = rectangulo(X0, Y0, lado, lado)
            return lienzoNuevo
        except:
            print("\n¡Introduzca valores válidos!\n")


    def elipse():
        global lienzoNuevo
        try:
            input_string = input("'Elipse'\nIntroduzca las coordenadas del centro P0(X0,Y0) y \n"
                                 "luego la medida del semieje 'X' y la medida del semieje 'Y', \n"
                                 "separados por espacios: \n\n")
            lista = input_string.split()
            X0 = int(lista[0])
            Y0 = int(lista[1])
            a = int(lista[2])
            b = int(lista[3])
            for y in range(42):
                for x in range(82):
                    if 0.92 < ((x-X0)/a)**2+((y-Y0)/b)**2 <= 1:
                        lienzoNuevo = plotear(x, y, lienzoNuevo)

            return lienzoNuevo
        except:
            print("\n¡Introduzca valores válidos!\n")


    def circulo():
        global lienzoNuevo
        try:
            input_string = input("'Circulo'\nIntroduzca el punto inferior izquierdo P0(X0,Y0) y \nluego la medida del radio, separados por espacios: \n\n")
            lista = input_string.split()
            X0 = int(lista[0])
            Y0 = int(lista[1])
            r = int(lista[2])
            for y in range(42):
                for x in range(82):
                    if r**2-r <(x-X0)**2+(y-Y0)**2 <= r**2:
                        lienzoNuevo = plotear(x, y, lienzoNuevo)

            return lienzoNuevo
        except:
            print("\n¡Introduzca valores válidos!\n")


    def mostrar(dibujofinal):
        imprimir(dibujofinal)


    def guardar(dibujofinal):
        nombrearchivo = input("Introduzca el nombre con que desea guardar el dibujo: \n") + ".cad"
        with open(nombrearchivo, "a+") as archivoNuevo:
            archivoNuevo.seek(0, 0)
            for j in range(42):
                for i in dibujofinal[41-j]:
                    archivoNuevo.write(i+",")
                archivoNuevo.write("\n")
        print("\n.\n.\n.\n Archivo guardado satisfactoriamente.\n")


    def leer():
        global lienzoNuevo
        global dibujo
        nombrearchivo = input("Introduzca el nombre del dibujo que desea abrir: \n") + ".cad"
        print('\n.\n.\n.\n Leyendo archivo: "', nombrearchivo, '"\n')
        try:
            with open(nombrearchivo, "a+") as abrirarchivo:
                abrirarchivo = open(nombrearchivo, "r")
                listalienzo = abrirarchivo.read()
                filas = listalienzo.splitlines()
                for y in range(42):
                    temp = filas[y].split(",")
                    if temp.__contains__("\n"):
                        temp.remove("\n")
                    temp.pop(82)
                    lienzoNuevo[41-y] = temp
            dibujo = lienzoNuevo
        except:
            print("No se encontro el archivo: '", nombrearchivo, "'" )


    opcion = int(input(menu))

    if opcion == 1:
        dibujo = recta()

    elif opcion == 2:
        try:
            opcionsubmenu2 = int(input(submenu2))
            if opcionsubmenu2 == 1:
                dibujo = elipse()
            elif opcionsubmenu2 == 2:
                dibujo = circulo()
        except:
            print("\nDebe introducir una opcion valida\n")

    elif opcion == 3:
        try:
            opcionsubmenu2 = int(input(submenu3))
            if opcionsubmenu2 == 1:
                dibujo = rectangulo()
            elif opcionsubmenu2 == 2:
                dibujo = cuadrado()
        except:
            print("\nDebe introducir una opcion valida\n")
    elif opcion == 4:
        dibujo = triangulo()
    elif opcion == 5:
        try:
            mostrar(dibujo)
        except:
            print("\n¡¡¡No se puede mostrar la imagen!!!\n")

    elif opcion == 6:
        leer()
    elif opcion == 7:
        guardar(dibujo)

        i = 1
        while i == 1:
            opcionsubmenu7 = input(submenu7)
            if opcionsubmenu7 == "1":
                i = 2
                continue
            elif opcionsubmenu7 == "2":
                lienzoNuevo = lienzo(82,42)
                dibujo = lienzoNuevo
                i = 2
            else:
                print("\n¡Opción incorrecta!\n")