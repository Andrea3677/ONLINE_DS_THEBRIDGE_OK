
#Función para crear tablero en blanco
def crear_tablero(lados):
    tablero=[]
    for elemento in range(0,lados,1):
        fila = []
        for elemento in range (0,lados,1):
            fila.append(" ")
        tablero.append(fila)
    return tablero


#Funcion para imprimir tablero
def imprimir_tablero(tablero):
    tamaño = len(tablero)+1
    
    # Encabezado con números
    print("    " + "   ".join(str(i) for i in range(1,tamaño)))
    
    # Filas con números
    for i, fila in enumerate(tablero):
        print(f"{i} | " + " | ".join(fila))

#Función para pintar los barcos en el tablero
def pintar_barcos(barcos,tablero):
    for valor in barcos.values():
        for elemento in valor:
            i = elemento[0] - 1
            j = elemento[1] - 1
            tablero[i][j] = "B"
    return tablero

#Función para el input de la coordenada del jugador humano
def input_coordenada_jh():
    i = int(input("Indica la coordenada x"))-1
    j = int(input("Indica la coordenada y"))-1
    return i, j

#Función para determinar disparo de la maquina
def disparo_maquina():
    i = random.randint(0,9)
    j = random.randint(0,9)
    return i, j

#Funcion para determinar si corresponde o no un segundo disparo 
def disparar(coordenada_i, coordenada_j, tablero):
    if tablero[coordenada_i][coordenada_j] == "B":
        return True
    elif tablero[coordenada_i][coordenada_j] == " ":
        return False
    else:
        return False

#Función para comprobar si la coordenada es válida
def coordenada_valida(i,j):
    if i > 10 or j > 10:
        return False
    else:
        return True

#Función para el turno humano
def jugada_humana(tablero_maquina, tablero_disparos):
    continuar = True
    while continuar == True:
        i, j = input_coordenada_jh()
        if coordenada_valida(i,j) == False:
            print(f"Coordenada {i},{j}, inválida. Error: Coordenada fuera del límite del tablero")
            print(f"Pierdes el turno")
            continuar = False
        else:
            if tablero_maquina[i][j] == "B":
                tablero_maquina[i][j] = "X"
                tablero_disparos[i][j] = "X"
                print(f"Tocado en posición {i + 1},{j + 1}")
                continuar = True
            elif tablero_maquina[i][j] == " ":
                tablero_maquina[i][j] = "O"
                tablero_disparos[i][j] = "O"
                continuar = False
                print(f"Agua en posición {i + 1},{j + 1}")
            elif tablero_disparos[i][j] == "X" or tablero_disparos[i][j] == "O":
                continuar = False
                print(f"Posición {i + 1},{j + 1} ya había sido disparada")
            else:
                continuar = False
                print(f"Coordenada {i + 1},{j + 1}, inválida.")
    return continuar,tablero_maquina,tablero_disparos

#Función de la jugada máquina
def jugada_maquina(tablero_jugador):
    continuar = True
    while continuar == True:
        i, j = disparo_maquina()
        print(i,j)
        if coordenada_valida(i,j) == False:
                print(f"Coordenada {i},{j}, inválida. Error: Coordenada fuera del límite del tablero")
                print(f"Pierdes el turno")
                continuar = False
        else:
            if tablero_jugador[i][j] == "B":
                tablero_jugador[i][j] = "X"
                continuar = True
                print(f"Tocado en posición {i},{j}")
            elif tablero_jugador[i][j] == " ":
                tablero_jugador[i][j] = "O"
                continuar = False
                print(f"Agua en posición {i},{j}")
            elif tablero_jugador[i][j] == "X" or tablero_jugador[i][j] == "O":
                continuar = False
                print(f"Posición {i},{j} ya había sido disparada")
            else:
                continuar = False
                print(f"Coordenada {i},{j}, inválida.")
    return continuar,tablero_jugador

#Función para saber si hay barcos en el tablero
def buscando_barcos(tablero_jugador):
    lista=[]
    for fila in tablero_jugador:
        for celda in fila:
            if "B" in celda:
                lista.append(True)
            else:
                lista.append(False)
    return bool(sum(lista))