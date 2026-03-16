nombre_usuario = None

while not nombre_usuario:
  nombre_usuario = input("Ingrese su nombre de usuario: ")
  if not nombre_usuario:
    print("Error: El nombre de usuario no puede estar vacío. Por favor, ingrese un nombre de usuario válido.")
print(f"Nombre de usuario válido: {nombre_usuario}")