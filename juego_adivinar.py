# el jugador debe adivinar un numero entre 1 y 50 , llevar el conteo de intentos y mostrar un mensaje de felicitaciones al adivinar el numero ademas mostrar si el numero que dijo es mayor o menor al que debe adivinar, al final mostrar el numero de intentos que le tomo adivinar el numero

from random import randint
numero_secreto = randint(1, 50)
intentos = 0
print("Bienvenido al juego de adivinar el numero secreto entre 1 y 50")
adivinanza = None

while adivinanza != numero_secreto:
  adivinanza = int(input("Ingrese su adivinanza: "))
  intentos += 1
  
  if adivinanza < numero_secreto:
    print("El numero secreto es mayor que su adivinanza")
  elif adivinanza > numero_secreto:
    print("El numero secreto es menor que su adivinanza")
  else:
    print(f"Felicitaciones! Has adivinado el numero secreto en {intentos} intentos")