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

def invert_text(text_chain):
    # es podria implementar amb reversed o 
    # slicing de cadena tipus [::-1]
    counter=len(text_chain)
    temp_text_chain=""

    # control errors
    if len(text_chain)==0:
        return temp_text_chain
    
    while counter > 0:
        temp_text_chain=temp_text_chain+text_chain[counter-1]
        counter -=1
    
    return temp_text_chain

print(invert_text('Hello world!'))
print(invert_text('1234567890'))
print(invert_text('Good day'))
# no es controlen tipus numèrics, per tant fallarà
# no s'implementa perquè no es demana a l'enunciat
#print(invert_text(34))
#print(invert_text(1.5))
#print(invert_text(None))

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(invert_text("Hello world!"))
