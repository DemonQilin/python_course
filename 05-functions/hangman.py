from random import choice

words = ['python', 'variable', 'function', 'algorithm', 'loop',
         'database', 'debugging', 'syntax', 'code', 'interface']
alphabet = 'abcdefghijklmnñopqrstuvwxyz '


def get_random_word():
    return choice(words)


def request_letter_to_user():
    letter = ''

    while True:
        letter = input('Type a letter: > ')
        if letter in alphabet:
            break
        else:
            print(f'The letter "{letter}" is not valid')

    return letter


def get_advance(word, letter):
    text_only_letter = [char.upper() if char.upper(
    ) == letter.upper() else "_" for char in word]

    return "".join(text_only_letter)


def join_advances(advance1, advance2):
    final_advance = []

    for pair in zip(advance1, advance2):
        match pair:
            case ("_", "_"):
                final_advance.append("_")
            case ("_", letter):
                final_advance.append(letter)
            case (letter, "_"):
                final_advance.append(letter)

    return "".join(final_advance)


def main():
    print("========================= HANGMAN =========================\n")
    print("You have 6 lives to guess the word one letter at a time\nLet's start")

    lives = 6
    word = get_random_word()
    advance = "_" * len(word)

    while lives > 0:
        print(f"\n❤ {lives}")
        print(f"Your advance: {advance}")
        letter = request_letter_to_user()

        if letter.lower() in word.lower():
            advance_for_letter = get_advance(word, letter)
            advance = join_advances(advance, advance_for_letter)

            if advance.lower() == word.lower():
                print(f'\nCongratulations, you guessed the word "{word}"')
                print("YOU WON!!!")
                break
        else:
            lives -= 1
            print(f'The word has not the letter "{letter}"')
    else:
        print(
            f'\nYou have spent all your lives and have not been able to guess the word "{word}"')
        print("YOU LOSE!!!")

    print("\n========================= HANGMAN =========================")


main()
