"""
Enunciado:
Utilizando la librería 'math', implementa una función llamada 
'calculate_angle(angle)'  que reciba como parámetro un número 
correspondiente a un ángulo en grados llamado 'angle' y retorne
como resultado el seno de dicho ángulo redondeado a 2 decimales.

Encontrarás la documentación de la librería 'math' en el 
siguiente enlace: https://docs.python.org/3/library/math.html

En concreto, la función 'sin(x)' de la librería 'math' la 
puedes encontrar en el siguiente enlace:
https://docs.python.org/3/library/math.html#math.sin

Y la función 'radians(x)' de la librería 'math' la puedes
encontrar en el siguiente enlace:
https://docs.python.org/3/library/math.html#math.radians
(te servirá para convertir los grados a radianes)

Recuerda que puedes redondear decimales con la función 
'round(x, n)'


Parámetros:
- angle: Entero correspondiente al valor de un ángulo.

Ejemplo:
    Entrada:
    calculate_angle(270)

    Salida:
    -1

Enunciat:
Utilitzant la llibreria 'math', implementa una funció anomenada
'calculate_angle(angle)' que rebi com a paràmetre un número
corresponent a un angle en graus anomenat 'angle' i retorni
com a resultat el sinus de l'angle arrodonit a 2 decimals.

Trobaràs la documentació de la llibreria 'math' en el 
següent enllaç: https://docs.python.org/3/library/math.html

En concret, la funció 'sense(x)' de la llibreria 'math' la 
pots trobar en el següent enllaç:
https://docs.python.org/3/library/math.html#math.sense

I la funció 'radians(x)' de la llibreria 'math' la pots
trobar en el següent enllaç:
https://docs.python.org/3/library/math.html#math.radians
(et servirà per a convertir els graus a radiants)

Recorda que pots arrodonir decimals amb la funció 
'round(x, n)'

Paràmetres:
- àngel: Sencer corresponent al valor d'un angle.

Exemple:
     Entrada:
     calculate_angle(270)

     Sortida:
     -1
"""

import math

def calculate_angle(angle):
    assert calculate_angle (0) == 0,"The calculate_angle for 0, does not return the correct value.It should be 0"
    assert calculate_angle (90) == 1, "The calculate angle for 90, does not return the correct value. It should be 1"
    assert math.isclose (calculate_angle(180), 0,rel_tol=0.01) "The calculate angle for 180, does not return the correct value. It should be 0"
    assert math.isclose (calculate_angle(270), -1,rel_tol=0.01) "The calculate angle for 270, does not return the correct value. It should be -1"
    assert math.isclose (calculate_angle (45), 0.71,rel_tol=0.01) "The calculate angle for 45, does not retrun the correct value. It should be 0.71"
    pass
   

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(calculate_angle(270))
