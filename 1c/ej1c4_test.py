from ej1c4 import is_palindrome


def test_is_palindrome():
    assert is_palindrome("racecar") == True, "is_palindrome does not return the correct value for input racecar. It should be True"
    assert is_palindrome("level") == True, "is_palindrome does not return the correct value for input level. It should be True"
    assert is_palindrome("deified") == True, "is_palindrome does not return the correct value for input deified. It should be True"
    assert is_palindrome("civic") == True, "is_palindrome does not return the correct value for input civic. It should be True"
    assert is_palindrome("python") == False, "is_palindrome does not return the correct value for input python. It should be False"
    assert is_palindrome("palindrome") == False, "is_palindrome does not return the correct value for input palindrome. It should be False"
    assert is_palindrome("") == True, "is_palindrome does not return the correct value for input ''. It should be True"
    assert is_palindrome("a") == True, "is_palindrome does not return the correct value for input a. It should be True"
    assert is_palindrome("ab") == False, "is_palindrome does not return the correct value for input ab. It should be False"
    assert is_palindrome("radar") == True, "is_palindrome does not return the correct value for input radar. It should be True"
    assert is_palindrome("anna") == True, "is_palindrome does not return the correct value for input radar. It should be True"
    assert is_palindrome("rana") == False, "is_palindrome does not return the correct value for input radar. It should be False"