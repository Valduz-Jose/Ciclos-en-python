# Creacion y validacion de password
print("***Creación y validación de password***")
password = input("Ingrese su password (debe tener al menos 6 caracteres): ")

while len(password) < 6:
  print("Error: El password debe tener al menos 6 caracteres")
  password = input("Ingrese su password (debe tener al menos 6 caracteres): ")
else:
  print("Password creado exitosamente")