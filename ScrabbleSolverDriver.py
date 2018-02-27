#!/usr/bin/env python3
#Driver script to run the Scrabble Solver program
from sys import argv
from ScrabbleSolver import ScrabbleSolver

def main(argv):
	if len(argv) < 2:
		print("missing letters argument")
	else:
		s = ScrabbleSolver()
		print(s.createWords(argv[1]))
		
if __name__ == '__main__':
    main(argv)