# Ejercicios de Python

## 1. Ingresar números en una lista
Escribe un programa que solicite al usuario ingresar 5 números enteros y los almacene en una lista. Luego, imprime la lista resultante.

---

## 2. Ordenar nombres alfabéticamente
Crea una lista con los nombres de tus compañeros de clase. Imprime la lista y luego ordena los nombres en orden alfabético. Imprime la lista nuevamente para verificar el orden.

---

## 3. Generar lista de números pares
Escribe una función que genere una lista de los primeros 10 números pares y luego imprima la lista. A dicha función se le pasará como parámetro una lista de números. La función debe devolver una nueva lista con solamente los primeros diez números pares que encuentre.

---

## 4. Convertir cadena a lista de palabras
Desarrolla un programa que pida al usuario ingresar una lista de palabras separadas por comas. Luego, convierte esta cadena en una lista y la imprime.

---

## 5. Elevar números al cuadrado
Crea una lista con los números del 1 al 10. Utiliza un bucle para elevar cada número al cuadrado y almacenar el resultado en una nueva lista. Imprime la lista de cuadrados resultante.

---

## 6. Eliminar elementos duplicados
Escribe un programa que elimine todos los elementos duplicados de una lista y luego imprima la lista sin duplicados.

---

## 7. Buscar un elemento en una lista
Crea una función que busque un elemento específico dentro de una lista y devuelva su índice si lo encuentra, o un mensaje indicando que no lo encuentra.  
**Ejemplo:** `[1, 2, 3, 4, 5]`, buscando el elemento `3`, devuelve `2`.

---

## 8. Extraer una sublista
Escribe un programa que extraiga una sublista de una lista principal, especificando el índice inicial y el final (o la longitud de la sublista).  
**Ejemplo:** `[1, 2, 3, 4, 5, 6]`, extrayendo desde el índice `2` hasta el final, devuelve `[3, 4, 5, 6]`.

---

## 9. Contar vocales en una cadena
Crea una función llamada `contar_vocales` que reciba una cadena de texto como argumento y devuelva una lista con la cantidad de veces que aparece cada vocal.  
- En la posición `0` va la cantidad de veces que aparece la letra `a`.  
- En la posición `1` va la cantidad de veces que aparece la letra `e`.  
- Así sucesivamente para las vocales `i`, `o`, `u`.  
**Ejemplo:** Si la entrada es `"hola mundo"`, la salida debe ser:  
```python
[1, 0, 1, 2, 1]
```

---

## 10. Suma acumulativa
Crea una función llamada suma_acumulativa que reciba una lista de números como argumento y devuelva una nueva lista donde cada elemento sea la suma acumulativa de los elementos anteriores.
Ejemplo: Si la lista es [1, 2, 3, 4], la función debe devolver [1, 3, 6, 10].