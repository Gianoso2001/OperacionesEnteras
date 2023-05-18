class OperacionesEnteras:
    def MCD(self, numero1, numero2):
        return None

    def MCD(self, numero1, numero2):
        temporal = 0

    while numero2 != 0:
        temporal = numero2
        numero2 = numero1 % numero2
        numero1 = temporal
    return numero1

def __init__(self):
    self.numeros = numeros
       def calcularMCD(self):
           if len(self.__numeros) < 2:
               raise numeroParametros
       elif len(self.__numeros) == 2:
       return self.MCD(self.__numeros[0], self.__numeros[1])
       elif len(self.__numeros) == 3:
       return None
       else:
       return None
       def MCD(self, numero1, numero2):
           temporal = 0
         while numero2 != 0:
              temporal = numero2
         numero2 = numero1 % numero2
         numero1 = temporal
           return numero1

            def MCDMasDosNumeros(self):
                cantidadNumeros = len(self.__numeros)

            mcd = self.MCD(self.__numeros[0], self.__numeros[1])
            i = 0
            while (i < (cantidadNumeros - 2)):
                mcd = self.MCD(mcd, self.__numeros[i + 2])
            i = i + 1
            return mcd