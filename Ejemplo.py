# Clase padre
class Peces:
    def __init__(self, nombre, color, size, habitad):
        self._nombre = nombre  # Cambiado a protegido (_nombre) para permitir acceso en la clase hija
        self._color = color
        self._size = size
        self._habitad = habitad

    def nadar(self):
        print(f"{self._nombre} está nadando.")

    def mostrar_info(self):
        print(f"El pez se llama: {self._nombre}, Color: {self._color}, Tamaño: {self._size}, Habitad: {self._habitad}")

    # Método getter para obtener el nombre
    def getNombre(self):
        return self._nombre

    # Método setter para establecer el nombre
    def setNombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


# Clase hija
class PezPayaso(Peces):
    def __init__(self, nombre, color, size, habitad, esconderse):
        super().__init__(nombre, color, size, habitad)
        self._esconderse = esconderse

    def mostrar_info(self):
        super().mostrar_info()
        print(f"¿El pez se esconde? {'Sí' if self._esconderse else 'No'}")


# Ejemplo de uso de las clases
pez_payaso = PezPayaso("Nemo", "Naranja y blanco", "Pequeño", "Agua salada", True)

# Mostrar el nombre del pez usando el método getNombre()
print(f"Mi pez se llama {pez_payaso.getNombre()}")

# Cambiar el nombre del pez usando el método setNombre()
pez_payaso.setNombre("Dori")
print(f"Mi pez se llama {pez_payaso.getNombre()}")
