# Intermediate Python #2: Inheritance

La herencia es un concepto clave en la programación orientada a objetos (OOP) que permite a una clase heredar atributos y métodos de otra clase. En Python, la herencia se implementa de la siguiente manera:

1. **Clase Padre o Superclase:**
   - La clase que es heredada se conoce como la clase padre o superclase.
   - Contiene atributos y métodos que son compartidos por una o más clases derivadas.

2. **Clase Derivada o Subclase:**
   - La clase que hereda de otra clase se llama clase derivada o subclase.
   - Puede tener sus propios atributos y métodos adicionales, además de heredar los de la clase padre.

3. **Sintaxis de Herencia en Python:**
   - Para heredar de una clase, se especifica la clase padre entre paréntesis después del nombre de la clase derivada.

   ```python
   class ClasePadre:
       # Atributos y métodos de la clase padre

   class ClaseDerivada(ClasePadre):
       # Atributos y métodos adicionales de la clase derivada
   ```

   - La clase derivada puede acceder a los atributos y métodos de la clase padre y también puede agregar, modificar o anular (sobrescribir) sus propios atributos y métodos.

Ejemplo de herencia en Python:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Crear objetos de las clases derivadas
mi_perro = Perro(nombre="Buddy")
mi_gato = Gato(nombre="Whiskers")

# Acceder a los atributos y métodos de la clase padre
print(f"{mi_perro.nombre} dice: {mi_perro.hacer_sonido()}")
print(f"{mi_gato.nombre} dice: {mi_gato.hacer_sonido()}")
```

En este ejemplo, `Animal` es la clase padre que tiene un método `hacer_sonido()`. Las clases `Perro` y `Gato` son clases derivadas que heredan de la clase `Animal`. Cada clase derivada implementa su propia versión del método `hacer_sonido()`.

La herencia permite la reutilización de código y facilita la organización y la estructura del código en proyectos más grandes. Además, promueve la coherencia y la consistencia al compartir funcionalidades comunes entre clases relacionadas.