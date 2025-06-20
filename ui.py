# src/ui.py
HANGMAN_PICS = [
    '  +---+',
    '  |   |',
    '      |',
    '      |',
    '      |',
    '      |',
    '========='
]


def render_hangman(wrong):
    pic = HANGMAN_PICS.copy()
    if wrong >= 1: pic[2] = '  O   |'
    if wrong >= 2: pic[3] = '  |   |'
    if wrong >= 3: pic[3] = ' /|   |'
    if wrong >= 4: pic[3] = ' /|\\  |'
    if wrong >= 5: pic[4] = ' /    |'
    if wrong >= 6: pic[4] = ' / \\  |'
    return '\n'.join(pic)


def render_state(state):
    out = render_hangman(state['wrong']) + '\n'
    out += f"Word:  {' '.join(state['hidden'])}\n"
    out += f"Wrong: {state['wrong']}/{state['max_wrong']}\n"
    out += 'Used: ' + ' '.join(sorted(state['used']))
    return out
