# Calculadora para sumar restar multiplicar o dividir
print("***Calculadora en Python")

salir = False

while not salir:
  print("Operaciones disponibles: \n1. Sumar \n2. Restar \n3. Multiplicar \n4. Dividir \n5. Salir")
  opcion = input("Seleccione una opción: ")
  
  if opcion in ["1", "2", "3", "4"]:
    print("Ingrese el primer número: ")
    num1 = float(input())
    print("Ingrese el segundo número: ")
    num2 = float(input())
    
    if opcion == "1":
      resultado = num1 + num2
      print(f"El resultado de la suma es: {resultado}")
    elif opcion == "2":
      resultado = num1 - num2
      print(f"El resultado de la resta es: {resultado}")
    elif opcion == "3":
      resultado = num1 * num2
      print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
      if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
      else:
        print("Error: No se puede dividir por cero")
        
  elif opcion == "5":
    salir = True
    print("Saliendo del programa...")
  else:
    print("Opción no válida, por favor seleccione una opción del menú")