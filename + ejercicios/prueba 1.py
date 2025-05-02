
for numero_entero in range(10,21, 2):
    print ("Valor del numero: ", numero_entero)

# Pedimos al usuario que ingrese un año
año = int(input("Ingrese un año: "))

# Verificamos si es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")


cadena = "python es un leguaje"

indice = cadena.index("un")
print("el indice de la palabra 'un' es: ", indice)

exit()


