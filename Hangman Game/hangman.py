"""
File: hangman.py
Name:劉亭方
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random

# This constant controls the number of guess the player has.
N_TURNS = 7

def main():
    """
    1. 設定空字串，方便猜對後填入
    2. 猜對猜錯先顯示對錯，再來處理猜對單字填入空字串的部分
    3. 可以一直猜到可猜次數規0，或猜到空字串裡沒有 ' - ' 符號
    """
    count = N_TURNS
    word = random_word()
    guess = len(word) * '-'
    # print(word)
    print('The word looks like: ' + guess)
    print('You have ' + str(count) + ' wrong guesses left.')
    while count > 0:
        ch = str(input('Your guess: '))
        string = ''
        if ch.isalpha() and len(ch) == 1:
            if ch.upper() in word:
                print('You are correct!')
            else:
                print("There is no " + ch.upper() + "'s in  the word.")
                count -= 1
                if count == 0:
                    break
            hangman(count)
            for i in range(len(word)):
                if ch.upper() in word[i]:
                    string += ch.upper()
                else:
                    string += guess[i]
            guess = string
            # print(guess)
            if '-' not in guess:
                print('You win!!!')
                break
            print()
            print('The word looks like: ' + guess)
            print('You have ' + str(count) + ' wrong guesses left.')
        else:
            print('Illegal format.')
    if count == 0:
        print()
        print("========")
        print("|    |  ")
        print("|  (X.X)")
        print("|  ~ # ~")
        print("|    #  ")
        print("|   / \ ")
        print("|  LOSE!")
        print('You are completely hung :( ')
    print('The answer is: ' + word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"
    

def hangman(count):
    if count == N_TURNS:
        print("========")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif count == N_TURNS-1:
        print("========")
        print("|    |  ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif count == N_TURNS-2:
        print("========")
        print("|    |  ")
        print("|   ( ) ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif count == N_TURNS-3:
        print("========")
        print("|    |  ")
        print("|   ( ) ")
        print("|    #  ")
        print("|    #  ")
        print("|       ")
        print("|       ")
    elif count == N_TURNS-4:
        print("========")
        print("|    |  ")
        print("|   ( ) ")
        print("|  ~ # ~")
        print("|    #  ")
        print("|       ")
        print("|       ")
    elif count == N_TURNS-5:
        print("========")
        print("|    |  ")
        print("|   ( ) ")
        print("|  ~ # ~")
        print("|    #  ")
        print("|   / \ ")
        print("|       ")
    elif count == N_TURNS-6:
        print("========")
        print("|    |  ")
        print("|  (0.0)")
        print("|  ~ # ~")
        print("|    #  ")
        print("|   / \ ")
        print("|       ")




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
