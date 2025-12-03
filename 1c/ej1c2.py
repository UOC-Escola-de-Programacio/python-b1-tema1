"""
Enunciado:
Escribe una función llamada 'invert_list(lst)' que reciba como parámetro
una lista 'lst' y la invierta utilizando recursión. La función debe
devolver la lista invertida.

Parámetros:
    lst (list): una lista de elementos.

Ejemplo
    Entrada:
    lst = [1, 2, 3, 4, 5]
    print(invert_list(lst))

    Salida:
    [5, 4, 3, 2, 1]

Enunciat:

Escriu una funció anomenada 'invert_list(lst)' que rebi com a paràmetre
una llista 'lst' i la inverteixi utilitzant recursió. La funció ha
tornar la llista invertida.

Paràmetres:
     lst (list): una llista d'elements.

Exemple
     Entrada:
     lst = [1, 2, 3, 4, 5]
     print(invert_list(lst))

     Sortida:
     [5, 4, 3, 2, 1]

"""


def invert_list(lst):
# Prueba básica con una lista de números enteros
    assert invert_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], "invert_list does not return the correct value for input [1, 2, 3, 4, 5]. It should be [5, 4, 3, 2, 1]"
# Prueba con una lista de cadenas
    assert invert_list(["a", "b", "c", "d", "e"]) == ["e", "d", "c", "b", "a"], "invert_list does not return the correct value for input ['a', 'b', 'c', 'd', 'e']. It should be ['e', 'd', 'c', 'b', 'a']"
# Prueba con una lista vacía
    assert invert_list([]) == [], "invert_list does not return the correct value for input []. It should be []"
# Prueba con una lista que contiene un solo elemento
    assert invert_list([10]) == [10], "invert_list does not return the correct value for input [10]. It should be [10]"
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# lst = [1, 20, 3, 40, 5]
#print(invert_list(lst))
