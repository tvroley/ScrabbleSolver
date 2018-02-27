#!/usr/bin/env python3
#unit tests for the scrabble solver class
from ScrabbleSolver import ScrabbleSolver
from collections import defaultdict
import unittest

solver = ScrabbleSolver()

class TestScrabbleSolver(unittest.TestCase):

	def test_getScrabbleDictionary(self):
		self.assertNotEqual(solver.getScrabbleDictionary("wordsEn.txt"), defaultdict(list))

	def test_getScrabbleDictionaryFileError(self):
		self.assertEqual(solver.getScrabbleDictionary("badFile"), defaultdict(list))
	
	def test_findScrabbleWords(self):
		self.assertEqual(solver.findScrabbleWords('ab'), ['a', 'ab'])
	
	def test_findScrabbleWordsNoWords(self):
		self.assertEqual(solver.findScrabbleWords('zzz'), [])
		
	def test_permute(self):
		perms = list(solver.permute("ab"))
		permutations = []
		for perm in perms:
			permutations.append("".join(perm))
		
		self.assertEqual(permutations, ['a', 'b', 'ab', 'ba'])
		
	def test_calculatePoints(self):
		self.assertEqual(solver.calculatePoints("code"), 7)
		
	def test_sortByValue(self):
		testWords = ['a', 'ah', 'at', 'ha', 'hat', 'th']
		solver.sortByValue(testWords)
		self.assertEqual(testWords, ['hat', 'ah', 'ha', 'th', 'at', 'a'])
	
	def test_validateLetters(self):
		self.assertTrue(solver.validateLetters('abcdefg'))
		
	def test_validateLettersInvalid(self):
		self.assertFalse(solver.validateLetters('abc#$defg'))
		
	def test_validateLettersUpper(self):
		self.assertTrue(solver.validateLetters('ABCDEFG'))
	
	def test_createWords(self):
		self.assertEqual(solver.createWords('hat'), ['hat', 'ha', 'ah', 'th', 'at', 'a'])
		
		
if __name__ == '__main__':
    unittest.main()