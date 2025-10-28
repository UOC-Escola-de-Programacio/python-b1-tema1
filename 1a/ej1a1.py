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
    '''
        if fibonacci_number == 0:
            return 1

        return fibonacci_number * fibonacci(fibonacci_number - 1)
    '''

    if isinstance(fibonacci_number, str):
        raise ValueError("El número de fibonacci ha d'ésser numèric: " + str(fibonacci_number))
    if isinstance(fibonacci_number, float):
        raise ValueError("El número de fibonacci ha d'ésser numèric, però int: " + str(fibonacci_number))
    if fibonacci_number is None:
        raise ValueError(f"El número de fibonacci no pot ser None")
    if fibonacci_number < 0:
        raise ValueError(f"El número de fibonacci no pot ser menor de 0: " + str(fibonacci_number))


    # comptador inicial per generar la sèrie fins arribar al límit
    # marcat pel paràmetre fibonacci_number
    counter=0

    # primers 2 elements generadors de la sèrie
    templist=[0,1]

    # generen la sèrie, afegint una llista la suma del n-essim element
    # amb n+1 element
    while counter <= fibonacci_number:
        templist.append(templist[counter] + templist[counter+1])
        counter +=1

    # per comprobació de l'usuari, imprim la llista
    #print(f"La llista fibonacci generada és: {templist} ")
    
    # retornem l'element a la posició marcada per fibonacci_number.
    return templist[fibonacci_number]
    
try:
    fibonacci(10)
    #print(fibonacci(1.5))
    #print(fibonacci(1))
    #print(fibonacci(2))
    #print(fibonacci(10))
    #print(fibonacci("10"))
    #print(fibonacci(-1))
    #print(fibonacci(""))
    #print(fibonacci(None))
except ValueError as err:
    print(err)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(fibonacci(10))
