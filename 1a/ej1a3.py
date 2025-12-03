'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

Enunciat:
Implementa una funció anomenada "invert_text(text_chain)" que rebi com
paràmetre una cadena de text de tipus string anomenada 'text_chain' i torni
el text invertit.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     invert_text('Hello world!')

     Sortida:
     !dlrow olleH

'''

def invert_text(text_chain:str):
    assert invert_text("Good day") == "yad dooG" "invert_text does not return the correct value for 'Good day'.It shoulb be 'yad dooG'"
    assert invert_text("python") == "nohtyp" "invert_text does not return the correct value for 'python'.It should be 'nohtyp'"
    assert invert_text("9 8 7 6 5 4 3 2 1") == "1 2 3 4 5 6 7 8 9" "invert_text does not return the correct value for '9 8 7 6 5 4 3 2 1'. It should be '1 2 3 4 5 6 7 8 9'"
    assert invert_text(" ") == " " "invert_text does not return the correct value for " ".It should be '""
    pass
"invert_text does not return the correct value for 'Good day'. It should be 'yad dooG'"
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(invert_text("Hello world!"))
