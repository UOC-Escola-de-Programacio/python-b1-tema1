""" 
Enunciado:
Escribe una función llamada is_palindrome(word) que reciba como parámetro
una cadena word y verifique si es un palíndromo utilizando recursión.
La función debe devolver True si la cadena es un palíndromo y False en
caso contrario.

Parámetros:
    word (str): una cadena de caracteres.

Ejemplo:
    Entrada:
    word = "racecar"
    print(is_palindrome(word))

    Salida:
    True



Enunciat:

Enunciat:
Escriu una funció anomenada is_palindrome(word) que rebi com a paràmetre
una cadena word i verifiqui si és un palíndrom utilitzant recursió.
La funció ha de tornar True si la cadena és un palíndrom i False a
cas contrari.

Paràmetres:
     word (str): una cadena de caràcters.

Exemple:
     Entrada:
     word = "racecar"
     print(is_palindrome(word))

     Sortida:
     True

"""


def is_palindrome(word):

    
    if len(word) == 1 or len(word) == 0:              # Si llegamos a tener una palabra de 1 letra (en palabras impares) o 0 (palabras pares) es que es palíndromo, True
        
        return True

    elif word[0] == word[-1]:                         # Si la primera y última letra son iguales, llamamos a función con la palabra sin esas letras
    
        return is_palindrome(word[1:-1])

    elif word[0] != word[-1]:                         # Aquí ya no sería palíndomo porque no son iguales la primera y última letra que estamos analizando, por lo tanto False

        return False
    
    
    
    


    
    



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
word = "level"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
#
word = "juan"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
