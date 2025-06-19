# List of Math Operators

En el video anterior, aprendiste cómo hacer una suma en Python. A continuación, se muestra la lista completa de operadores matemáticos que podés usar en Python:

---

### ➕ Addition (`+`)

```python
print(3 + 4)
```

**Output:**
```
7
```

---

### ➖ Subtraction (`-`)

```python
print(3 - 4)
```

**Output:**
```
-1
```

---

### ✖️ Multiplication (`*`)

```python
print(3 * 4)
```

**Output:**
```
12
```

---

### ➗ Division (`/`)

```python
print(3 / 4)
```

**Output:**
```
0.75
```

---

### 🔽 Floor Division (`//`)

```python
print(9 // 2)
```

**Output:**
```
4
```

**Explicación:**  
Si tu habitación tiene nueve metros de alto, podrías colocar cuatro armarios de 2 metros uno encima del otro.

---

### 🧮 Modulus (`%`)

```python
print(9 % 2)
```

**Output:**
```
1
```

**Explicación:**  
Si tu habitación tiene nueve metros de alto, podrías colocar cuatro armarios de 2 metros uno encima del otro. Sobraría un metro de espacio vertical.

---

### 🔢 Exponentiation (`**`)

```python
print(3 ** 4)
```

**Output:**
```
81
```

**Explicación:**  
`3 ** 4` es equivalente a `3 * 3 * 3 * 3`.

---
# 🧠 Cheatsheet: Data Types

En esta sección aprendiste que:

---

### 🔢 Integers
Representan números enteros:

```python
rank = 10
eggs = 12
people = 3
```

---

### 🌡️ Floats
Representan números decimales:

```python
temperature = 10.2
rainfall = 5.98
elevation = 1031.88
```

---

### 📝 Strings
Representan texto:

```python
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
```

---

### 📦 Lists
Representan arreglos de valores que pueden cambiar durante el programa:

```python
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
```

---

### 🔑 Dictionaries
Representan pares clave-valor:

```python
phone_numbers = {
  "John Smith": "+37682929928",
  "Marry Simpons": "+423998200919"
}

volcano_elevations = {
  "Glacier Peak": 3213.9,
  "Rainer": 4392.1
}
```

Obtener **claves** de un diccionario:

```python
phone_numbers.keys()
```

Obtener **valores** de un diccionario:

```python
phone_numbers.values()
```

---

### 🔒 Tuples
Representan arreglos de valores que **no deben cambiar** durante el programa:

```python
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```

---

### 🛠️ Utilidades para inspeccionar objetos

📄 Ver atributos/métodos de un tipo de dato:

```python
dir(str)
dir(list)
dir(dict)
```

📦 Ver funciones integradas de Python:

```python
dir(__builtins__)
```

📚 Ver documentación de un tipo o función:

```python
help(str)
help(str.replace)
help(dict.values)
```

---
# 🔄 Tip: Converting Between Datatypes

A veces necesitás convertir entre diferentes tipos de datos en Python. ¡Es muy fácil!

---

### 🧊 De **tupla** a **lista**

```python
cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list)  # [1, 2, 3]
```

---

### 📦 De **lista** a **tupla**

```python
cool_list = [1, 2, 3]
cool_tuple = tuple(cool_list)
print(cool_tuple)  # (1, 2, 3)
```

---

### 🧵 De **string** a **lista**

```python
cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list)  # ['H', 'e', 'l', 'l', 'o']
```

---

### 🔤 De **lista** a **string**

```python
cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string)  # 'Hello'
```

💡 Como ves, convertir una lista a string es un poco más complejo. `str()` no es suficiente, necesitamos `str.join()`.

Podés probar también con separadores personalizados:

```python
print(str.join("---", cool_list))  # 'H---e---l---l---o'
```

Así vas a entender cómo funciona `str.join()` combinando los elementos de una lista con un separador.

---
# 🧠 Cheatsheet: Operations with Data Types

En esta sección aprendiste que:

---

### 📌 Índices en listas, strings y tuplas

Usan un sistema de índices positivos:

```python
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
```

Y también un sistema de índices negativos:

```python
["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
```

---

### 📋 Slicing en listas

📍 Acceder al 2do, 3ro y 4to elemento:

```python
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[1:4])  # ['Tue', 'Wed', 'Thu']
```

📍 Primeros tres elementos:

```python
print(days[:3])  # ['Mon', 'Tue', 'Wed']
```

📍 Últimos tres elementos:

```python
print(days[-3:])  # ['Fri', 'Sat', 'Sun']
```

📍 Todos menos el último:

```python
print(days[:-1])  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
```

📍 Todos menos los últimos dos:

```python
print(days[:-2])  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
```

---

### 📞 Diccionarios: acceder a valores por clave

```python
phone_numbers = {
  "John": "+37682929928",
  "Marry": "+423998200919"
}

print(phone_numbers["Marry"])  # '+423998200919'
```

---
# 🧠 Cheatsheet: Functions and Conditionals

En esta sección aprendiste a:

---

### 🔧 Definir funciones

```python
def cube_volume(a):
    return a * a * a
```

---

### 🔁 Escribir condicionales if-else

```python
message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")
```

---

### 🔁 Condicionales if-elif-else

```python
message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")
```

---

### ✅ Operador `and` (ambas condiciones deben ser verdaderas)

```python
x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")
```

---

### ✅ Operador `or` (al menos una condición debe ser verdadera)

```python
x = 1
y = 2

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")
```

---

### 🔍 Verificar el tipo de dato con `isinstance`

```python
isinstance("abc", str)         # True
isinstance([1, 2, 3], list)    # True
```

O directamente con `type`:

```python
type("abc") == str             # True
type([1, 2, 3]) == list        # True
```

---
