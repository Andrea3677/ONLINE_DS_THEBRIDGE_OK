import random
import time

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

    print()

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
    i = input("Indica la coordenada x")
    j = input("Indica la coordenada y")
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
    if len(i)!= 1 or len(j)!= 1:
        return False,i,j
    elif i.isalpha() or j.isalpha():
        return False,i,j
    else:
        i = int(i)-1
        j = int(j)
        if i > 10 or j > 10:
            return False, i, j 
        elif i < 0 or j < 0:
            return False, i, j
        else:
            return True, i, j 
   

#Función para el turno humano
def jugada_humana(tablero_maquina, tablero_disparos):
    continuar = True
    time.sleep(2)
    while continuar == True:
        i, j = input_coordenada_jh()
        validez, i, j = coordenada_valida(i,j)
        if validez == False:
            print(f"Coordenada inválida. Sólo se admiten numeros de 0 al 10, según tablero.")
            print(f"Pierdes el turno")
            continuar = False
        else:
            if tablero_maquina[j][i] == "B":
                tablero_maquina[j][i] = "X"
                tablero_disparos[j][i] = "X"
                print(f"Tocado en posición {i+1},{j}. Vuelves a disparar.")
                print("Registro de disparos humanos :")
                imprimir_tablero(tablero_disparos)  
                continuar = True
            elif tablero_maquina[j][i] == " ":
                tablero_maquina[j][i] = "O"
                tablero_disparos[j][i] = "O"
                continuar = False
                print(f"Agua en posición {i+1},{j}.")
                print("Registro de disparos humanos :")
                imprimir_tablero(tablero_disparos) 
            elif tablero_disparos[j][i] == "X" or tablero_disparos[j][i] == "O":
                continuar = False
                print(f"Posición {i+1},{j} ya había sido disparada. Pierdes tu turno")
            else:
                continuar = False
                print(f"Coordenada {i+1},{j}, inválida. Pierdes tu turno.")
    return continuar,tablero_maquina,tablero_disparos

#Función de la jugada máquina
def jugada_maquina(tablero_jugador):
    continuar = True
    while continuar == True:
        print()
        print("Esperando disparo de la máquina:")
        time.sleep(2)
        i, j = disparo_maquina()
        if tablero_jugador[j][i] == "B":
            tablero_jugador[j][i] = "X"
            continuar = True
            print(f"Tocado en posición {i+1},{j}. La máquina ha acertado.")
        elif tablero_jugador[j][i] == " ":
            tablero_jugador[j][i] = "O"
            continuar = False
            print(f"Agua en posición {i+1},{j}.")
        elif tablero_jugador[j][i] == "X" or tablero_jugador[j][i] == "O":
            continuar = False
            print(f"Posición {i+1},{j} ya había sido disparada.")
        else:
            continuar = False
            print(f"Coordenada {i+1},{j}, inválida.")
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