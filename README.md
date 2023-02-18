# CS_4395_Portfolio
Jimmy Harvin
Spring 2023

## Portfolio Setup
[Overview of NLP](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/CS%204395%20Overview%20of%20NLP.pdf)

## Text Processing
The following is a Python program made to do basic text processing on a csv file containing employee information. An example of a data file is given alongside the Python file. To run this program, provide a system argument (either in a command line or through an IDE) for the relative file path of the data you would like to process. Text processing, input, and output are very easy in Python relative to some of the other popular language, like Java and JavaScript. Built-in string functions like split and title make basic string manipulation trivial, and RE functions are as effective and simple as ever. Input and output is effortless, whether it be from the command line or to external files using something like pickle. This assignment provided a great refresher on Python syntax, with a healthy mix of control structures, object-oriented paradigms, and string manipulation. The use of regular expressions was particularly helpful, as these are essential to text and language processing in any programming language. <br/>

[Employee File](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/data.csv)<br/>
[Program](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/jah200003a1.py)

## Word Guessing
The following is a Python program that takes an input text from a specified system argument (either in a command line or through an IDE), finds the fifty most common nouns as tagged by NLTK, and allows the user to play a guessing game. For each round, the user enters a letter in the terminal; if the letter is in the word and has not been guessed previously, a point is scored. If the letter is not present or otherwise does not conform to input restrictions, a point is deducted. The user starts with five points, and the game ends when the score becomes negative. Alternatively, the user can end at any point by typing an exclamation point. <br/>

[Guessing Game](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/wordGuessing.py)<br/>
