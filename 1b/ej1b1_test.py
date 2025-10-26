from ej1b1 import obtain_max
import pytest



def test_obtain_max():
    assert obtain_max([1, 45, 87, 21, 0, 23, 28]) == 87, "obtain_max does not return the correct value for input [1, 45, 87, 21, 0, 23, 28]. It should be 87"
    assert obtain_max([1, 2]) == 2, "obtain_max does not return the correct value for input [1, 2]. It should be 2"
    assert obtain_max([0]) == 0, "obtain_max does not return the correct value for input [0]. It should be 0"
    assert obtain_max([32, 600, 129, 98, 123]) == 600, "obtain_max does not return the correct value for input [32, 600, 129, 98, 123]. It should be 600"
   
   
def test_invalid_input():
     with pytest.raises(ValueError): 
         obtain_max([-1.5,4,20]), "obtain_max no devuelve el valor esperado para [-1.5,4,20], debería ser ValueError por valor float"