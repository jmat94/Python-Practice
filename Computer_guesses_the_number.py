import random
import time

low_number = 1
high_number = 100

print("Hey computer let's play guess the number.")

guess_count = 0

#The computer generates a random number.
computer_guess = random.randint(1, 101)

# The user specifies their number.
user_input = int(input("Enter your number: "))

# Function to guess the number.
def computer_guesses_the_number(user_input):
    global guess_count
    global low_number
    global high_number
    global computer_guess

    while computer_guess != user_input:
        guess_count += 1
        print("Wait for a few seconds please, ", computer_guess)
        
       # I have given a delay of 4 seconds after each guess.
        time.sleep(4)

        if computer_guess > user_input:
            high_number = computer_guess
        elif computer_guess < user_input:
            low_number = computer_guess + 1

        computer_guess = (low_number + high_number)//2
     
    print("Your guess", computer_guess, "is right")
    
    if guess_count == 1:
        print("You took 1 guess.")
    else:
        print("And you took", guess_count,"number of guesses")
    
    

computer_guesses_the_number(user_input)




