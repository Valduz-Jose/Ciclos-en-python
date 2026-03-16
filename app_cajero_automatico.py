print("Aplicacion Cajero Automatico")
saldo = 1000
salir = False
while not salir:
  print(f"Operaciones disponibles: \n1. Consultar saldo \n2. Retirar dinero \n3. Depositar dinero \n4. Salir")
  opcion = input("Seleccione una opción: ")
  if opcion == "1":
    print(f"Su saldo actual es: {saldo}")
  elif opcion == "2":
    print("Ingrese la cantidad a retirar: ")
    cantidad = int(input())
    if cantidad > saldo:
      print("No tiene suficiente saldo para realizar esta operación")
    else:
      saldo -= cantidad
      print(f"Retiro exitoso, su nuevo saldo es: {saldo}")
  elif opcion == "3":
    print("Ingrese la cantidad a depositar: ")
    cantidad = int(input())
    saldo += cantidad
    print(f"Depósito exitoso, su nuevo saldo es: {saldo}")
  elif opcion == "4":
    salir = True
    print("Saliendo del programa...")
  else:
    print("Opción no válida, por favor seleccione una opción del menú")