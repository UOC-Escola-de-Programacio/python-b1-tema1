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
    assert is_palindrome("racecar") == True, "is palindrome does not return the correct value for input racecar. It should be True"
    assert is_palindrome("level") == True, "is palindrome does not return the correct value for input level. It should be True"
    assert is_palindrome("deifies") == True, "is palindrome does not return the correct value for input deifies. It should be True"
    assert is_palindrome("civic") == True, "is palindrome does not return the correct value for input civic. It should be True"
    assert is_palindrome("python") == False, "is palindrome does not return the correct value for input python. It should be False"
    assert is_palindrome("palindrome") == False, "is palindrome does not return the correct value for input palindrome. It should be False"
    assert is_palindrome(" ") == True, "is palindrome does not return the correct value for input ' '. It should be True"
    assert is_palindrome("a") == True, "is palindrome does not return the correct value for input 'a'. It should be True"
    assert is_palindrome("ab") == False, "is palindrome does not return the correct value for input 'ab'. It should be False"
    assert is_palindrome("radar") == True, "is palindrome does not return the correct value for input 'radar'. It should be True" 
    
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# word = "level"
# print(f"Is '{word}' word palindrome?", is_palindrome(word))
#
# word = "juan"
# print(f"Is '{word}' word palindrome?", is_palindrome(word))
