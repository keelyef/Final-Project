import pytest
import createpw

characters = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "1234567890"
    "!@#$%^&*()?_")

''' tests 100 permutations of password length'''
def test_create_password_length():
    ''' run validation of 1...100 length passwords '''
    for x in range(1,100):
        password = createpw.create_password(x)
        assert len(password) == x

'''tests all characters in generated password
are within the possible character list'''
def test_create_password_characters():
    allCharacters = list(characters)
    password = createpw.create_password(len(allCharacters))
    print(password)
    for x in password:
        assert x in allCharacters