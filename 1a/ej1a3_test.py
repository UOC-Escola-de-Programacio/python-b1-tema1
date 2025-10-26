from ej1a3 import invert_text_long,invert_text_short

def test_invert_text_long():
    assert invert_text_long("Good day") == "yad dooG", "invert_text does not return the correct value for 'Good day'. It should be 'yad dooG'"
    assert invert_text_long("python") == "nohtyp", "invert_text does not return the correct value for 'python'. It should be 'nohtyp'"
    assert invert_text_long("987654321") == "123456789", "invert_text does not return the correct value for '987654321'. It should be '123456789'"
    assert invert_text_long("") == "", "invert_text does not return the correct value for ''. It should be ''"


def test_invert_text_short():

    assert invert_text_short("Good day") == "yad dooG", "invert_text does not return the correct value for 'Good day'. It should be 'yad dooG'"
    assert invert_text_short("python") == "nohtyp", "invert_text does not return the correct value for 'python'. It should be 'nohtyp'"
    assert invert_text_short("987654321") == "123456789", "invert_text does not return the correct value for '987654321'. It should be '123456789'"
    assert invert_text_short("") == "", "invert_text does not return the correct value for ''. It should be ''"

