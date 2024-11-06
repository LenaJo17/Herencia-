
# Clase padre
class Peces:
    def __init__(self, nombre, color, size, habitad):
        self._nombre = nombre  # Atributo protegido
        self._color = color  # Atributo protegido
        self._size = size  # Atributo protegido
        self._habitad = habitad  # Atributo protegido

    def nadar(self):
        print(f"{self._nombre} está nadando.")  # Mensaje al nadar

    def mostrar_info(self):
        print(f"El pez se llama: {self._nombre}, es de color: {self._color}, y vive en: {self._habitad}")

    # Método getter para obtener el nombre
    def getNombre(self):
        return self._nombre

    # Método setter para establecer el nombre
    def setNombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


