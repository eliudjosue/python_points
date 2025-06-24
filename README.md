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
# 🧠 Cheatsheet: Processing User Input

En esta sección aprendiste que:

---

### 📥 Obtener datos del usuario con `input()`

```python
name = input("Enter your name: ")
```

La función `input()` **detiene la ejecución** y espera que el usuario ingrese texto.  
⚠️ El resultado **siempre es un string**.

---

### 🔄 Convertir input a otros tipos

Podés convertir el valor recibido con `int()` o `float()` si necesitás operar con números:

```python
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
```

---

### 🧵 Formatear cadenas con `.format()`

```python
name = "Sim"
experience_years = 1.5

print("Hi {}, you have {} years of experience".format(name, experience_years))
```

💬 **Salida:**
```
Hi Sim, you have 1.5 years of experience.
```

---
# 🔁 Cheatsheet: Loops

En esta sección aprendiste lo siguiente:

---

### 🔄 For-loop

Un `for` se usa para ejecutar repetidamente un bloque de código:

```python
for letter in 'abc':
    print(letter.upper())
```

💬 **Salida:**
```
A
B
C
```

📌 El nombre después de `for` (como `letter`) es solo una variable que representa cada ítem del iterable.

---

### 🔑 Recorrer claves de un diccionario

```python
phone_numbers = {
    "John Smith": "+37682929928",
    "Marry Simpons": "+423998200919"
}

for key in phone_numbers.keys():
    print(key)
```

💬 **Salida:**
```
John Smith
Marry Simpons
```

---

### 🔢 Recorrer valores de un diccionario

```python
for value in phone_numbers.values():
    print(value)
```

💬 **Salida:**
```
+37682929928
+423998200919
```

---

### 🗂️ Recorrer ítems (clave y valor)

```python
for key, value in phone_numbers.items():
    print(key, value)
```

💬 **Salida:**
```
John Smith +37682929928
Marry Simpons +423998200919
```

---

### ♾️ While-loop

El código dentro de un `while` se ejecuta **mientras la condición sea verdadera**:

```python
import datetime

while datetime.datetime.now() < datetime.datetime(2090, 8, 20, 19, 30, 20):
    print("It's not yet 19:30:20 of 2090.8.20")
```

💡 Este bucle imprimirá el mensaje una y otra vez hasta que llegue esa fecha y hora.

---
# 🧠 Cheatsheet: List Comprehensions

En esta sección aprendiste que:

Una **list comprehension** es una expresión que crea una lista **iterando sobre otra estructura de datos**.

---

### 🔁 List comprehension básica

```python
[i*2 for i in [1, 5, 10]]
```

💬 **Salida:**
```
[2, 10, 20]
```

---

### ✅ Con condición `if`

```python
[i*2 for i in [1, -2, 10] if i > 0]
```

💬 **Salida:**
```
[2, 20]
```

---

### ✅ Con `if` y `else`

```python
[i*2 if i > 0 else 0 for i in [1, -2, 10]]
```

💬 **Salida:**
```
[2, 0, 20]
```

---

💡 Las list comprehensions son una forma **más concisa y legible** de crear listas a partir de otras listas o iterables, aplicando transformaciones y/o filtros.

---
# 🧠 Cheatsheet: More on Functions

En esta sección aprendiste que:

---

### 📦 Funciones con múltiples parámetros

```python
def volume(a, b, c):
    return a * b * c
```

---

### ⚙️ Parámetros con valores por defecto

```python
def converter(feet, coefficient=3.2808):
    meters = feet / coefficient
    return meters

print(converter(10))
```

💬 **Salida:**
```
3.0480370641306997
```

---

### 🧩 Argumentos posicionales y por clave

```python
def volume(a, b, c):
    return a * b * c

print(volume(1, b=2, c=10))
```

---

### ✳️ `*args`: argumentos no nombrados (posicionales arbitrarios)

```python
def find_max(*args):
    return max(args)

print(find_max(3, 99, 1001, 2, 8))
```

💬 **Salida:**
```
1001
```

---

### ✳️ `**kwargs`: argumentos nombrados arbitrarios

```python
def find_winner(**kwargs):
    return max(kwargs, key=kwargs.get)

print(find_winner(Andy=17, Marry=19, Sim=45, Kae=34))
```

💬 **Salida:**
```
Sim
```

---

### 🧾 Resumen de elementos de funciones

| Elemento     | Uso                                                  |
|--------------|------------------------------------------------------|
| Parámetros   | `def func(a, b):`                                    |
| Valores por defecto | `def func(a=5):`                           |
| `*args`      | Recibe argumentos posicionales variables             |
| `**kwargs`   | Recibe argumentos con nombre variables               |
| `return`     | Devuelve un valor desde la función                   |

---
# 📁 Sección 11: File Processing

En esta sección aprendiste que:

---

### 📖 Leer un archivo existente

```python
with open("file.txt") as file:
    content = file.read()
```

---

### ✍️ Crear un archivo nuevo y escribir texto

```python
with open("file.txt", "w") as file:
    content = file.write("Sample text")
```

ℹ️ Modo `"w"` sobrescribe el archivo si ya existe.

---

### ➕ Agregar texto a un archivo existente (sin sobrescribir)

```python
with open("file.txt", "a") as file:
    content = file.write("More sample text")
```

ℹ️ Modo `"a"` agrega al final del archivo.

---

### 🔁 Leer y agregar texto en el mismo archivo

```python
with open("file.txt", "a+") as file:
    file.write("Even more sample text")
    file.seek(0)
    content = file.read()
```

ℹ️ Modo `"a+"` permite tanto agregar como leer.  
`file.seek(0)` mueve el cursor al inicio del archivo para poder leer.

---

✅ Usar `with open(...)` es la forma recomendada ya que se encarga automáticamente de cerrar el archivo al finalizar.

---
# 📦 Sección 12: Imported Modules

En esta sección aprendiste que:

---

### 🧠 Builtin Objects

Los **builtin objects** son objetos integrados en el intérprete de Python (escritos en C).

Los **builtin modules** contienen estos objetos integrados.

---

### ⚠️ Algunos objetos no están disponibles directamente

Para usarlos, primero hay que importar el módulo:

```python
import time
time.sleep(5)
```

---

### 📋 Listar todos los módulos integrados

```python
import sys
print(sys.builtin_module_names)
```

---

### 📚 Librerías estándar (Standard Libraries)

El término **standard libraries** incluye:
- Módulos integrados en C (builtin)
- Módulos escritos en Python (`.py`), que están dentro del directorio de instalación de Python

📍 Podés ver el path con:

```python
print(sys.prefix)
```

---

### 📦 Paquetes

Un **paquete** es una colección de módulos `.py` organizados dentro de una carpeta.

---

### 🌐 Librerías de terceros

Son paquetes/módulos creados por la comunidad (no parte del core de Python).

---

### 📥 Instalación de librerías de terceros

🪟 **Windows**:

```bash
pip install pandas
# o si falla:
python -m pip install pandas
```

🍎🐧 **Mac y Linux**:

```bash
pip3 install pandas
# o si falla:
python3 -m pip install pandas
```

---

💡 Tip: Usá un entorno virtual (`venv`) para gestionar tus dependencias de manera aislada.

---
