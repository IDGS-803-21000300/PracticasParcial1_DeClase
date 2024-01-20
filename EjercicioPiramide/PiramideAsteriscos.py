
class PiramideAsteriscos:

    cantidad = 0

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def crear(self):

        asteriscos = "*"

        for i in range(self.cantidad):
            print("*" * (i + 1))
    
def main(cantidad):
    obj = PiramideAsteriscos(cantidad)
    obj.crear()

if __name__ == "__main__":
    main()