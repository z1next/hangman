# Hangman: Difficulty Levels

#### Video Demo: <https://youtu.be/YOUR\_VIDEO\_ID\_HERE>

#### Description:

Hangman: Difficulty Levels is a console-based Python game that challenges players with four distinct difficulty tiers:

* **Easy:** Common short words, 10 wrong guesses allowed.
* **Medium:** Moderate-length words, 8 wrong guesses allowed.
* **Hard:** Longer, more complex words, 6 wrong guesses allowed.
* **Impossible:** Rare or very long words, only 4 wrong guesses allowed.

At startup, the user selects a difficulty level, then tries to guess the hidden word one letter at a time. Correct letters are revealed in place; wrong letters add parts to an ASCII-art gallows. The game ends when the word is fully revealed (win) or the gallows is completed (loss), then offers the option to play again.

This project demonstrates:

* **Modular design:** Separate modules for word selection (`word_picker.py`), game logic (`game_engine.py`), and display (`ui.py`), all orchestrated by `main.py`.
* **Algorithmic thinking:** Linear-time word scanning and display updates (O(n) per guess, where n is word length).
* **Solo project management:** End-to-end planning, coding, and documentation handled individually.

## Project Structure

```
hangman/
│
├─ data/
│   └─ words.txt          # Optional custom word list (one word per line)
│
├─ src/
│   ├─ word_picker.py     # Loads words and picks by difficulty
│   ├─ game_engine.py     # Core game state and guess logic
│   ├─ ui.py              # ASCII gallows and display routines
│   └─ main.py            # Entry point & game loop
│
├─ tests/
│   ├─ test_word_picker.py
│   ├─ test_game_engine.py
│   └─ test_ui.py
│
└─ README.md              # This file
```

## Installation & Running

This project requires only **Python 3.8+**—no additional libraries are needed. To play from the repository root:

1. Open your terminal or VS Code integrated terminal.
2. Navigate into the project folder if you aren’t already:

   ```bash
   cd hangman
   ```
3. Launch the game:

   ```bash
   python main.py
   ```

That’s all—just type letters when prompted to make guesses.
