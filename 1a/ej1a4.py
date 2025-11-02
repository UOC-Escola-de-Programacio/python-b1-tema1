'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

Enunciat:
Crea una funció anomenada "count_vowels(text_chain)" que rebi com a paràmetre
una cadena de text de tipus string anomenada 'text_chain' i retorni el número
de vocals, ja siguin majúscules o minúscules, sense accent, que es trobin en 
aquesta cadena de text.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     count_vowels('Hello world, this is an example.')

     Sortida:
     9

'''

def count_vowels(text_chain):
    # array amb les vocals per ser comptades
    vowels=['a','e','i','o','u','A','E','I','O','U',]    
    vowels_counter=0

    for elem in text_chain:
        if elem in vowels:
            # augmentem el comptador de vocals
            vowels_counter +=1
    
    return vowels_counter

print(count_vowels('Hello world, this is an example.'))
print(count_vowels('.....'))
print(count_vowels('AEIOU'))
print(count_vowels('Hola'))
print(count_vowels('Python'))
print(count_vowels('AEIOU'))
print(count_vowels('AeioU'))
print(count_vowels(''))
print(count_vowels(' '))
print(count_vowels('3344a'))


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(count_vowels("Hello world, this is an example."))
