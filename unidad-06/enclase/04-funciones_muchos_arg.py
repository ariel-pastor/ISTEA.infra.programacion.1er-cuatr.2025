


def numeros(*numeros):
    sub_total = 0  # Inicializamos el acumulador
    
    # Iteramos sobre cada número recibido en la tupla *numeros
    for num in numeros:
        sub_total += num  # Sumamos cada número al subtotal
    
    return sub_total  # Retornamos la suma total


# Llamamos a la función con varios valores
total = numeros(2, 4, 6, 8, 10)

# Imprimimos el resultado con un mensaje descriptivo
print(f"El total de la suma de los valores es: {total}")





"""


#### 1. `*numeros` - Argumentos variables
- El símbolo `*` antes del nombre del parámetro (`numeros`) permite que la función acepte **un número variable de argumentos**.
- Internamente, estos argumentos se almacenan como una **tupla**.
- Esto es útil cuando no sabes cuántos valores va a recibir tu función.

#### 2. Acumulador (`sub_total`)
- Se inicializa en `0`, y luego se va sumando cada valor dentro del bucle `for`.
- Este concepto es común en programación para realizar cálculos iterativos (como sumas, promedios, etc.).

#### 3. Bucle `for`
- Itera sobre cada elemento dentro de la tupla `numeros`.
- En cada iteración, el valor actual (`num`) se agrega al acumulador.

#### 4. `return sub_total`
- Devuelve el valor final del acumulador, es decir, la suma total de todos los números.

#### 5. Llamada a la función
- `numeros(2, 4, 6, 8, 10)` pasa cinco valores a la función.
- Estos valores son sumados y el resultado se asigna a la variable `total`.

#### 6. `print(...)`
- Muestra el resultado final al usuario en consola.
- Usa una **f-string** para insertar variables directamente en el texto.

#### 7. `exit()`
- Finaliza la ejecución del programa.
- Opcional, ya que Python termina automáticamente al llegar al final del script.

---

### ✅ Ventajas de esta versión mejorada:

- ✅ **Claridad**: Nombres significativos y comentarios útiles.
- ✅ **Mantenibilidad**: Fácil de entender y modificar en el futuro.
- ✅ **Documentación interna**: Uso de `docstring` para documentar funciones.
- ✅ **Cumple PEP8**: Formato limpio y estándar oficial de Python.

"""