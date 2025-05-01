def reemplazar_vocales(lista_palabras):
    lista_modificada = []
    for palabra in lista_palabras:
        nueva_palabra = ''
        for letra in palabra:
            if letra.lower() in 'aeiou':
                nueva_palabra += '*'
            else:
                nueva_palabra += letra
        lista_modificada.append(nueva_palabra)
    return lista_modificada

# Ejemplo de uso
lista_original = ['cuartirolo', 'papa', 'perro']
lista_modificada = reemplazar_vocales(lista_original)

print("Lista original:", lista_original)
print("Lista modificada:", lista_modificada)