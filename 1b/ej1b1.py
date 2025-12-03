"""
Enunciado:
Implementar la función 'obtain_max(list_numbers)' que recibe 
como parámetro una lista no vacía de números enteros y devuelve
el número mayor de la lista.

Recuerda que en Python existe la función llamada 'max'

Parámetros:
- list_numbers: Lista de números enteros

Ejemplo:
    Entrada:
    obtain_max([1, 45, 87, 21, 0, 23, 28])

    Salida:
    87

Enunciat:
Implementar la funció 'obtain_max(list_numbers)' que rep 
com a paràmetre una llista no buida de nombres enters i retorna
el número major de la llista.

Recorda que en Python existeix la funció anomenada 'max'

Paràmetres:
- list_numbers: Llista de nombres enters

Exemple:
    Entrada:
    obtain_max([1, 45, 87, 21, 0, 23, 28])

    Sortida:
    87
"""

def obtain_max(list_numbers):
   
    assert obtain_max([1, 45, 87, 21, 0, 23, 28]) == 87, "obtain_max does not return the correct value for input [1, 45, 87, 21, 0, 23, 28]. It should be 87"
    assert obtain_max([1, 2]) == 2, "obtain_max does not return the correct value for input [1, 2]. It should be 2"
    assert obtain_max([0]) == 0, "obtain_max does not return the correct value for input [0]. It should be 0"
    assert obtain_max([32, 600, 129, 98, 123]) == 600, "obtain_max does not return the correct value for input [32, 600, 129, 98, 123]. It should be 600"
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(obtain_max([1, 45, 87, 21, 0, 23, 28]))
