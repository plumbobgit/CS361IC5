import unittest
import palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindromeness(self):
        value = palindrome.is_palindrome('racecar')
        self.assertEqual(value, True)

    def test_notpalindromeness(self):
        value = palindrome.is_palindrome('hello')
        self.assertEqual(value, False)


if __name__ == "__main__":
    unittest.main()
