



# subcadena_uno = "mi"
# subcadena_dos = "la"
# subcadena_tres = "ne"
# subcadena_cuatro = "sas"

# # concatenar
# cadena_total = subcadena_uno + subcadena_dos + subcadena_tres + subcadena_cuatro

# # print(cadena_total)


# # Uso de len()
# longitud_cadena = len(cadena_total)
# # print(" La longitud de la cadena es: ", longitud_cadena)

# # exit()
# #########################################################


# # Uso de index() -> nos va a devolver el indice de la primera ocurrencia de la subcadena que le pasamos como argumento

# # cadena = "Python es un lenguaje de alto nivel"

# # indice = cadena.index("h")

# # print("El indice de la palabra 'lenguaje' es: ", indice)

# # exit()


# #########################################################


# # Vamos a probar las diferentes maneras de ver los indices de una cadena


# cadena = "Python es un lenguaje de alto nivel"

# print(cadena[13:16])
# # salida: P

# exit()

# print(cadena[0:10])
# # salida: Python es

# print(cadena[10:20])
# # salida: un lenguaj

# print(cadena[0:20:2])
# # salida: Pto su ega

# cadena = "Python es un lenguaje de alto nivel"
# print(cadena[:-2])
# # salida: Python es un lenguaje de alto nive
 
# print(cadena[-1])
# # salida: l



# #########################################################



# # in y not in -> nos va a devolver True si la subcadena que le pasamos como argumento está en la cadena, False en caso contrario

numero_uno = input("Ingrese un número: ")

if numero_uno.isdigit():
    print("El string ingresado es un número")
else:
    print("El string ingresado no es un número")




print("Fin del programa")


