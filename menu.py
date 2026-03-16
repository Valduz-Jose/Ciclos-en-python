# Crear un menu para 3 opciones, crear cuenta, eliminar cuenta o salir
salir = False
while not salir:
  print("1. Crear cuenta")
  print("2. Eliminar cuenta")
  print("3. Salir")
  opcion = input("Seleccione una opción: ")
  
  if opcion == "1":
    print("Cuenta creada")
  elif opcion == "2":
    print("Cuenta eliminada")
  elif opcion == "3":
    print("Saliendo del programa...")
    salir =True
  else:
    print("Opción no válida, por favor seleccione una opción del menú")