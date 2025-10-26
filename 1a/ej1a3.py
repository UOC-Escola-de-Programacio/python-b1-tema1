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


def invert_text_long(text_chain:str):    # VERSION LARGA 
    
    if type(text_chain) != str:

        raise ValueError("El valor introducido debe ser de tipo 'string'")

    lista =[]                      # Creamos lista con los elementos de text_chain para luego iterarla a la inversa
    for i in text_chain:
        lista.append(i)
    
    inv_palabra = ""
    for index, i in enumerate(lista,1):

        inv_palabra += lista[-index]
        
        
       
    return inv_palabra
   

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(invert_text_long("Hello World!"))




def invert_text_short(text_chain:str):        #VERSION CORTA

    if type(text_chain) != str:

        raise ValueError("El valor introducido debe ser de tipo 'string'")
    

    return text_chain[::-1]

print(invert_text_short("Hello World!"))





