# ejemplo break

for numero in range (1, 10):
  if numero %2 ==0:
      print(numero)
      break
  print(numero)
  
  # break rompe el ciclo y sale de el, no se ejecuta el codigo que esta debajo del break
  print("\n\n\nCon Continue")
  for numero in range (1, 10):
    if numero %2 == 1:
      print(numero)
      continue