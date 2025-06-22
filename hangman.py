import random

# Step 1: Define word list
word_list = ['apple', 'robot', 'train', 'chair', 'light']
chosen_word = random.choice(word_list)

# Step 2: Setup game variables
guessed_word = ['_'] * len(chosen_word)
guessed_letters = []
max_wrong_guesses = 6
wrong_guesses = 0

print("Welcome to Hangman!")
print("Guess the word:", ' '.join(guessed_word))

# Step 3: Game loop
while wrong_guesses < max_wrong_guesses and '_' in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Correct!")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[index] = guess
    else:
        wrong_guesses += 1
        print(f"Wrong! You have {max_wrong_guesses - wrong_guesses} guesses left.")

    print("Word so far:", ' '.join(guessed_word))
    print("Guessed letters:", ', '.join(guessed_letters))

# Step 4: Game end
if '_' not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n😢 Out of guesses! The word was:", chosen_word)
