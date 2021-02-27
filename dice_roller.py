def main():
    players = int(input("How many players are rolling the dice?"))
    dice_rolls = int(input('How many dice would you like to roll?'))
    dice_size = int(input('How many sides are the dice?'))
    dice_sum = 0
    
    total = 0
    vencedor = [0]
    for x in range(0, players):
        player = x + 1
        for i in range(0, dice_rolls):
            roll = random.randint(1, dice_size)
            dice_sum = dice_sum + roll
            if roll == 1:
        	    print(f'Player {player} rolled a {roll}! Critical Fail!')
            elif roll == dice_size:
                print(f'Player {player} rolled a {roll}! Critical Success!')
            else:
                print(f'Player {player} rolled a {roll}')
        print(f'Player {player} has rolled a total of {dice_sum}')
        if total < dice_sum:
            total = dice_sum
            
            vencedor[0] = player
            dice_sum = 0
        elif total == dice_sum:
            vencedor.append(player)
        dice_sum = 0
    if len(vencedor) == 1:
        print(f'Player {vencedor[0]} is the winner')
    else:
         print("The winners are", end=" ")
         for i in range(len(vencedor)):
            if vencedor[i] != vencedor[-1]:
                print(f"Player {vencedor[i]},", end=" ")
            else:
                print("Player", vencedor[i])


if __name__== "__main__":
    main()
