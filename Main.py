import random
from Hangman import hangman_logo,stages
from WordList import word_list

# Initialize variables
lives = 6
random_word = random.choice(word_list)
word_length = len(random_word)
display = ["_"] * word_length
end_of_game = False

# Display welcome message and game logo
print("Welcome to Hangman Game!!!\n")
print(hangman_logo)


while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()

     # Validate user input
    if not guessed_letter.isalpha() or len(guessed_letter) != 1:
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guessed_letter in display:
        print("You already guessed this letter. Try a different one.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print(stages[0])
            print(f"\nYou lost.The word was: {random_word}")
        print(display)
        print(stages[lives]) 
        print(f"Remaining lives: {lives}")   
        continue

    # Check if the guessed letter is in the word
    for position in range(word_length) :
        letter = random_word[position]
        if guessed_letter == letter:
            display[position] = letter
    if guessed_letter not in random_word:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        lives-=1
        if lives == 0:
            end_of_game = True
            print(stages[0])
            print(f"\nYou lost.The word was: {random_word}")

    print(" ".join(display))

    # Check if the player has guessed all letters
    
    if "_" not in display:
        end_of_game = True
        print("\nCongratulatuions! You saved the person.")
    
    print(stages[lives])
    print(f"Remaining lives: {lives}")

# End of game
if "_" in display:
    print(stages[0])
    print(f"\nYou couldn't save the person. The word was: {random_word}")

    