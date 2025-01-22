# Word Guessing Game

A simple Python-based word guessing game where players guess the characters of a randomly selected word, aided by a hint.

## Features

- Randomly selects a word from a predefined list.
- Provides a hint for each word to assist the player.
- Allows players to guess characters until they complete the word or choose to exit.
- Option to restart the game after an incorrect guess.

## How to Play

1. Run the script in a Python environment.
2. Enter your name to start the game.
3. Use the hint provided to guess the characters of the word.
4. For each incorrect guess, you'll be prompted to restart the game or exit.
5. The game ends when you correctly guess the word or choose to exit.

## Prerequisites

- Python 3.x installed on your system.



## Code Overview

- `words_with_hints`: A dictionary containing words and their corresponding hints.
- `play()`: Prompts the user for their name and starts the game.
- `play_game(name)`: The core game loop that manages guesses, checks for correctness, and handles restarting.

## Example Gameplay

```
What is your name? Alice
Good Luck! Alice

Hint: A natural phenomenon with 7 colors.

Guess the characters of the word!
_ _ _ _ _ _ _ 

Guess a character: r
r _ _ _ _ _ _ 

Guess a character: a
r a _ _ _ _ _ 

You Win!
The word is: rainbow
```

