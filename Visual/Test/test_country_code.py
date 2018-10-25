from country_code import get_country_code
import unittest

class CodeTextCase(unittest.TestCase):
    
    def test_get_country_code(self):
        code = get_country_code('Andorra')
        self.assertEqual(code,'ad')

unittest.main()
