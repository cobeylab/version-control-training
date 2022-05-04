import unittest
from evolve import *

class TestEvolveMethods(unittest.TestCase):

    def test_fitness(self):
        self.assertEqual(fitness("abcd", "axxd"), 2)
        self.assertEqual(fitness("abcd", "abcd"), 4)
        self.assertEqual(fitness("abcd", "wxyz"), 0)

    def test_mutaterate(self):
        self.assertEqual(mutaterate("abcd", "wxyz"), 1)
        self.assertEqual(mutaterate("abcd", "abce"), 0.25)
        self.assertEqual(mutaterate("abcd", "abcd"), 0)

    def test_mutate(self):
        """mutate with no mutation rate returns the parent."""
        alphabet = "abcdefgh"
        self.assertEqual(mutate("abcd", 0, alphabet), ['a', 'b', 'c', 'd'])

        """mutate returns only characters from the alphabet."""
        self.assertTrue(all([l in alphabet for l in mutate("abcd", 0.25, "abcdefgh")]))

    def test_mate(self):
        self.assertEqual(mate("abcd", "efgh"), ('abcd', 'efgh', 'abgh', 'efcd'))

    def test_evolve(self):
        """evolve raises error if target is not composed of the alphabet."""
        with self.assertRaises(AssertionError):
            evolve("abcd", "abcx", "abcd")

        """evolve raises error if seed and target are different lengths."""
        with self.assertRaises(AssertionError):
            evolve("abc", "abcd", "abcd")

