import unittest
from machinetranslation import translator


class TranslatorTest(unittest.TestCase):
    def test_french_to_english(self):
        french_to_english_assert_equal(self, None, None)
        french_to_english_assert_equal(self, 'Bonjour', 'Hello')
        french_to_english_assert_equal(self, 'Quoi', 'What')
        french_to_english_assert_equal(self, 'Merci', 'Thank you')
        french_to_english_assert_notequal(self, None, '')
        french_to_english_assert_notequal(self, 'Bonjour', 'Thank you')
        french_to_english_assert_notequal(self, 'Quoi', 'Hello')
        french_to_english_assert_notequal(self, 'Merci', 'What')

    def test_english_to_french(self):
        english_to_french_assert_equal(self, None, None)
        english_to_french_assert_equal(self, 'Hello', 'Bonjour')
        english_to_french_assert_equal(self, 'What', 'Quoi')
        english_to_french_assert_equal(self, 'Thanks', 'Merci')
        english_to_french_assert_notequal(self, None, '')
        english_to_french_assert_notequal(self, 'Hello', 'Merci')
        english_to_french_assert_notequal(self, 'What', 'Bonjour')
        english_to_french_assert_notequal(self, 'Thanks', 'Quoi')


def french_to_english_assert_equal(self, french_text, english_text):
    translation = translator.french_to_english(french_text)
    self.assertEqual(translation, english_text)


def french_to_english_assert_notequal(self, french_text, english_text):
    translation = translator.french_to_english(french_text)
    self.assertNotEqual(translation, english_text)


def english_to_french_assert_equal(self, english_text, french_text):
    translation = translator.english_to_french(english_text)
    self.assertEqual(translation, french_text)


def english_to_french_assert_notequal(self, english_text, french_text):
    translation = translator.english_to_french(english_text)
    self.assertNotEqual(translation, french_text)


if __name__ == '__main__':
    unittest.main()
