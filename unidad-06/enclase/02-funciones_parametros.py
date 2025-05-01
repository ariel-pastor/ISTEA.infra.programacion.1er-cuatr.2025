


def texto_imprimir( texto, caracter_cuadro ):
    print(caracter_cuadro * 30)
    print(caracter_cuadro * 30)
    print(caracter_cuadro * 30)
    print(texto)
    print(caracter_cuadro * 30)
    print(caracter_cuadro * 30)
    print(caracter_cuadro * 30)

def sumar( numero_uno, numero_dos):
    # La función sumar recibe dos números y retorna la suma de ellos.
    sub_total = numero_uno + numero_dos
    return sub_total

def restar( numero_uno, numero_dos):
    # La función restar recibe dos números y retorna la resta de ellos.
    sub_total = numero_uno - numero_dos
    return sub_total






texto_imprimir( "Ingresar un valor numerico: ", "*" )
valor_uno = int(input())
texto_imprimir( "Ingresar otro valor numerico: ", "*" )
valor_dos = int(input())

total_suma = sumar(valor_uno,valor_dos)
print(f"El total de la suma de los dos valores es: {total_suma}")

total_resta = restar(valor_uno,valor_dos)
print(f"El total de la resta de los dos valores es: {total_resta}")


