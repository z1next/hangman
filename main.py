# src/main.py
import sys
from word_picker import pick_word
from game_engine import init_game, process_guess, is_won, is_lost
from ui import render_state

# Built-in word lists per difficulty
WORD_LIST = {
    'easy':   ['CAT','DOG','TREE','BOOK','GAME','CODE'],
    'medium': ['PYTHON','HANGMAN','PUZZLE','WIZARD','MATRIX','ADVENTURE'],
    'hard':   ['DUNGEON','GALAXY','ALGORITHM','FRAMEWORK','DEVELOPER'],
    'impossible': ['CRYPTOGRAPHY','QUIZZICAL','XYLOPHONE','JUXTAPOSE','ZOOLOGICAL']
}

# Maximum wrong guesses per difficulty
DIFFICULTY_SETTINGS = {
    'easy':       10,
    'medium':     8,
    'hard':       6,
    'impossible': 4
}

def choose_level():
    print('Select difficulty:', ', '.join(WORD_LIST.keys()))
    while True:
        lvl = input('> ').lower().strip()
        if lvl in WORD_LIST:
            return lvl
        print('Invalid choice, try again.')


def main():
    while True:
        level = choose_level()
        max_wr = DIFFICULTY_SETTINGS[level]
        word = pick_word(WORD_LIST, level)
        state = init_game(word, max_wr)
        print(f"\nStarting {level.upper()} (max wrong: {max_wr})\n")

        while not (is_won(state) or is_lost(state)):
            print(render_state(state))
            guess = input('Guess a letter: ').strip()
            # Validate input: must be single A-Z letter
            if len(guess) != 1 or not guess.isalpha():
                print('Please enter a single letter A-Z.')
                continue

            state, result = process_guess(state, guess)
            if result is None:
                print('You already guessed that letter.')
            elif result:
                print('Correct!')
            else:
                print('Wrong!')

        print(render_state(state))
        if is_won(state):
            print(f"You win! The word was {word}.")
        else:
            print(f"Game over. The word was {word}.")

        if input('Play again? (y/n): ').lower().startswith('y'):
            continue
        break

    sys.exit()

if __name__ == '__main__':
    main()
