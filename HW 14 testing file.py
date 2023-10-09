import unittest
from functions import greeting_by_name, get_symbol_position, merge
from functions_with_errors import greeting_by_name as greeting_by_name_with_errors, \
    get_symbol_position as get_symbol_position_with_errors, merge as merge_with_errors

class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        name = "Alice"
        expected = f"Hello {name}!"
        self.assertEqual(greeting_by_name(name), expected)

        # Test the function with errors
        self.assertEqual(greeting_by_name_with_errors(name), expected)

    def test_get_symbol_position(self):
        text = "Hello, World!"
        symbol = "o"
        expected = 5
        self.assertEqual(get_symbol_position(text, symbol), expected)

        # Test the function with errors
        self.assertEqual(get_symbol_position_with_errors(text, symbol), expected)

        # Test when the symbol is not found
        symbol = "x"
        expected = "Not found"
        self.assertEqual(get_symbol_position(text, symbol), expected)

        # Test when symbol is incorrect
        symbol = "oo"
        expected = "Error! Symbol can be a string with only one letter"
        self.assertEqual(get_symbol_position(text, symbol), expected)
        self.assertEqual(get_symbol_position_with_errors(text, symbol), expected)

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'b': 3, 'c': 4}
        expected = {'a': 1, 'b': 3, 'c': 4}

        # Test the function without errors
        self.assertEqual(merge(dict1, dict2), expected)

        # Test dict immutability
        merged_dict = merge(dict1, dict2)
        self.assertNotEqual(id(dict1), id(merged_dict))
        self.assertNotEqual(id(dict2), id(merged_dict))

        # Test the function with errors
        self.assertEqual(merge_with_errors(dict1, dict2), expected)

if __name__ == '__main__':
    unittest.main()