cadena = "Hola Mundo".strip().lower()
vocales = 0
for letra in cadena:
    if letra in ["a","e","i","o","u"]:
        vocales+=1
print(vocales)