import random
while True:
    user=("Enter a choice (Rock,Paper,Scissor):")
    possible=["Rock","Paper","Scissor"]
    computer= random.choice(possible)
    if user == computer:
        print(f"Both players selected,{user}. Its a tie")
    elif user=="Rock":
        if computer=="Scissors":
            print("Rock smashes scissors, YOU WIN!")
        else:
            print("Paper covers rock, YOU LOSE!")
    elif user=="Scissor":
        if computer=="Paper":
            print("Scissor cuts paper, YOU WIN!")
        else:
            print("Rock smashes scissor, YOU LOSE!")
    elif user=="Paper":
        if computer=="Rock":
            print("Paper covers rock, YOU WIN!")
        else:
            print ("Scissor cuts paper, YOU LOSE!")
    