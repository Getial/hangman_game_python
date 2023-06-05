import os
import random

INDICE_DE_IMAGEN_PERDEDORA = 10
INDICE_DE_IMAGEN_GANADORA = 11

def imprimir_logo():
    print('''

    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   █   █   █████   █   █   █████   █   █   █████   █   █   ║
    ║   █   █   █   █   ██  █   █       ██ ██   █   █   ██  █   ║
    ║   █████   █████   █ █ █   █████   █ █ █   █████   █ █ █   ║
    ║   █   █   █   █   █  ██   █   █   █   █   █   █   █  ██   ║
    ║   █   █   █   █   █   █   █████   █   █   █   █   █   █   ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
''')
          
def buscar_imagenes():
    """
    el numero_evento asciende dependiendo de las fallas que tenga el jugado,
    la imagen es un string sencillo con simbolos
    returns: diccionario de la forma: {numero_evento: imagen}
    """
    die0 = '''













'''
    die1 = '''







        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / '''+chr(92)+'''
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: die11}
    return deaths

def imprimir_juego_actual(imagenes, muertes, letras, letra_invalida=False):
    os.system('clear')
    imprimir_logo()
    print(f'Letras disponibles: {" ".join(letras)}')
    print(imagenes.get(muertes))

    if letra_invalida:
        print('Debes ingresar una de las letras disponibles')

def devolver_palabra(descubiertas, quitar_espacios=True):
    """devuelve la palabra como string"""
    palabra = ''.join(descubiertas)
    return palabra.replace(' ', '') if quitar_espacios else palabra

def escoger_palabra():
    with open('archivos/data.txt', 'r', encoding='utf-8') as diccionario:
        contenido = diccionario.read() #lee el archivo entero como un string, los saltos de linea se representan por \n
        contenido = contenido.upper() #convierte el contenido a mayusculas
        palabras = contenido.split('\n') # convierte el string en un arreglo de palabras, separando los saltos de linea
        palabra = random.choice(palabras)

    caracteres_para_remplazar = {'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U'} # diccionario de la forma: {letra_a_remplazar: por_letra, ...}
    for letra_remplzada, por_letra in caracteres_para_remplazar.items():
        palabra = palabra.replace(letra_remplzada, por_letra)

    return palabra

def comparar_letras(letra_elegida, palabra, descubiertas):
    """
    Mira si la letra elegida esta en la palabra para adivinar, si es asi modifica el arreglo de letras descubiertas
    returns:
    descubiertas: el arreglo de letras descubiertas modificado con la nueva letra.
    fallo: booleano indicando si fallo o no la busqueda de esa letra en la palabra.
    """
    fallo = True
    for indice, letra_palabra in enumerate(palabra):
        if letra_palabra == letra_elegida:
            descubiertas[indice] = letra_elegida + ' '
            fallo = False
    return descubiertas, fallo

def elige_si():
    while True:
        otra_vez = input('Quieres jugar otra vez? (S/n):  ')
        if otra_vez.lower() in ('s', 'n'):
            return otra_vez.lower() == 's'
        else:
            print('Elige (s)i o (n)o')

def nueva_palabra():
    """
    Escoge una palabra y calcula sus propiedades
    palabra: una palabra aleatoria de nuestro diccionario
    indice_letra: diccionario de la forma {indice: letra}
    descubiertas: arreglo con las letras como se visualizan en el juego, ejemplo: ['B', ' -', 'R', 'C', ' -']
    muertes: numero de veces que ha errado
    letras_disponibles: letras con las que dispone para jugar, empieza con el abcdario completo y va disminuyendo las letras que se han usado
    """

    palabra = escoger_palabra()
    indice_letra = {i[0]: i[1] for i in enumerate(palabra)}
    descubiertas = ['- ' for _ in range(len(indice_letra))]
    muertes = 0
    letras_disponibles = ['A','B','C','D','E','F','G','H',
               'I','J','K','L','M','N','Ñ','O',
               'P','Q','R','S','T','U','V','W',
               'X','Y','Z']
    return palabra, indice_letra, descubiertas, muertes, letras_disponibles

def perder(muertes, imagenes, letras_disponibles, palabra):
    """Devuelve si la persona ha perdido, en casso de que si imprime el final del juego"""
    if muertes == INDICE_DE_IMAGEN_PERDEDORA:
        imprimir_juego_actual(imagenes, INDICE_DE_IMAGEN_PERDEDORA, letras_disponibles)
        print(f'Perdiste! La palabra era {palabra}')
        return True
    else:
        return False
    
def ganar(muertes, imagenes, letras_disponibles, palabra, descubiertas):
    """devuelve si la persona ha ganado, en caso de que si imprime el final del juego"""
    if devolver_palabra(descubiertas) == palabra:
        imprimir_juego_actual(imagenes, INDICE_DE_IMAGEN_GANADORA, letras_disponibles)
        print(f'Tuviste {muertes} errores, la palabra era:   {devolver_palabra(descubiertas)}')
        return True
    else:
        return False

def correr():
    #trae las imagenes que utilizaremos conforme avance el juego
    imagenes = buscar_imagenes()

    letra_invalida = False
    palabra, indice_letra, descubiertas, muertes, letras_disponibles = nueva_palabra()

    while True:
        imprimir_juego_actual(imagenes, muertes, letras_disponibles, letra_invalida=letra_invalida)

        letra_invalida = False
        letra = input(f'''¡Adivina la palabra!     {devolver_palabra(descubiertas, quitar_espacios=False)}
Ingresa una letra: ''').upper()
        
        try:
            indice = letras_disponibles.index(letra)
            letras_disponibles[indice] = ''
        except ValueError:
            letra_invalida = True
            continue

        descubiertas, fallo = comparar_letras(letra, palabra, descubiertas)
        if fallo:
            muertes += 1

        is_perdio = perder(muertes, imagenes, letras_disponibles, palabra)
        is_gano = ganar(muertes, imagenes, letras_disponibles, palabra, descubiertas)

        if is_perdio or is_gano: 
            if elige_si():
                palabra, indice_letra, descubiertas, muertes, letras_disponibles = nueva_palabra()

            else:
                print("Gracias por jugar :)")
                break
        


if __name__ == '__main__':
    os.system('clear')
    correr()