import random

# List of words and their corresponding hints
words_with_hints = {
    'rainbow': 'A natural phenomenon with 7 colors.',
    'computer': 'An electronic device for processing data.',
    'science': 'A systematic study of the natural world.',
    'programming': 'The process of writing computer code.',
    'python': 'A popular programming language.',
    'mathematics': 'The study of numbers and shapes.',
    'player': 'A person involved in a game or sport.',
    'condition': 'A state or situation of something.',
    'reverse': 'To go backward or opposite.',
    'water': 'A liquid essential for life.',
    'board': 'A flat surface for writing or games.',
    'geeks': 'People who are passionate about technology.'
}
def play():
    name = input("What is your name? ")
    play_game(name)
def play_game(name):
        # Randomly choosing one word and its hint
        word, hint = random.choice(list(words_with_hints.items()))
    
        # Asking for the user's name
        
        print("Good Luck!", name)
    
        print("\nHint: " + hint)  # Display the hint
        print("\nGuess the characters of the word!")
        guesses = ''  # Stores guessed characters
    
        # Game loop
        while True:
            failed = 0  # Counter for missing guesses
    
            # Display the word with guessed characters or underscores
            for char in word:
                if char in guesses:
                    print(char, end=" ")
                else:
                    print("_", end=" ")
                    failed += 1
    
            print()  # Newline for readability
    
            # If all characters are guessed
            if failed == 0:
                print("\nYou Win!")
                print("The word is:", word)
                break
    
            # Prompt the user to guess a character
            guess = input("Guess a character: ").lower()
    
            # Add the guess to the guessed characters
            guesses += guess
    
            # Check if the guess is incorrect
            if guess not in word:
                play_again=str(input("\nWrong guess! Do You Want to restart the  game... ?(Y/N) Press"))
                if play_again.lower()=="y":
                   play_game(name)  # Restart the game
                   return
                else:
                    print("Thank You For Playing ")
                    break
               
# Start the game
play()