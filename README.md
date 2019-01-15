# hangman-game
This is a hangman game program that I have written for coursework with knowledge gained while taking the course "MITx: 6.00.1x Introduction to Computer Science and Programming Using Python" on edX

When running, the program states to user the amount of words loaded from a separate txt file for game play and randomly chooses one word.  This word's length is shown with corresponding blanks and the alphabet that player can choose guesses from.  

![hamgman game output when executed](https://github.com/citrusapple/hangman-game/blob/master/gamescreenshot.PNG)

When a character guessed is not in the word, the program outputs "oops! that letter is not in my word" and the number of guesses left decrements by 1.  The alphabet available for guesses will also change to be without the incorrect letter.

![hangman game output for incorrect guesses](https://github.com/citrusapple/hangman-game/blob/master/gamescreenshot2.PNG)

When a guess is correct, the letter will replace blanks in corresponding places within the word and guesses left will remain unchanged.

![hangman game output for correct guesses](https://github.com/citrusapple/hangman-game/blob/master/gamescreenshot3.PNG)

When a player guesses all the correct letters within the word before they run out of tries, the game will output "Congratulations, You won!" and display the full word.

![hangman game winning output](https://github.com/citrusapple/hangman-game/blob/master/gamescreenshot4.PNG)

If a player used up all guesses before guessing the word, the game will output the correct answer with "Sorry you ran out of guesses, the word was (word)"

![hangman game losing output](https://github.com/citrusapple/hangman-game/blob/master/gamescreenshot5.PNG)
