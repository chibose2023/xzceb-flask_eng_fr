import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'hello')        
    
    def test2(self):
        self.assertRaises(ValueError, english_to_french, None)        
        self.assertRaises(ValueError, french_to_english, None) 

unittest.main()
