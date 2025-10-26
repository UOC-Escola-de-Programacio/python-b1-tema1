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
    
    if len(lst) <=1:

        return lst                                      # En este punto, lst únicamente contiene el primer valor de la lista original, y se empieza a realizar los returns anteriores

    return [lst[-1]] + invert_list(lst[:-1])            # Al sumar la función, la función principal se queda a la espera de recibir el resultado. Así hasta que len(list) = 1. 


   
    



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
lst = [1, 20, 3, 40, 5]
print(invert_list(lst))
