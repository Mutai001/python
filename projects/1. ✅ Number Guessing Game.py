
# Number Gueseing Game 
import random 

number = random.randint(1,  100)
guess = None

while guess != number:
    guess = int(input ("Guess a number betweeen I and 100: "))
  
    if guess < number:
            print("Too low! Try again.")
    elif guess > number:
            print("Too high! Try again.")
    else:
            print("🎉🎉🎉Correct! You have guesed the number.")
