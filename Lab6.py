import random
number = random.randint(1,10)
count = 0
for i in range(3):
    print(i)
    userIn = input("Guess a number between 1 and 10, you only have 3 chances! ")
    count += 1
    if int(userIn) == number:
        print(f"You guessed {userIn}. That is right! You win!")
        break
    else:
        print(f"You guessed {userIn}. Sorry, that isn’t it. Try again, you used {count} of your guesses.")
