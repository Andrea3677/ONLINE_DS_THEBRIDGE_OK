#Como base necesito tres tableros, los tableros de ambos jugadores y uno donde registrar los disparos que se hagan
tablero_maquina = crear_tablero(10)
tablero_jugador = crear_tablero(10)
tablero_disparos = crear_tablero(10)

#Generar las posiciones de los barcos

#Variables barco para el jugador humano
barcos_jh = {
"barco4_1" : [[9,2],[9,3],[9,4],[9,5]],
"barco3_1" : [[1,1],[2,1],[3,1]],
"barco3_2" : [[5,3],[5,4],[5,5]],
"barco2_1" : [[2,4],[2,5]],
"barco2_2" : [[5,7],[6,7]],
"barco2_3" : [[6,9],[7,9]],
"barco1_1" : [[7,4]],
"barco1_2" : [[2,8]],
"barco1_3" : [[10,8]],
"barco1_4" : [[4,10]],
}