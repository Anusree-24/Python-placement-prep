import random
choices=["rock","paper","scissor"]
computer=random.choice(choices)
user=input("Enter your choice:")
print("computer chose:",computer)
if user==computer:
    print("its a tie!")
elif(user=="rock" and computer=="scissor") or \
(user=="scissor" and computer=="paper") or \
(user=="paper" and computer=="rock"):
    print("user wins")
else:
    print("computer wins")
