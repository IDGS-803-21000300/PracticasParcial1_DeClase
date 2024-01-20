
class Lista:

    def __init__(self) :
        
        self.listaNormal = []
        self.listaOrdenada = []
        self.numerosPares = []
        self.numerosImpares = []
        self.vecesRepetidos = []
    
    def pedirNumeros(self):

        rango = int(input("Cuantos numeros vas a ingresar padrino! "))
        for i in range(rango):
            add = int(input("Ingresa el numero:   "))
            self.listaNormal.append(add)
    
    def generar(self):

        self.listaOrdenada = sorted(self.listaNormal)
        
        for num in self.listaOrdenada:
            if num % 2 == 0:
                self.numerosPares.append(num)
            else:
                self.numerosImpares.append(num)
        
        if self.listaOrdenada.count(num) > 1:
                self.vecesRepetidos.append((num, self.listaOrdenada.count(num)))

    
    def imprimir(self):
        print("_____________________________________")
        print("Lista Normal: ", self.listaNormal)
        print("_____________________________________")
        print("Lista Ordenada  ", self.listaOrdenada)
        print("_____________________________________")
        print("numeros Pares  ", self.numerosPares)
        print("_____________________________________")
        print("Numeros Impares   ", self.numerosImpares)
        print("_____________________________________")
        print("Números repetidos y sus repeticiones: ", self.vecesRepetidos)
        print("_____________________________________")

def main():
    obj = Lista()
    obj.pedirNumeros()
    obj.generar()
    obj.imprimir()

if __name__ == "__main__" :
    main()

