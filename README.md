# pythonWordle
Simple python wordle game.

Uses an api that returns a random word based on chosen length, that you have to guess in order to win.

You must input a word.
If the word you guessed has a letter at the right place, the letter will remain as lowercase. If the letter is in the word but at another index, the letter will be shown as uppercase.

The game also remembers the wrong characters you already used.

# requirements before running:
pip install requests, pyenchant
