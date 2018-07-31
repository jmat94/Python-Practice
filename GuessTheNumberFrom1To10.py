import random

# Ask the user for their name.
name = input("Hi, please enter your name: ")

print("Hi", name, "let us play the game of guessing the number.")
guess_count = 0

# Generate a random number between 1 and 10.
random_number = random.randint(1, 11)

# Function to guess the number.
def guess_a_number():
    global guess_count

    while guess_count < 4:
        print("Make a guess and see if it matches with the number.")
        your_number = int(input("Enter a number: "))
        guess_count += 1

        if your_number < random_number:
            print("Your number is smaller.")

        if your_number > random_number:
            print("Your number is greater")

        if your_number == random_number:
            print("Congrats")
            break
    
    # Count the total number of guesses you made
    if guess_count == 1:
        print("You got it in 1 guess")
    else:
        print("You took", guess_count, "number of guesses")

guess_a_number()
