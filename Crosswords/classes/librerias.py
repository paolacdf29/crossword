import random

class setofwords:
    def __init__(self, wordsarray):
        self.libreria = wordsarray

    def showtema(self, index):
        print('has elegido el siguiente conjunto de palabras')
        i = 0
        set = self.libreria[index]
        while i < len(set)-1:
            print(set[i] + ' '*(30-len(set[i])) + set[i+1])
            i += 2

        # for item in self.libreria[index]:
        #     print(item)

    def selectset(self):
        print('Seleccione el tema de las palabras que desea usar')
        index = 1
        for item in self.libreria:
            print(str(index) + '.' + item[0])
            index += 1

        temachoice = int(input('Que tema te gustaria elegir: ')) - 1
        if temachoice < 0 or temachoice >= len(self.libreria):
            return self.selectset()

        self.showtema(temachoice)

        finalchoice = int(input('Confirmas que deseas elegir estas palabras? \n 1.Si \n 2.No \n'))
        if finalchoice == 1:
            return self.libreria[temachoice]
        else:
            return self.selectset()
