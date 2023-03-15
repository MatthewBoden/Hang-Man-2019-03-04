import random

# This takes the 4 text files, selects one, and picks a random word from the list
# This then sets the count/amount of guesses to 7 (what they start off with)
# Variables
files = ["Technology", "Video Games", "Fruits", "School Subjects" ]
Topic = files[random.randint(0,len(files)-1)]
choice = open(Topic,'r')
list = choice.read().split("\n")
choice.close()
secret_word = random.choice(list)
missing_letters = len(secret_word)
guessedLetters=""
# number of tries
count = 7
############_________________________Graphics_________________________###############
man7 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO   OOo        | @|
  oO       Oo       |  |
  OO       OOo      |  |
  *O       OO*      |  |
  *O        O*      |  |
   *O      O*       |  |
    *OOOOOO*        |  |
                    | ||
 ___________________| ||__
  \  \  \  \ \ \ \  ||||  \.
  \   \  \  \ \ \  _ | ||\ \.
  \  \  \  \ \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \.
 \  \  \  \  \ \  \  \  \  \  \.
  \  \  \  \ \  \  \  \  \ \   \.
  \  \  \  \ \  \  \  \  \ \ \  \.
 \  \  \  \  \  \  \  \  \ \ \   \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''
man6 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ O O /OO*      |  |
   *| <   |O*       |  |
     \_O_/          |  |
                    |  |
                    | ||
 ___________________| ||__
  \  \  \  \ \ \ \  ||||  \.
  \   \  \  \ \ \  _ | ||\ \.
  \  \  \  \ \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \.
 \  \  \  \  \ \  \  \  \  \  \.
  \  \  \  \ \  \  \  \  \ \   \.
  \  \  \  \ \  \  \  \  \ \ \  \.
 \  \  \  \  \  \  \  \  \ \ \   \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''
man5 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ O O /OO*      |  |
   *| <   |O*       |  |
   | \_O_/ |        |  |
   |       |        |  |
   |       |        | ||
   |       |________| ||__
   |_______\ \ \ \  ||||  \.
  \   \  \  \ \ \  _ | ||\ \.
  \  \  \  \ \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \.
 \  \  \  \  \ \  \  \  \  \  \.
  \  \  \  \ \  \  \  \  \ \   \.
  \  \  \  \ \  \  \  \  \ \ \  \.
 \  \  \  \  \  \  \  \  \ \ \   \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''
man4 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ O O /OO*      |  |
   *| <   |O*       |  |
   | \_O_/ |        |  |
   |       |        |  |
   |       |        | ||
   |       |________| ||__
   |_______\ \ \ \  ||||  \.
  \  \ |    \ \ \  _ | ||\ \.
   \   |    |\  \  \  \  \  \.
  \ \  |    | \  \  \  \  \  \.
  \ \  |    |\ \  \  \  \  \  \.
  \  \ |___| \  \  \  \  \ \   \.
   \ \ \###| \  \  \  \  \ \ \  \.
  \   \ \##/ \  \  \  \  \ \ \   \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''

man3 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ O O /OO*      |  |
   *| <   |O*       |  |
   | \_O_/ |        |  |
   |       |        |  |
   |       |        | ||
   |       |________| ||__
   |_______\ \ \ \  ||||  \.
  /         \ \ \  _ | ||\ \.
  |    V    |\  \  \  \  \  \.
  |    |    | \  \  \  \  \  \.
  |    |    |\ \  \  \  \  \  \.
  |___| |___| \  \  \  \  \ \  \.
  |###/ \###| \  \  \  \  \ \ \ \.
  \##/   \##/ \  \  \  \  \ \ \  \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''

man2 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ O O /OO*      |  |
  /*| <   |O*       |  |
 |   \_O_/ |        |  |
 |         |        |  |
 | |       |        | ||
 | |       |________| ||__
 |_/_______\ \ \ \  ||||  \.
  /         \ \ \  _ | ||\ \.
  |    V    |\  \  \  \  \  \.
  |    |    | \  \  \  \  \  \.
  |    |    |\ \  \  \  \  \  \.
  |___| |___| \  \  \  \  \ \  \.
  |###/ \###| \  \  \  \  \ \ \ \.
  \##/   \##/ \  \  \  \  \ \ \  \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''

man1 = '''
    ___________________
    |_______________``\`
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ O O /OO*      |  |
  /*| <   |O*\      |  |
 |   \_O_/    \     |  |
 |            |     |  |
 | |       |  |     | ||
 | |       |  |_____| ||__
 |_/_______\__|  \  ||||  \.
  /         \_|\  _ | ||\  \.
  |    V    |\  \  \  \  \  \.
  |    |    | \  \  \  \  \  \.
  |    |    |\ \  \  \  \  \  \.
  |___| |___| \  \  \  \  \ \  \.
  |###/ \###| \  \  \  \  \ \ \ \.
  \##/   \##/ \  \  \  \  \ \ \  \.
  ------------\--- \  \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|__\.

'''

man0 = '''
    ___________________
    |_______________ `\`
      [/]           [  ]
      [\]           | ||
      [/]           |  |
      [\]           |  |
      [/]           || |
     [---]          |  |
     [---]          |@ |
     [---]          |  |
    oOOOOOo         |  |
   oOO___OOo        | @|
  oO/|||||\Oo       |  |
  OO/|||||\OOo      |  |
  *O\ X X /OO*      |  |
  /*| <   |O*\      |  |
 |   \_O_/    \     |  |
 |            |     |  |
 | |       |  |     | ||
 | |       |  |_____| ||__
 |_/_______\__|  \  ||||  \.
  /         \_|\  _ | ||\  \.
  |    V    |\  \//\  \  \  \.
  |    |    | __//  \  \  \  \.
  |    |    |\|//|\  \  \  \  \.
  ------------\--- \  \  \  \  \.
  \  \  \  \  \  \  \  \  \  \  \.
  _\__\__\__\__\__\__\__\__\__\__\.
  __|__|__|__|__|__|__|__|__|__|__|
  |___| |___|
  |###/ \###|
  \##/   \##/
   ``     ``
'''
############________________________Title of game_______________________###############
print('''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \`
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
_______________________________________________
                   ''')
############_____________________________Rules_____________________________###############
print("Rules: "
      "The rules are simple, you have to guess the word by suggesting letters, within a 7 guesses.\n"
      "The words are random, try to save the man. Good luck!\n"
      "_______________________________________________________________________________________________")
#sets category
#gives how many attempts and length of word/amt of letters
print(man7)
print("The category is", Topic)
print("\n", count, "Attempts left!")

#used to check when the game is over
missing_letters = len(secret_word)

for letter in secret_word:
    if (letter not in guessedLetters):
        print ("__", end=" ")

#Tells you what letters you used
print("Used Letters: ", guessedLetters)

while missing_letters > 0 and count > 0:
    guess = input("\nGuess a letter: ").lower()
    if guess == " ":
        print("Do not put spaces! Enter a valid input!")
    if guess == secret_word:
        missing_letters = 0
# 2 dif winner statements for when missing letters = 0 and for when you guess the word by typing it out.
        print('''\n
                   ___               ___   ___
            |   |   |   |\  | |\  | |     |   |
            | + |   +   | + | | + | |-+-  |-+-
            |/ \|   |   |  \| |  \| |     |  \.
                   ---               ---

        YOU HAVE SAVED THE MAN!, THE WORD WAS''', secret_word)
# This checks the guess and runs it through all of these to see if they fit
    elif guess in guessedLetters:
        print("You already guessed that letter, Enter a valid input!")
    elif guess.isdigit():
        print("Invalid Input, do not enter a number!")
    elif len(guess) > 1:
        print("Do not enter multiple characters!")
    elif not guess.isalpha():
        print("Invalid Input, Enter a valid input!")
#When guess is a str and it is not already guessed, it adds the guess to the guessed letter
    else:
        if guess.isalpha():
            if guess not in guessedLetters:
                guessedLetters += guess

#prints hangman and changes the count, as well as re-printing the word/guessed and unguessed letters

                missing_letters = len(secret_word)
                if (guess  not in guessedLetters or guess not in secret_word):
                    count -= 1
                    if count == 6:
                        print(man6)
                    elif count == 5:
                        print(man5)
                    elif count == 4:
                        print(man4)
                    elif count == 3:
                        print(man3)
                    elif count == 2:
                        print(man2)
                    elif count == 1:
                        print(man1)
                    print("\n", count, "Attempts left!")
                else:
                    if count == 7:
                        print(man7)
                    elif count == 6:
                        print(man6)
                    elif count == 5:
                        print(man5)
                    elif count == 4:
                        print(man4)
                    elif count == 3:
                        print(man3)
                    elif count == 2:
                        print(man2)
                    elif count == 1:
                        print(man1)
                    print("\n", count, "Attempts left!")
                for letter in secret_word:
                    if (letter in guessedLetters):
                        print (letter, end=" ")
                        missing_letters -= 1
                    else:
                        print ("__", end=" ")

                print("Used Letters: ", guessedLetters)
############_________End game: Win when missing letters = 0_________############
                if missing_letters == 0:
                    print('''\n
           ___               ___   ___
    |   |   |   |\  | |\  | |     |   |
    | + |   +   | + | | + | |-+-  |-+-
    |/ \|   |   |  \| |  \| |     |  \.
           ---               ---

YOU HAVE SAVED THE MAN!, THE WORD WAS''', secret_word)

############_______________________________End game: Loss______________________________###############
if count >= 0 and missing_letters > 0:
    print(man0)
    print('''
       ___                     ___   ___   ___
 \ /  |   | |   |       |     |   | |     |
  +   |   | |   |       |     |   |  -+-  |-+-
  |   |   | |   |       |     |   |     | |
  |    ---   ---         ---   ---   ---   ---

          THE MAN HAS BEEN HUNG\n
          The Word was''', secret_word)
