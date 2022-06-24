import requests


def getword():
    # This functions helps us to get a random word using the API from http://random-word-api.herokuapp.com/home
    response = requests.get('https://random-word-api.herokuapp.com/word')
    # print(response.status_code)
    return response.json()[0]


def start_game():
    print('Thank you for playing hangman.')
    while True:
        user_start = input('Ready to start? (Y/N): ')
        if user_start == 'Y' or user_start == 'y':
            print("Ok! Let's go!")
            word = getword()
            word_revealed = '_' * len(word)
            print(word)
            print('Your word has', len(word), 'letters:')
            print(word_revealed, '\b')
            for i in range(12):
                if '_' not in word_revealed:
                    print('Congratulation! You have discovered all the letters and won the game!')
                    break
                print('--------------------------')
                letter_chosen = input('Please chose a letter: ')
                word_revealed = check_answer(word, letter_chosen, word_revealed)
                print(word_revealed, '\b You have', 12 - i, 'attempts left')
                print('')
                print('---------------------------')
            break
        elif user_start == 'N':
            print("Let's play another time.")
            break
        else:
            print('Invaid input. Please enter Y or N \b')
            continue


def check_answer(word, letter_chosen, word_revealed):
    if letter_chosen in word and letter_chosen not in word_revealed:
        print('The letter is in the word!')
    elif letter_chosen in word_revealed:
        print('You have already chosen this letter. Please chose another. \b')
    else:
        print('The chosen letter is not on the word \b')
    return reveal_letters(word, letter_chosen, word_revealed)


def reveal_letters(word, letter_chosen, word_revealed):
    new_word_revealed = ''
    for letter in word:
        if letter_chosen == letter or letter in word_revealed:
            new_word_revealed = new_word_revealed + letter
        else:
            new_word_revealed = new_word_revealed + '_'
    rl_word = new_word_revealed
    return rl_word


def hangman():
    start_game()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hangman()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
