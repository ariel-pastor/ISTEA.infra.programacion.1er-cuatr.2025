"""

def sumar(a,b):
    resultado = a + b
    return resultado

sum1=int(input("Ingrese el primer numero a sumar: "))
sum2=int(input("Ingrese el segundo numero a sumar: "))

resultado_suma= sumar(sum1, sum2)

print ("El resultado de la suma es: ", resultado_suma)


"""
import os
os.system('cls')


def resta (num1, num2):
    resultado_resta= num1 - num2
    return resultado_resta

res1= int(input("Ingrese el primer numero a restar: "))
res2= int(input("Ingrese el segundo numero a restar: "))

numeros_restados= resta(res1, res2)

print ("Los numeros restados son: ", numeros_restados)
