# Ejercicios de Python

## 1. Invierte una lista
Escribe un programa que invierta el orden de los elementos de una lista.  
**Ejemplo:** `[1, 2, 3, 4, 5]` se convierte en `[5, 4, 3, 2, 1]`.  
Primero resuélvelo manualmente. Luego, crea una función que lo haga automáticamente (puedes usar listas de hasta 100 números).

---

## 2. Elimina duplicados
Crea una función que elimine los elementos duplicados de una lista.  
**Ejemplo:** `[1, 2, 3, 1, 2, 4]` se convierte en `[1, 2, 3, 4]`.

---

## 3. Combina dos listas
Escribe una función que combine dos listas en una sola lista.  
**Ejemplo:** `[1, 2, 3]` y `[4, 5, 6]` se convierte en `[1, 2, 3, 4, 5, 6]`.

---

## 4. Intersección y diferencia de conjuntos
Crea dos funciones:  
1. Una que calcule la **intersección** (elementos comunes) entre dos listas.  
2. Otra que calcule la **diferencia** (elementos exclusivos) entre dos listas.  
Las funciones deben poder trabajar con listas de cualquier longitud y tipo de elemento.

---

## 5. Creación de una lista a partir de un rango
Escribe una función que genere una lista a partir de un rango de números especificado por el usuario. La función debe permitir definir el valor inicial, el valor final y el incremento (paso) entre los elementos.  
**Ejemplo:** Si el usuario define `inicio=1`, `fin=10`, `paso=2`, la lista generada será `[1, 3, 5, 7, 9]`.

---

## 6. Búsqueda en una lista
Implementa la búsqueda en una lista de números. La función debe recibir como parámetros la lista ordenada y el elemento a buscar. La función debe devolver el índice del elemento en la lista si lo encuentra, o un mensaje indicando que el elemento no está presente.  
No debes utilizar las funciones `index()` ni `find()` de Python. Debes hacer la búsqueda manualmente.

---

## 7. Lista de Saludos
Define una función llamada `saludar_lista` que tome una lista de nombres (strings) como parámetro.  
- La función debe iterar sobre la lista e imprimir un saludo personalizado para cada nombre.  
**Ejemplo de entrada:** `["Ana", "Carlos", "Sofía"]`  
**Ejemplo de salida:**  


---

## 8. Filtrar Palabras por Longitud
Define una función llamada `filtrar_por_longitud` que tome una lista de palabras (strings) y un número entero `n` como parámetros.  
- La función debe devolver una nueva lista que contenga solo las palabras de la lista original que tengan una longitud mayor o igual a `n`.

---

## 9. Buscar y Reemplazar en Lista
Define una función llamada `buscar_reemplazar` que tome una lista de strings, una palabra a buscar (string), y una palabra de reemplazo (string) como parámetros.  
- La función debe crear y devolver una nueva lista donde todas las ocurrencias de la palabra a buscar en los strings de la lista original sean reemplazadas por la palabra de reemplazo.

---

## 10. Lista de Números Pares e Impares
Define una función llamada `separar_pares_impares` que tome una lista de números enteros como parámetro.  
- La función debe devolver dos listas: una con los números pares y otra con los números impares de la lista original.

---

## 11. Verificar Elemento en Lista (Ignorando Caso)
Define una función llamada `verificar_elemento_ignorando_caso` que tome una lista de strings y un elemento a buscar (string) como parámetros.  
- La función debe devolver `True` si el elemento a buscar se encuentra en la lista (ignorando la diferencia entre mayúsculas y minúsculas), y `False` en caso contrario.

---

## 12. Ordenar Lista de Strings por Longitud
Define una función llamada `ordenar_por_longitud` que tome una lista de strings como parámetro.  
- La función debe devolver una nueva lista con los strings ordenados de menor a mayor longitud.

---

## 13. Juego de Adivinar la Palabra
Define una función llamada `jugar_adivinanza` que tome una palabra secreta (string) como parámetro.  
- La función debe permitir al usuario ingresar letras para adivinar la palabra.  
- Mantén un registro de las letras adivinadas y muestra el progreso de la palabra (con guiones bajos para las letras no adivinadas).  
- El juego termina cuando el usuario adivina la palabra completa o ingresa un número máximo de intentos fallidos (por ejemplo, 5).  
- La función debe imprimir un mensaje indicando si el jugador ganó o perdió.

---

## 14. Calculadora de Promedios (Ignorando Valores No Numéricos)
Define una función llamada `calcular_promedio_numerico` que tome una lista como parámetro.  
- La función debe calcular y devolver el promedio de los elementos que sean numéricos (`int` o `float`) en la lista. Los elementos no numéricos deben ser ignorados. Si no hay números en la lista, la función debe devolver `0`.

---

## 15. Combinar y Ordenar Listas de Palabras
Define una función llamada `combinar_ordenar_palabras` que tome dos listas de palabras (strings) como parámetros.  
- La función debe combinar ambas listas en una sola, eliminar los duplicados (ignorando el caso), convertir todas las palabras a minúsculas y luego ordenar la lista resultante alfabéticamente.

---

## 16. Analizador de Texto
Escribe una función llamada `analizar_texto` que reciba una cadena de texto como argumento y realice las siguientes operaciones:  
1. Cuente el número total de palabras.  
2. Encuentre la palabra más larga.  
3. Convierta todo el texto a minúsculas.  
4. Devuelva una lista con los resultados en la posicion 0 el total de palabras, en la posicion 1 la palabra más larga y en la posicion 2 el texto en minúsculas.

