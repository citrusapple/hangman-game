# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
       if letter not in lettersGuessed:
           return False
    else:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    board = []
    for letter in secretWord:
        if letter not in lettersGuessed:
            board.append("_")
        if letter in lettersGuessed:
            board.append(letter)
    board = " ".join(board)
    return board
    print (board)  



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in alpha:
            alpha.remove(letter)
    alpha = "".join(alpha)
    return alpha
    print (alpha)

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is", len(secretWord), "letters long.")
    print ("------------")
    count = 8
    lettersGuessed = []
    while isWordGuessed(secretWord, lettersGuessed) == False and count > 0:
        print ("You have", count, "guesses left.")
        print ("Available Letters:", getAvailableLetters(lettersGuessed))
        letterInput = input("Please guess a letter: ")
        if letterInput in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print("------------")
        else:
            lettersGuessed.append(letterInput.lower())
            if letterInput in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                print("------------")
            if letterInput not in secretWord:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                print("------------")
                count -= 1
    if isWordGuessed(secretWord, lettersGuessed) == True and count > 0:
        print ("Congratulations, you won!")
    if isWordGuessed(secretWord, lettersGuessed) == False and count == 0:
        print("Sorry, you ran out of guesses. The word was", secretWord)


hangman("else")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
