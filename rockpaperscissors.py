import random
choices =['rock','paper','scissors']
computer=random.choice(choices)
while True :
    player = None
    while player not in choices:
        player = input("Enter rock, paper or scissors : ").lower()
    
    if player == computer :
        print("computer : ",computer)
        print("player : ",player)
        print('Tie!!!')
    elif player == "scissors" :
        if computer == "rock" :
            print("computer : ",computer)
            print("player : ",player)
            print("You lose!!!")
        if computer == "paper" :
            print("computer : ",computer)
            print("player : ",player)
            print("You win!!!")
    elif player == "rock" :
        if computer == "paper" :
            print("computer : ",computer)
            print("player : ",player)
            print("You lose!!!")
        if computer == "scissors" :
            print("computer : ",computer)
            print("player : ",player)
            print("You win!!!")
    elif player == "paper" :
        if computer == "scissors" :
            print("computer : ",computer)
            print("player : ",player)
            print("You lose!!!")
        if computer == "rock" :
            print("computer : ",computer)
            print("player : ",player)
            print("You win!!!")
    play_again = input("Do you want to play again yes or no ? ").lower()
    
    if play_again != "yes" :
        break
print("bye!!! bye!!!")
    