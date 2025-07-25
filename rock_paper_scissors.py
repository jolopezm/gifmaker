import random

keep_playing = True

rules = """
- ✊ beats ✌️  and 🦎.
- ✋ beats ✊ and 🖖.
- ✌️  beats ✋ beats 🦎.
- 🦎 beats ✋ beats 🖖.
- 🖖 beats ✌️  beats ✊.
"""
            

while keep_playing:
    print("==================="
        "\nRock Paper Scissors, Lizard, Spock"
        "\n==================="

        "\n1) ✊"
        "\n2) ✋"
        "\n3) ✌️"
        "\n4) 🦎"
        "\n5) 🖖"
        "\n6) Read rules"
        "\n7) Exit")
    
    player = int(input("\nPick a number: "))
    
    computer = random.randint(1, 4) 
    
    if player > 0 and player < 7:
        if player == 6:
            print(rules)
            
        else:
            print(f"\nYou chose: {player}"
                  f"\nComputer chose: {computer}"
                   "\n")
            
            if player == computer:
                print("It's a tie!")
            else: 
                if (player == 1 and (computer == 3 or computer == 4)) or \
                (player == 2 and (computer == 1 or computer == 5)) or \
                (player == 3 and (computer == 2 or computer == 4)) or \
                (player == 4 and (computer == 2 or computer == 5)) or \
                (player == 5 and (computer == 1 or computer == 3)):
                    print("You win!")
                else:
                    print("You lose!")
    elif player == 7:
        print("Thanks for playing!")
        keep_playing = False
    else:
        print("Invalid choice, please try agai.")