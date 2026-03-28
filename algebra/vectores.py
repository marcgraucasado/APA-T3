"""
Autor: Marc Grau Casado

Clase Vector y operaciones asociadas.

Tests unitarios
===============

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> 2 * v1
Vector([2, 4, 6])
>>> v1 * v2
Vector([4, 10, 18])
>>> v1 @ v2
32

>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""

import doctest


class Vector:

    def __init__(self, iterable):
        """
        Construye un vector a partir de un iterable.

        Args:
            iterable: Iterable con las componentes del vector.
        """
        self.vector = [elemento for elemento in iterable]

    def __repr__(self):
        """
        Devuelve la representación formal del vector.

        Returns:
            str: Representación del vector.
        """
        return "Vector(" + repr(self.vector) + ")"

    def __ascii__(self):
        """
        Devuelve la representación ASCII del vector.

        Returns:
            str: Representación ASCII del vector.
        """
        return ascii(self.vector)

    def __len__(self):
        """
        Devuelve la dimensión del vector.

        Returns:
            int: Número de componentes del vector.
        """
        return len(self.vector)

    def __getitem__(self, indice):
        """
        Devuelve la componente indicada.

        Args:
            indice (int): Índice de la componente.

        Returns:
            Valor de la componente.
        """
        return self.vector[indice]

    def __add__(self, otro):
        """
        Suma dos vectores componente a componente.

        Args:
            otro (Vector): Vector a sumar.

        Returns:
            Vector: Suma de ambos vectores.
        """
        return Vector([a + b for a, b in zip(self.vector, otro.vector)])

    def __sub__(self, otro):
        """
        Resta dos vectores componente a componente.

        Args:
            otro (Vector): Vector a restar.

        Returns:
            Vector: Diferencia entre ambos vectores.
        """
        return Vector([a - b for a, b in zip(self.vector, otro.vector)])

    def __mul__(self, otro):
        """
        Multiplica un vector por un escalar o realiza el producto de Hadamard.

        Args:
            otro: Escalar o vector.

        Returns:
            Vector: Resultado de la multiplicación.
        """
        if isinstance(otro, (int, float)):
            return Vector([elemento * otro for elemento in self.vector])

        if isinstance(otro, Vector):
            return Vector([a * b for a, b in zip(self.vector, otro.vector)])

        return NotImplemented

    def __rmul__(self, otro):
        """
        Multiplica un escalar por un vector.

        Args:
            otro: Escalar.

        Returns:
            Vector: Resultado de la multiplicación.
        """
        return self.__mul__(otro)

    def __matmul__(self, otro):
        """
        Calcula el producto escalar de dos vectores.

        Args:
            otro (Vector): Segundo vector.

        Returns:
            int | float: Producto escalar.
        """
        return sum(a * b for a, b in zip(self.vector, otro.vector))

    def __floordiv__(self, otro):
        """
        Devuelve la componente paralela de un vector respecto a otro.

        Args:
            otro (Vector): Vector de referencia.

        Returns:
            Vector: Componente paralela.
        """
        coeficiente = (self @ otro) / (otro @ otro)
        return coeficiente * otro

    def __mod__(self, otro):
        """
        Devuelve la componente perpendicular de un vector respecto a otro.

        Args:
            otro (Vector): Vector de referencia.

        Returns:
            Vector: Componente perpendicular.
        """
        return self - (self // otro)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
