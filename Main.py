from classPezPayaso import PezPayaso  # Importa solo la clase PezPayaso

# Ejemplo de uso de las clases
pez_payaso = PezPayaso("Nemo", "Naranja y blanco", "Pequeño", "Agua salada", True)  # Instanciar el pez

# Mostrar la información del pez
pez_payaso.mostrar_info()  # Muestra la información del pez
pez_payaso.nadar()  # Llama al método nadar

# Mostrar el nombre del pez usando el método getNombre()
print(f"Mi pez se llama {pez_payaso.getNombre()}")

# Cambiar el nombre del pez usando el método setNombre()
pez_payaso.setNombre("Dori")
print(f"Mi pez se llama {pez_payaso.getNombre()}")


