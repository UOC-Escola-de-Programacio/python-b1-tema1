from ej1a1 import fibonacci
import pytest


def test_fibonacci_():
    assert fibonacci(0) == 0, "fibonacci does not return the correct value for input 0. It should be 0"
    assert fibonacci(1) == 1, "fibonacci does not return the correct value for input 1. It should be 1"
    assert fibonacci(6) == 8, "fibonacci does not return the correct value for input 6. It should be 8"
    assert fibonacci(10) == 55, "fibonacci does not return the correct value for input 10. It should be 55"

def test_fibonacci_invalid_input():
    with pytest.raises(ValueError):
        fibonacci(-1), "no detecta error en valor negativo."
    with pytest.raises(ValueError):
        fibonacci(1.5), "fibonacci does not return the correct value for input 1.5. It should raise an error"
    with pytest.raises(ValueError):
        fibonacci("5"), "fibonacci does not return the correct value for input '5'. It should raise an error"