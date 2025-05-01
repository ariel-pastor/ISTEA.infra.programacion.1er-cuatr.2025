# - Intersección y diferencia de conjuntos
#     Crea dos funciones:  
#     1. Una que calcule la **intersección** (elementos comunes) entre dos listas.  
#     2. Otra que calcule la **diferencia** (elementos exclusivos) entre dos listas.  
#     Las funciones deben poder trabajar con listas de cualquier longitud y tipo de elemento.



def buscar_interseccion(lista1, lista2):
    """
    Función que calcula la intersección entre dos listas.
    """
    lista_interseccion = []

    for elemento in lista1:
        if elemento in lista2:
            lista_interseccion.append(elemento)
    return lista_interseccion




lista_uno = [1, 2, 3, 4, 5]
lista_dos = [4, 5, 6, 7, 8]

resultados_interseccion = buscar_interseccion(lista_uno, lista_dos)  

print(f"La intersección entre {lista_uno} y {lista_dos} es: {resultados_interseccion}")