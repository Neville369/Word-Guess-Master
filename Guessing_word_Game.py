import random

game_title = "WORD GUESSING"
with open("PROJECT\WORDGAME\word.txt") as word_file:
    word_bank = word_file.readlines()
    word_bank = [line.strip().lower() for line in word_bank]

random_word = random.choice(word_bank)

misplaced_letters = []
incorrect_letters = []
max_turns = 5
turns_taken = 0

print("Welcome to", game_title)
print("You are to make a guess of a word with", len(random_word), "letters.")
print("You have", max_turns - turns_taken, "turns left to guess the correct word.")

while turns_taken < max_turns:
    user_guess = input(f"What is your guess (a {len(random_word)}-letter word)? ").lower()
    
    # Validate user input
    while len(user_guess) != len(random_word) or not user_guess.isalpha():
        user_guess = input(f"Incorrect word, try again (a {len(random_word)}-letter word)? ").lower()

    # Check each letter in the guess against the word's letters
    index = 0
    for c in user_guess:
        if c == random_word[index]:
            print(c, end=" ")
            if c in misplaced_letters:
                misplaced_letters.remove(c)
        elif c in random_word:
            if c not in misplaced_letters:
                misplaced_letters.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_letters:
                incorrect_letters.append(c)
            print("_", end=" ")
        index += 1

    print("\n")
    print("Misplaced letters:", misplaced_letters)
    print("Incorrect letters:", incorrect_letters)
    turns_taken += 1

    # Check if the player has won
    if user_guess == random_word:
        print("Congratulations, you win!")
        break

    # Check if the player has lost
    if turns_taken == max_turns:
        print("Sorry, you lost. The word was", random_word)
        break

    # Display the number of turns left and ask for another guess
    print("You have", max_turns - turns_taken, "turns left.")
