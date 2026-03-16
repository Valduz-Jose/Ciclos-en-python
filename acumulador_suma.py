MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
  print(f"(acumulador_suma + numero): {acumulador_suma} + {numero}")
  acumulador_suma += numero
  numero += 1
  
print(f"La suma de los números del 1 al {MAXIMO} es: {acumulador_suma}")