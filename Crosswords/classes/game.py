import random
import re

class crossword:
    def __init__(self, rw, cl, wrds):
        self.rows = rw
        self.cols = cl
        self.words = wrds
        self.matrix = []
        self.retrys = 0
        self.fullindex = (70 * (rw * cl)) / 100
        self.fullboxes = 0

    def printcross(self):
        for col in self.matrix:
            print(col)

    def checkword(self, word):
        # Revisa si la palabra entra en la matriz
        # Checking if the words fits in the matrix
        i = 0
        while i < len(word):
            if not(re.match('[a-z]|ñ', word[i])):
                print('esta no es una palabra valida')
                return False
            i += 1

        if len(word) > self.rows and len(word) > self.cols:
            print('La palabra' + word + ' no se puede ingresar a la matriz')
            return False

        else:
            print(word,  'Es del tamaño correcto')
            return True

    def checkdiagonal(self, irow, icol, newrow):
        # Revisa si hay espacio para insertar la palabra en un punto de una diagonal determinada
        # check if is possible to insert the word at specific point in diagonal
        iword = 0
        while irow < self.rows and icol < self.cols and iword < len(newrow):
            if self.matrix[irow][icol] != ' ' and self.matrix[irow][icol] != newrow[iword]:
                return False
            irow += 1
            icol += 1
            iword += 1
        return True

    def checkspot(self, row, col, word, Pchoice):
        # Chequea si se puede poner una palabra en un punto determinado sin afectar otras palabras
        # Check if the word can be placed at a specific point without stepping into another word
        iword = 0
        if Pchoice == 'H':
            # Si la palabra sera colocada en horizontal
            # If the word is goint to be placed in horizontal
            rows = self.matrix[row]
            print(rows, '\n')
            index = col
        elif Pchoice == 'V':
            # Si la palabra sera colocada en Vertical
            # If the word is goint to be placed in Vertical
            # 'rows' es de hecho una columna
            # 'rows' is actually a column
            rows = []
            for columna in self.matrix:
                rows.append(columna[col])
            print(rows, '\n')
            index = row
        elif Pchoice == 'D':
            # Si la palabra sera colocada en Diagonal
            # If the word is goint to be placed in Diagonal
            print('\n')
            return self.checkdiagonal(row, col, word)

        # Una vez tenemos la fila/columna y la posicion donde se encontrara la palabra se chequea el recorrido
        # Now that we have the row/col and the position where is going to be the word we check
        while index < len(rows) and iword < len(word):
            if rows[index] != ' ' and rows[index] != word[iword]:
                return False
            index += 1
            iword += 1
        return True

    def startpoint(self, word, Pchoice):
        # esta funcion busca un punto aleatorio donde colocar la palabra
        # this function look for a random point to place the word
        if Pchoice == 'H':
            # La palabra se insertara en posicion Horizontal
            lim = self.cols - (len(word) - 1)
            colstartpoint = random.randrange(0, lim)
            rowstartpoint = random.randrange(0, self.rows - 1)

        elif Pchoice == 'V':
            # La palabra se insertara en posicion Vertical
            lim = self.rows - (len(word) - 1)
            colstartpoint = random.randrange(0, self.cols - 1)
            rowstartpoint = random.randrange(0, lim)

        elif Pchoice == 'D':
            # La palabra se insertara en diagonal
            limR = self.rows - len(word)
            limC = self.cols - len(word)
            rowstartpoint = random.randrange(0, limR)
            colstartpoint = random.randrange(0, limC)

        print('La palabra se intentara insertar en este punto', rowstartpoint, colstartpoint)
        if self.checkspot(rowstartpoint, colstartpoint, word, Pchoice):
            return [rowstartpoint, colstartpoint], Pchoice
        else:
            print('No se pudo insertar, Buscando un nuevo punto de partida')
            if self.retrys < 20:
                self.retrys += 1
                Pchoice = random.choice(['H', 'V', 'D'])
                return self.startpoint(word, Pchoice)
            else:
                print('no se puede insertar esta palabra')
                return [0, 0], 'X'

    def wordIntoMatrix2(self, newrow, startpoint, Pchoice):
        # Dependiendo de la posicion en la que se pondra se manda a uno de estos metodos

        if Pchoice == 'H':
            self.recorrerFila(startpoint[0], startpoint[1], newrow)

        elif Pchoice == 'V':
            self.recorrerColumna(startpoint[0], startpoint[1], newrow)

        elif Pchoice == 'D':
            self.recorrerDiagonal(startpoint[0], startpoint[1], newrow)

        self.printcross()

    def recorrerFila(self, irow, icol, newrow):
        iword = 0
        while icol < self.cols and iword < len(newrow):
            self.matrix[irow][icol] = newrow[iword]
            icol += 1
            iword += 1

    def recorrerColumna(self, irow, icol, newrow):
        iword = 0
        while irow < self.rows and iword < len(newrow):
            self.matrix[irow][icol] = newrow[iword]
            irow += 1
            iword += 1

    def recorrerDiagonal(self, irow, icol, newrow):
        iword = 0
        while irow < self.rows and icol < self.cols and iword < len(newrow):
            self.matrix[irow][icol] = newrow[iword]
            irow += 1
            icol += 1
            iword += 1

    def insertword(self, word):
        self.retrys = 0
        if self.checkword(word):
            #Si la palabra no se encuentra en el array de palabras se insertara
            self.fullboxes += len(word)
            if word not in self.words:
                self.words.append(word)

            # Se elige de manera aleatoria si la palabra sera colocada al reves o no
            # This choose randomly if the word is goin to be upside down or not
            orden = ['derecho', 'reves']
            if random.choice(orden) == 'derecho':
                newrow = list(word)
            else:
                newrow = list(word)
                newrow.reverse()

            # Se selecciona aleatoriamente si la palabra sera colocada en horizontal, vertical o diagonal
            # this ramdonly select if the words is going to be placed Horizontal, Vertical or Diagonal

            position = ['H', 'V', 'D']
            Pchoice = random.choice(position)

            # Se busca un punto donde se colocara la primera letra
            # Looking for a random point to start
            startpoint, Pchoice = self.startpoint(newrow, Pchoice)
            if Pchoice != 'X':
                # Se coloca la palabra en la matriz en la posicion seleccionada
                # Actually putting the word into the matrix at the selected point
                self.wordIntoMatrix2(newrow, startpoint, Pchoice)

    def startcrossword(self):
        # Inicializa una matriz vacia con el numero de filas y columnas que se crea
        # Start an empty matrix whit the number of rows and columns that is created
        col = []
        i = 0
        j = 0
        while i < self.cols:
            col.append(' ')
            i += 1
        while j < self.rows:
            self.matrix.append(list.copy(col))
            j += 1

        self.printcross()
        # Se insertan en la matriz las palabras con las que se inicializo
        # Insert into the matrix the initials words
        for item in self.words:
            if self.fullboxes <= self.fullindex:
                self.insertword(str(item))
            else:
                print('No se pudo ingresar, la sopa de letras tiene demasiadas palabras')

    def rellenarmatrix(self):
        # Se llenan los espacios vacios de la matriz con letras aleatorias
        # Fills the empty spaces of the matrix with random letters
        lettersarray = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        icol = 0
        while icol < self.cols:
            irow = 0
            while irow < self.rows:
                if self.matrix[irow][icol] == ' ':
                    letter = random.choice(lettersarray)
                    self.matrix[irow][icol] = letter
                irow += 1
            icol += 1

    def endcrossword(self):
        # Finaliza el proceso de creacion de la sopa de letras y se imprime para el juego
        # Ends the creation process of the crossword and print it ready to play
        self.rellenarmatrix()
        print('\n Esta es tu sopa de letras \n')
        self.printcross()
        print('\n Estas son las palabras dentro de la sopa de letras \n')

        i = 0
        while i < len(self.words):
            print(self.words[i] + ' '*(30-len(self.words[i])) + self.words[i+1])
            i += 2


