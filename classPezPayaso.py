# classPezPayaso.py

from classPeces import Peces  # Asegúrate de importar la clase base

# Clase hija
class PezPayaso(Peces):
    def __init__(self, nombre, color, size, habitad, esconderse):
        super().__init__(nombre, color, size, habitad)
        self._esconderse = esconderse

    def mostrar_info(self):
        super().mostrar_info()  # Mostrar info del padre
        print(f"El color del pez es: {self._color}")  # Imprimir el color desde la clase padre
        print(f"Este pez se esconde? {self._esconderse}")  # Imprimir si se esconde como True o False

    def getColor(self):
        return self.color
