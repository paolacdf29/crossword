import random
from classes.game import crossword
from classes.librerias import setofwords

ensalada = ['ensalada', 'papa', 'zanahoria', 'tomate', 'lechuga', 'aguacate', 'chia', 'quinoa']
dulces = ['dulces', 'torta', 'pie', 'caramelo', 'helado', 'gomitas', 'galletas', 'chocolate']
herramientas = ['herramientas', 'martillo', 'destornillador', 'cincel', 'sierra', 'caladora', 'llave', 'pega', 'tornillos']
deportes = ['deportes', 'futbol', 'basket', 'baseball', 'hockye', 'rugby', 'judo', 'taekwondo']

sets = setofwords([ensalada, dulces, herramientas, deportes])


settings = int(input('Como desea empezar su sopa de letras? \n 1. Configuracion predeterminada \n 2. Empezar desde cero: '))
if settings == 2:
    rows = int(input('Ingrese el numero de filas (Recomendado 10): '))
    cols = int(input('Ingrese el numero de columnas (Recomendado 10): '))
    crossword1 = crossword(rows, cols, [])
elif settings == 1:
    print('Se iniciara con una matriz de 10x10')
    wordsarr = sets.selectset()
    crossword1 = crossword(10, 10, wordsarr)
else:
    print('has seleccionado una opcion invalida')

crossword1.startcrossword()


running = True

while running:
    choice = input('Desea i-nsertar una palabra? \n 1. Si \n 2. No')
    if choice == '1':
        word = input('ingrese la palabra que desea')
        crossword1.insertword(word)
    elif choice == '2':
        crossword1.endcrossword()
        running = False

