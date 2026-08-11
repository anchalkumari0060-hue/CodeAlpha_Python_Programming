import random

words = ["python", "computer", "coding", "developer", "programming"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.\n")

while wrong_guesses < 6:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong attempts:", wrong_guesses, "/ 6\n")
else:
    print("Game Over!")
    print("The correct word was:", word)
