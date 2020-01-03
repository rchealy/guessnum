import random
n = random.randint(1,150)
guess = int(input("Enter an integer from 1 to 150: "))
while n != "guess":
    print()
    if guess < n:
       print("Guess is low")
       guess = int(input("Enter an integer from 1 to 150: "))
    elif guess > n:
       print("Guess is high")
       guess = int(input("Enter an integer from 1 to 150: "))
    else:
       print("you guessed it!")
       break
    print()


