


import os
os.system('cls')


# 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.
"""
base = 5
altura = 3

area_rectangulo = base * altura

print(f"El área de un rectángulo con base {base} y altura {altura} es: ", area_rectangulo)
"""

# 2. Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y luego imprime la temperatura equivalente en Fahrenheit.

"""
temp_celsius = int(input("Ingrese la temperatura en grados Celsius: "))

temp_fahren = temp_celsius * 1.8 + 32

print(f"La temperatura ingresada {temp_celsius} en grados Celsius es equivalente en grados Fahrenheit a {temp_fahren}")
"""

# 3. Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato de esa variable.

"""
nombre = input("Ingrese su nombre: ")
edad = input ("Ingrese su edad: ")

nom_y_edad = nombre + edad

print (f"Usted ha ingresado el nombre: {nombre} y la edad: {edad} que son de tipo: {type(nom_y_edad)}")
"""


# 4. Calcula el área de un círculo con radio 4. Imprime el resultado.

"""
pi = 3.1416

radio = int(input("Ingrese el radio: "))

area = pi * radio **2

print (f"El area calculada de un circulo con radio: {radio} es {area}")
"""

# 5. Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números.

"""
num1 = int (input ("Ingrese el primero de los numeros: "))
num2 = int (input ("Ingrese el segundo de los numeros: "))

suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2

print ("El resultado de la suma es: ", suma)
print ("El resultado de la resta es: ", resta)
print ("El resultado de la multiplicacion es: ", multi)
print ("El resultado de la division es: ", div)
"""

# 6. Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.

"""
resultado = (5 + 3) * 2 / (4 - 1) ** 2
print("Resultado:", resultado)
print("Tipo de dato:", type(resultado))
"""

# 7. Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado.

nota = int(input("Ingrese la nota del alumno: "))
aprobado = False

if nota >= 7:
    aprobado = True
    print(f"El alumno se encuentra aprobado con la nota {nota}")
else:
    print("El alumno no se encuentra aprobado")

print("Estado de aprobado:", aprobado)

# 8. Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado.

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.

# 10. Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato.



