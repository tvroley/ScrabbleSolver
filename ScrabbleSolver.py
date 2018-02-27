#!/usr/bin/env python3
#Scrabble Solver script with the Scrabble Solver class
from collections import defaultdict
from itertools import permutations

''' The ScrabbleSolver class contains methods to create a list of scrabble words from any set of letters and return the
scrabble words sorted from highest to lowest score '''
class ScrabbleSolver:
		
	def __init__(self):
		self.scrabblePoints = {'q':10, 'z':10, 'j':8, 'x':8, 'k':5, 'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 'b':3, 'c':3, 
			'm':3, 'p':3, 'd':2, 'g':2, 'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1} 
		self.dictionaryFileName = 'wordsEn.txt' #change to use a different scrabble dictionary file
		self.scrabbleDictionary = self.getScrabbleDictionary(self.dictionaryFileName)
	
	''' opens the scrabble enyclopedia file specified in the initialization method and moves the words into a defaultdict of 
	lists sorted by the starting letter of each word due to the length of the encyclopedia '''
	def getScrabbleDictionary(self, dictionaryFile):
		scrabbleDictionary = defaultdict(list)
		try:
			with open(dictionaryFile, 'r') as scrabbleFile:
				for line in scrabbleFile:
					scrabbleDictionary[line[0]].append(line[0:len(line) - 1])
				if not scrabbleDictionary:
					print('dictionary file is empty')
				scrabbleFile.close()
		except IOError:
			print("error reading scrabble dictionary file")
		return scrabbleDictionary
	
	#returns all permutations and permutations of every subset for a set of letters 
	def permute(self, letters):
		for i in range(1, len(letters) + 1):
			for permutation in permutations(letters, i):
				yield permutation

	#returns all scrabble words in a set of permutations by checking the defaultdict of lists of scrabble words 
	def findScrabbleWords(self, letters):
		scrabbleWords = []
		for perm in self.permute(letters):
			permutation = ''.join(perm)
			firstLetter = permutation[0]
			if permutation in self.scrabbleDictionary[firstLetter] and permutation not in scrabbleWords:
				scrabbleWords.append(permutation)
		return scrabbleWords
	
	#returns the points any scrabble word is worth
	def calculatePoints(self, word):
		if len(word) == 0:
			return 0
		points = 0
		for i in range(0, len(word)):
			points += self.scrabblePoints[word[i]]
		return points
		
	#sorts scrabble words by points value
	def sortByValue(self, scrabbleWords):
		index = 0
		runner = 0
		maxIndex = 0
		while(index < len(scrabbleWords)):
			maxIndex = index
			runner = index + 1
			while(runner < len(scrabbleWords)):
				if self.calculatePoints(scrabbleWords[runner]) > self.calculatePoints(scrabbleWords[maxIndex]):
					maxIndex = runner
				runner = runner + 1
			if maxIndex != index:
				temp = scrabbleWords[index]
				scrabbleWords[index] = scrabbleWords[maxIndex]
				scrabbleWords[maxIndex] = temp
			index = index + 1
			
	#checks for characters that aren't letters
	def validateLetters(self, letters):
		for i in range(0, len(letters)):
			numberValue = ord(letters[i])
			if numberValue < 65 or numberValue > 122:
				return False
			if numberValue > 90 and numberValue < 97:
				return False
		return True
	
	#calls all of the methods needed to return sorted scrabble words from a set of letters
	def createWords(self, letters):
		if self.validateLetters(letters):
			letters = letters.lower()
			scrabbleWords = self.findScrabbleWords(letters)
			self.sortByValue(scrabbleWords)
			return scrabbleWords
		else:
			print("letters contain a character that is not a letter")
			return []
