import random  

number = random.randint(1, 100)  
guess = None  

while guess != number:  
    try:  
        guess = int(input("Guess a number between 1 and 100: "))  

        if guess < number:  
            print("Too low! Try again.")  
        elif guess > number:  
            print("Too high! Try again.")  
        else:  
            print("🎉🎉🎉 Correct! You have guessed the number.")  
    except ValueError:  
        print("❌ Invalid input! Please enter a number between 1 and 100.")  
