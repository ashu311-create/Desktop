import random
playing=True
num=str(random.randint(10,20))
print("I will generate  random number from 10 to 20, try to guess what it is")
print("You win if you get 1 right")
while playing:
    guess=input("Give me your best guess \n")
    if num==guess:
        print("You win the game")
        print("The number was",num)
        break
    else:
        print("Your guess isnt right, try again")