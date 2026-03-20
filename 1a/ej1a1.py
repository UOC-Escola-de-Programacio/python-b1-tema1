'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

Enunciat:
Implementa la funció 'fibonacci(fibonacci_number)' que contingui l'algorisme
de Fibonacci i rebi com a paràmetre un valor numèric enter anomenat
'fibonacci_number' i torneu el valor de la sèrie Fibonacci en aquesta posició.
Així mateix, si el valor no és numèric, o és menor a zero, cal llançar
una excepció ValueError("missatge"), la qual pot incloure un missatge que hi hauria de
correspondre amb el tipus d'error durant la validació.

Paràmetres:
- fibonacci_number: Nombre enter positiu superior a 0 que representa la
posició a la sèrie Fibonacci.

Exemple:
     Entrada:
     fibonacci(10)

     Sortida:
     55

'''

def fibonacci(fibonacci_number):
    # Permitimos solo números enteros
    if type(fibonacci_number) is not int:
      raise ValueError("El valor debe ser un número entero.")
    
    # Solo valen números positivos
    if fibonacci_number < 0:
      raise ValueError("El número debe ser mayor o igual a cero.")
    
    # Casos base
    if fibonacci_number == 0:
      return 0
    if fibonacci_number == 1:
      return 1
    
    # Algoritmo
    a, b = 0, 1#variable a, es el numero anterior, b, el actual
    for i in range(2, fibonacci_number + 1):#el +1 es para que se pare en el número deseado
      a, b = b, a + b#a la izquierda, variables a actualizar.A la derecha, valores calculados
      
    return b

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(fibonacci(10))
