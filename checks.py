#This is a guess the number game
import random

name = input("Hello! what is you name: ")
print("Hello " + name + " Can you gues what number i am thinking between 1 to 20: ")
num2 = random.randint(1, 21)


print("DEBUG: secret number is :" + str(num2))

for num in range(1,7):
    print("Take a guess")
    guess_num = int(input())
    if guess_num > num2:
        print("Your number is too high, think little lower")
    elif guess_num < num2:
        print("Your number is too low, think little higher number")
    else:
        break


if guess_num == num2:
    print("Good job!" + name + " you guessed my number " + str(num2) + " in " + str(num) + " time")
else:
    print("Nope! The number i was thinking was " + str(num2))
