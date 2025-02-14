###
# 02 - Bucles (for)
# Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

print("\nBucle for:")

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "midudev"
for caracter in cadena:
    print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
    print(f"El índice es {idx} y la fruta es {value}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")


# break
print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro está escondido en el índice {idx}")
        break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        continue

    print(animal)

# Comprensión de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

for par in range(2, 21, 2):
    print(par)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")


suma = 0
for n in numeros:
    suma += n

media = suma / len(numeros)
print(f"La media en {numeros} es {media}")


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [15, 5, 25, 110, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")

max = 0
for n in numeros:
    if n > max:
        max = n

print(f"El máximo dentro de {numeros} es {max}")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabrasLargas = []
for palabra in palabras:
    if len(palabra) > 5:
        palabrasLargas.append(palabra)

print(f"Palabras largas: {palabrasLargas}")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

letra = input("Ingresa solo una letra:").lower()
contador = 0

for palabra in palabras:
    if str.lower(palabra[0]) == letra:
        contador += 1

print(f"En {palabras} hay {contador} que empiezan con {letra}")
