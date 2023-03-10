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

[Guessing Game](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/wordGuessing.py)

## WordNet
The following is a Python notebook that explores different features of NLTK and WordNet, including synonym set hierarchies, sentimental analysis, and collocations. Descriptions and results for each task can be found within the notebook alongside Python code.

[Notebook](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/jah200003a3.ipynb)

## N-Grams
The following is a collection of Python programs made to create language models using n-grams. The first program takes in training data from three different languages and generates unigram and bigram dictionaries for each one. These pickled files can then be processed by the second program, which uses probabilities determined from the training data to identify the languages of test files.

[Dictionary Generator](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/get_ngrams.py)<br/>
[Language Identifier](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/LangPredModel.py)<br/>
[Narrative](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/N_Gram__Language_Models.pdf)

## Parsing
The following is a written assignment that parses a lengthy sentence with three different methods: PSG, dependencies, and semantic role labeling. PSG is the easiest to read and understand, including part-of-speech labels by each terminal symbol, but it is the most difficult to create. Dependency parsing was more thorough and caught relationships surrounding an anchor word, but the documentation was a fair bit more difficult to navigate. Semantic role labeling parses had even stranger documentation through the verb frames in PropBank, and while fewer relationships were captured, some meaning could be derived alongside syntax.

[Document](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/Parsing.pdf)

## Web Crawler
The following is a program that crawls and scrapes URLs to build a knowledge base pertaining to tea. This generates 50 files of text, and each of these is then cleaned and used to find important terms. There is a python file and an accompannying narrative file.

[Web Crawler](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/web_crawler_2.py)<br/>
[Narrative](https://github.com/JimmyHF/CS_4395_Portfolio/blob/main/Finding_and_Building_a_Corpus.pdf)
