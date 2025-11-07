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
    # Write here your code
    wordList = list(word)
    palindrome = True
    if len(wordList) > 0:
        if wordList[len(wordList)-1] != wordList[0]:
            palindrome = False
        wordList.pop(len(wordList)-1)
        if len(wordList) > 0:
            wordList.pop(0)
    return palindrome


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
word = "level"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
#
word = "juan"
print(f"Is '{word}' word palindrome?", is_palindrome(word))
