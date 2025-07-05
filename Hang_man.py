secret_word = 'python'
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("_" * len(secret_word))

while attempts > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You have already gussed a letter. ")
        continue
    
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Correct 😎!!")
    else:
        attempts -= 1
        print(f"Wrong! you have {attempts} attempts left ☹. ")
        
    display_word = ""
    for letters in secret_word:
        if letters in guessed_letters:
            display_word += letters + " "
        else:
            display_word += "_"
    print(display_word.strip())
    
    if all(letters in guessed_letters for letters in secret_word):
        print("Congratulations🎉 You guessed the word!")
        break
else:
    print("Game over! The word was:", secret_word)
        
    