"""
Enunciado:
Mediante la librería 'matplotlib', implementa una función llamada 
'line_graph(x,y)', se debe realizar únicamente la configuración 
para la gráfica (sin mostrar nada en pantalla).
De esta forma, deberás configurar el título, que será 'Graph';
los labels de los ejes, que serán 'Axis X' y 'Axis Y' y activar
el grid.

Puedes encontrar la documentación de la librería 'matplotlib' en el
siguiente enlace: https://matplotlib.org/stable/users/index

En concreto, te recomendamos que consultes:
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html


Los valores de los parámetros que recibe esta función son:
    
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

Enunciat:
Mitjançant la llibreria 'matplotlib', implementa una funció anomenada
'line_graph(x,y)', s'ha de realitzar únicament la configuració
per a la gràfica (sense mostrar res en pantalla).
D'aquesta forma, hauràs de configurar el títol, que serà 'Graph';
els labels dels eixos, que seran 'Axis X' i 'Axis I' i activar
el grid.

Pots trobar la documentació de la llibreria 'matplotlib' en el
següent enllaç: https://matplotlib.org/stable/users/index

En concret, et recomanem que consultis:
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html
* https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

Els valors dels paràmetres que rep aquesta funció són:
    
     x = [1, 2, 3, 4, 5]
     y = [2, 4, 6, 8, 10]

"""

import matplotlib.pyplot as plt

# Esta función deberá configurar la gráfica en la variable plt
# Aquesta funció haurà de configurar la gràfica en la variable plt
def line_graph(x, y):
    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    line_graph (x,y)
    ax = pet.gca()
    assert ax.get_xlabel() == 'Axis X', "No label in Axis X detected"
    assert ax.get_ylaber() == 'Axis Y', "No laber in Axis Y detected"
    assert ax.get_titlle() == 'Graph', "No tittle detected"
    assert len(pet.get.fingnums()) == 1, "number of figures is not 1"
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# line_graph([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
