Scrabble Solver

Description:
This program takes as input a set of letters representing tiles on a Scrabble board, and returns all of the possible acceptable 
Scrabble words sorted from highest point value to lowest point value as a list.

Python version notes:
This program was written and tested in Python version 3.6.4
To check your version of python, use the command "python --version"

Running on Linux:
The following line is included at the top of each script to allow the scripts to run on Linux: "#!/usr/bin/env python3"
You may also need to use the "chmod a+x" command on each script to execute the scripts on Linux.
Example: "chmod a+x ScrabbleSolverDriver.py"
Most versions of ubuntu come with Python 2 already installed.
IMPORTANT: To ensure this program runs properly on linux, use the "python3" command instead of the "python" command.
Example: "python3 ScrabbleSolverDriver.py tah"
To make sure the python3 path is configured in your Linux environment, use the command "whereis python3".
The Linux command line should print out a directory, such as "usr/bin/python3".

General Instructions:
To run this python program, cd into its directory and use the python command to run ScrabbleSolverDriver.py with the letters 
you would like to find Scrabble words for as the argument after the file name.
Example: "python ScrabbleSolverDriver.py tah"

Testing:
To run the unit tests for ScrabbleSolver.py, use the python command on the TestScrabbleSolver.py file.
This would look like: "python TestScrabbleSolver.py"

Scrabble Encyclopedia Notes:
The encyclopedia of scrabble words used by this program are from http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt 
and are included in the the project's directory as a text file called “wordsEn.txt”.
