"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7


Enunciat:

Implementa una funció anomenada find_max(lst) que trobi el valor màxim en una
llista de números utilitzant recursió. La funció ha de tornar el valor
màxim de la llista.

Paràmetres:
     lst (List): llista de nombres enters o flotants

Exemple:
     Entrada:
     numbers_list = [1, 5, 2, 7, 3]
     fid_max(numbers_list)

     Sortida:
     7

"""


def find_max(lst):
  assert find_max([1, 2, 3, 4, 5]) == 5, "find max does not return the correct value for input [1, 2, 3, 4, 5]. It should be 5"
  assert find_max([100, 2, 3, 4, 5]) == 100, "find max does not return the correct value for input [100, 2, 3, 4, 5,]. It should be 100"
  assert find_max([3, 1000, 5]) == 1000, "find max does not return the correct value for input [3, 1000, 5]. It should be 1000"
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# numbers_list = [1, 5, 2, 7, 3]
# print(find_max(numbers_list))
