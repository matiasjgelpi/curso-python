###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

import os
os.system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


### Completa aquí

print("Matías Gelpi", end="\n")
print("Mar del Plata")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("a es de tipo:", type(a))
print("b es de tipo:", type(b))
print("c es de tipo:", type(c))
print("d es de tipo:", type(d))
print("e es de tipo:", type(e)) 

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(int("12345"))
print(type(int("12345")))
print(float("12345"))
print(type(float("12345")))
print(int(3.99))

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "Matías Gelpi"
age = 39
height = 1.78

print(f"Hola {name}, tengo {age} años, mido {height} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


### Completa aquí
pi = 3.14159
print(round(pi))
print(int(round(pi) / 2))

