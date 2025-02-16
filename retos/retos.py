""" 
En el universo de los 4 Fantásticos, la unión y el equilibrio entre los poderes es clave para enfrentar desafíos. En este ejercicio, nos centraremos en dos miembros de la alianza:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.
El objetivo es crear una función en Python que reciba una cadena de texto y cuente cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J (para Johnny Storm). La función debe tener los siguientes comportamientos:

Si la cantidad de R y la cantidad de J son iguales, la alianza está en equilibrio y la función debe retornar True.
Si las cantidades no son iguales, la función debe retornar False.
Si no aparece ninguna de las dos letras en la cadena, se considera que el equilibrio se mantiene, por lo que la función debe retornar True.

"""

prueba = "452wwrrjjfw"


def check(text=""):
    countR = text.upper().count("R")
    countJ = text.upper().count("J")

    return countJ == countR


""" 
En Jurassic Park, los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. 
En este ejercicio, se nos proporciona una lista de números enteros que representan la cantidad de huevos puestos por diferentes dinosaurios en el parque.

Objetivo
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros,
es decir, la suma de todos los números pares en la lista.

"""


def egg_count(eggs):
    carnivores_eggs = [egg for egg in eggs if egg % 2 == 0]

    for egg in carnivores_eggs:
        count += egg

    return count


print(egg_count([5, 7, 9]))


"""
Dado un array de números y un número objetivo (goal), necesitamos encontrar los dos primeros números en el array cuya suma sea igual a ese número objetivo.
Si existe tal combinación, la función debe devolver los índices de estos dos números. Si no se encuentra ninguna combinación, debe devolver None.

"""


def find_first_sum(nums, goal):
    # Recorrer todos los pares posibles de números en el array
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]  # Devolver los índices de la combinación

    return None
