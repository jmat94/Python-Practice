import random

name = input("Hi, please enter your name: ")

print("Hi", name, "Let us play the game of guessing the number.")
guess_count = 0

random_number = random.randint(1, 11)

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

    print("You took", guess_count, "number of guesses")

guess_a_number()