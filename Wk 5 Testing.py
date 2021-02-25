## Sample script rearrange.py
import re

def rearrange_name(name):
    result = re.search(r'([\w.]*), ([\w.]*)$', name)
    if result is None:
        return name
    return '{} {}'.format(result[2], result[1])

# Unit test for sample script rearrange_test.py

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    #Parentheses: we pass in the class that we want to inherit from
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)
        # This test prompted the addition of 'If result is None' tp rearrange_naem 

    def test_double_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = 'Socrates'
        expected = 'Socrates'
        self.assertEqual(rearrange_name(testcase), expected)


# Make sure to chmod +x rearrange_test.py to make it executable 
# Call tests):
unittest.main()

### TRY-EXCEPT CONSTRUCT ###

def character_frequemcy(filename):
    '''Counts the frequency of each character in the given string'''
    # First try to open the file
    try:
        f = open(filename)
    except OSError:
        return None

    # Now process the file
    characters = {}
    for line in f:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    f.close()
    return characters 

# VALIDATE USERNAME: RAISING ERRORS 

def validate_user(username, minlen):
    assert type(username) == str, 'username must be a string'
    if minlen < 1:
        raise ValueError('minlen must be a number > 0')
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True 

# TEST CASES FOR VALIDATE_USER

import unittest

from validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user('validuser', 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user('inv', 5), False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user('invalid_user', 1), False)

    def test_invalid_minlen(self):
        # To test for errors, pass the expected error type,
        # then the function, then paramteters
        self.assertRaises(ValueError, validate_user, 'user', -1)
# Run the tests
unittest.main()
