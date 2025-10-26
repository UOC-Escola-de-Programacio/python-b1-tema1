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
    
    for i in list_numbers:

        if type(i) != int:
 
            
            raise ValueError("Los valores deben ser de tipo entero")
        
    
        
    return max(list_numbers)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(obtain_max([2,40,4]))