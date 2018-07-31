import random
import time

low_number = 1
high_number = 100

print("Hey computer let's play guess the number.")

guess_count = 0

computer_guess = random.randint(1, 101)

user_input = int(input("Enter your number: "))

def computer_guesses_the_number(user_input):
    global guess_count
    global low_number
    global high_number
    global computer_guess

    while computer_guess != user_input:
        guess_count += 1
        print("Wait for a few seconds please, ", computer_guess)
        time.sleep(4)

        if computer_guess > user_input:
            high_number = computer_guess
        elif computer_guess < user_input:
            low_number = computer_guess + 1

        computer_guess = (low_number + high_number)//2

    print("Your guess", computer_guess, "is right")
    print("And you took", guess_count,"number of guesses")

computer_guesses_the_number(user_input)




