import sys
import os
import random
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import numpy


def read_data(file_path):
    # Reads file from specified file path, returns file text
    with open(os.path.join(os.getcwd(), file_path), "r") as f:
        text = f.read()
    return text


def get_tokens(file_text):
    # Input is raw text, returns a list of tokens and a set of tokens
    token_list = word_tokenize(file_text)
    token_list = [t.lower() for t in token_list if t.isalpha()]
    unique_set = set(())
    for token in token_list:
        unique_set.add(token)
    return token_list, unique_set


def get_unique_lemmas(token_list):
    # Input is a list of tokens, returns a set of lemmas
    stopword_set = set(stopwords.words('english'))
    token_list = [t for t in token_list if (len(t) > 5 and t not in stopword_set)]

    wnl = WordNetLemmatizer()
    lemmatized_tokens = set([wnl.lemmatize(t) for t in token_list])
    return lemmatized_tokens


def get_nouns(tag_list):
    # Input is a list of lemmas with part of speech tags, returns list of lemmas that are nouns
    nouns = [l[0] for l in tag_list if (l[1] == "NN" or l[1] == "NNS" or l[1] == "NNP" or l[1] == "NNPS")]
    return nouns

def preprocess(token_list):
    # Input is a list of tokens, returns same list of tokens and list of lemmas that are nouns
    lemmas = get_unique_lemmas(token_list)
    tags = nltk.pos_tag(lemmas)
    print("Parts of Speech: ")
    for tag in tags[:20]:
        print(tag)

    noun_lemmas = get_nouns(tags)
    print("Number of tokens: " + str(len(token_list)))
    print("Number of unique nouns: " + str(len(noun_lemmas)) + "\n")
    return token_list, noun_lemmas


def guessing_game(word_list):
    # Input is a list of words, user guesses until score is depleted or ! is entered
    print("\nLet's play a word guessing game!")
    score = 5
    while True:
        curr_word = random.choice(word_list)
        # guessed contains underscores to represent blanks for each letter in the current word
        guessed = " ".join(["_" for c in curr_word])
        # continue until score is depleted or guessed contains no more blanks
        while score >= 0 and "_" in guessed:
            print(guessed)
            next_char = input("Guess a letter: ").lower()
            if next_char == "!":
                print("Final score is " + str(score))
                exit()
            elif len(next_char) > 1 or not next_char.isalpha:
                score -= 1
                print("Sorry, that is not a letter. Score is " + str(score))
            elif next_char in guessed:
                score -= 1
                print("Sorry, that letter has been guessed. Score is " + str(score))
            elif next_char in curr_word:
                score += 1
                print("Right! Score is " + str(score))

                # replace blank with the successfully guessed character
                index = 0
                for char in curr_word:
                    if char == next_char:
                        guessed = "".join([guessed[:index], next_char, guessed[index + 1:]])
                    index += 2
            else:
                score -= 1
                print("Sorry, guess again. Score is " + str(score))

        if score < 0:
            print("Game over!")
            exit()
        else:
            print("You solved it!")
            print("Current score: " + str(score))
            print("\nGuess another word")


if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            # raise an exception if sys args does not have a file path
            raise Exception("Missing file path")
        else:
            filePath = sys.argv[1]
            fileText = read_data(filePath)
            tokens, unique_tokens = get_tokens(fileText)
            lexDiversity = len(unique_tokens) / len(tokens)
            print("Lexical Diversity: {:.2f}".format(lexDiversity))

            tokens, nouns = preprocess(tokens)
            noun_dict = {}
            # create a dictionary mapping nouns to their frequency in the text
            for token in tokens:
                if token in nouns:
                    if token in noun_dict:
                        noun_dict[token] = noun_dict[token] + 1
                    else:
                        noun_dict[token] = 1

            # sort the noun dictionary in order of descending frequency
            noun_keys = list(noun_dict.keys())
            noun_counts = list(noun_dict.values())
            np_noun_counts = numpy.array(noun_counts)
            sorted_nouns = (-np_noun_counts).argsort()[:50]
            sorted_dict = {noun_keys[i]: noun_counts[i] for i in sorted_nouns}
            print(sorted_dict)

            # play a game using the 50 most common nouns
            game_list = [noun_keys[i] for i in sorted_nouns]
            guessing_game(game_list)

    except Exception as exception:
        print(exception.args)
        exit()
