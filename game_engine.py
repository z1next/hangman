# src/game_engine.py

def init_game(word, max_wrong):
    return {
        'word': list(word),
        'hidden': ['_' for _ in word],
        'used': set(),
        'wrong': 0,
        'max_wrong': max_wrong
    }


def process_guess(state, guess):
    guess = guess.upper()
    if guess in state['used']:
        return state, None  # None means repeated
    state['used'].add(guess)
    if guess in state['word']:
        for i, c in enumerate(state['word']):
            if c == guess:
                state['hidden'][i] = guess
        return state, True
    else:
        state['wrong'] += 1
        return state, False


def is_won(state):
    return '_' not in state['hidden']


def is_lost(state):
    return state['wrong'] >= state['max_wrong']
