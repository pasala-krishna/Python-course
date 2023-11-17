import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words)

def display_flower_growth(incorrect_guesses):
    growth_stages = ["🌱", "🌱🌿", "🌱🌿🌷", "🌱🌿🌷🌻", "🌱🌿🌷🌻🌼", "🌱🌿🌷🌻🌼🌹", "🌱🌿🌷🌻🌼🌹🌸"]
    return growth_stages[:incorrect_guesses]

def play_hangman():
    word = choose_random_word()
    word_state = ['_'] * len(word)
    incorrect_guesses = 0
    max_attempts = len(display_flower_growth(-1))
    guessed_letters = []

    print("Welcome to Hangman!")

    while incorrect_guesses < max_attempts:
        print("\nWord: " + " ".join(word_state))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    word_state[i] = guess
        else:
            incorrect_guesses += 1
            print("Flower Growth: " + " ".join(display_flower_growth(incorrect_guesses)))

        if "_" not in word_state:
            print("\nCongratulations! You've guessed the word: " + word)
            break

    if "_" in word_state:
        print("\nYou've run out of attempts! The word was: " + word)

play_hangman()
