import unittest
import wordCount


class TestWordCount(unittest.TestCase):

    def test_wordcountiness(self):
        value = wordCount.wordCount("Hey there feller")
        self.assertEqual(value, '3')


if __name__ == "__main__":
    unittest.main()
