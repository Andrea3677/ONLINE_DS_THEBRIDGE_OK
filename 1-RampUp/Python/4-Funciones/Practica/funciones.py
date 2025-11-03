def area_cuad (lado):
    return lado**2

def area_tri(base, altura):
    return (base*altura)/2

def area_cir(radio):
    return math.pi*(radio**2)

def fibonacci(numero):
    if numero <= 1:
        return 0
    elif numero == 1:
        return 1
    else:
        resultado = fibonacci(numero-1) + fibonacci(numero-2)
        return resultado
    
def unir (*args):
    return " ".join(args)

def eliminar(lista,comando,elemento = None):
    if comando == "add":
        lista.append(elemento)
        return lista
    elif comando == "remove":
        lista.remove(elemento)
        return lista
    else:
        return "Comando inválido"
    
def conversion_dict(cadena):
    diccionario ={}
    for indice, letra in enumerate(cadena):
        if letra in diccionario.keys():
            diccionario[letra].append(indice)
        else:
            diccionario[letra] = [indice]
    return diccionario


def contador_letras (cadena,letra):
    return cadena.count(letra)


def comparacion(numero1,numero2):
    if numero1 == numero2:
        return "Los numeros son iguales"
    elif numero1 > numero2:
        return "El primer numero es mayor que el segundo."
    else:
        return "El segundo numero es mayor que el primero."

def piramide(numero):
    for i in list(range(numero,0,-1)):
        for j in (range(i,0,-1)):
            print(j, end=" ")
        print()

def dia (numero):
    match numero:
        case 1:
            return "Lunes"
        case 2:
            return "Martes"
        case 3:
            return "Miércoles"
        case 4:
            return "Jueves"
        case 5:
            return "Viernes"
        case 6:
            return "Sabado"
        case 7:
            return "Domingo"
        case _:
            return "El dato introducido es inválido"