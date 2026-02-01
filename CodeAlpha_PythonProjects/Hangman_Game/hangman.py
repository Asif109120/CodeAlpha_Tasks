import random

words = ["python", "java", "react", "django", "flask"]
word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman Game!")

while attempts > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print("❌ Wrong guess! Attempts left:", attempts)
    else:
        print("✅ Correct guess!")

if attempts == 0:
    print("😢 You lost! The word was:", word)
