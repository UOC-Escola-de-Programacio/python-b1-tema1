from ej1a4 import count_vowels

def test_count_vowels():
    assert count_vowels("Hola") == 2, "count_vowels does not return the correct value for input 'Hola'. It should be 2"
    assert count_vowels("Python") == 1, "count_vowels does not return the correct value for input 'Python'. It should be 1"
    assert count_vowels("Aeiou") == 5, "count_vowels does not return the correct value for input 'Aeiou'. It should be 5"
    assert count_vowels("") == 0, "count_vowels does not return the correct value for input ''. It should be 0"


