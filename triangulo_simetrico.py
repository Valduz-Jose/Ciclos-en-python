# dibujar un triangulo simetrico con asteriscos 
altura = int(input("Ingrese la altura del triangulo: "))
for i in range(1, altura + 1):
  print(" " * (altura - i) + "*" * (2 * i - 1))
  