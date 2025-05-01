

def saludar(nombre, saludo = "Hola"):
   
    print(f"{saludo}, {nombre}!")

# Caso 1: Usando solo el parámetro posicional
saludar("Carlos")
# Salida: Hola, Carlos!

# Caso 2: Usando también un keyword argument
saludar("Laura", saludo="Buenos días")
# Salida: Buenos días, Laura!

# Caso 3: Cambiando el orden usando keywords
saludar("María", saludo="Bienvenida")
# Salida: Bienvenida, María!