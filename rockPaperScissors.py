from random import randint

options = ["Rock", "Paper", "Scissors"]

play_again = True

while  play_again:
    cpu = options[randint(0,2)]
    player = False

    while not player:
        print("Rock, Paper, or Scissors")
        player = input("You choose: ").capitalize()    
        if player == "R":
            player = "Rock"
        elif player == "P":
            player ="Paper"
        elif player == "S":
            player = "Scissors"
        if player == cpu:
            print("Tie!")
        elif player == "Rock" or player =="R":
            if cpu == "Paper":
                print("You lose!", cpu, "covers", player)
            else:
                print("You win!", player, "smashes", cpu)
        elif player == "Paper" or player == "P":
            if cpu == "Scissors":
                print("You lose!", cpu, "cut", player)
            else:
                print("You win!", player, "covers", cpu)
        elif player == "Scissors" or  player == "S":
            if cpu == "Rock":
                print("You lose!", cpu, "smashes", player)
            else:
                print("You win!", player, "cut", cpu)
        else:
            print("Play was not recognized, Check your spelling")
        print("Would you like to play again? Y or N")
        play_again = input("Play again? ").casefold() in ("y", "yes")
        if play_again:
            player =False
print("Thanks for playing!")