import random
num=random.randint(1,100)
print("Random number is generated")
n=int(input("Enter your guess:"))
if num==n:
    print("Correct!")
else:
    print("Wrong guess")
