

# scope: el alcance de una variable
# En Python, el "scope" (alcance) de una variable se refiere a la parte del código donde esa variable es accesible. Hay dos tipos principales de scope:
# 1. **Global Scope**: Variables definidas fuera de cualquier función. Son accesibles desde cualquier parte del código.
# 2. **Local Scope**: Variables definidas dentro de una función. Solo son accesibles dentro de esa función.

# Recuerden que nunca es buena practica usar variables globales, ya que pueden causar confusión y errores difíciles de rastrear. Siempre es mejor pasar variables como parámetros a las funciones.





# Definimos una función con variables locales
def dividir(a, b):
   resultado = a / b  # 'resultado' solo existe dentro de la función
   return resultado

division = dividir(10, 2)

print(division)  # Funciona bien

print(resultado)  # Esto dará un error porque 'resultado' no existe fuera de la función