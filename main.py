from player import Player
from roulette import Roulette

def boundariesCheck(bet):
    if bet > 4000 or bet < 5:
        return True
    else:
        return False 

def main():  # Runs the simulation. 
    # Initialize the players with their bet types.
    playerA = Player("Red") 
    playerB = Player("Black")
    playerC = Player("High")
    playerD = Player("Low")
    playerE = Player("Odd")
    playerF = Player("Even")

    players = [playerA, playerB, playerC, playerD, playerE, playerF]  # Group the players in a list to iterate over them.
    roulette = Roulette()  # Initialize the roulette.

    teamBalance = 0  # Initialize the team balance.
    for _ in range(0,10000):  # Run the simulation loop and update each player. 
        outcome = roulette.spinRoulette()
        for player in players:
            if (len(player.notebook)== 0):
                player.reset_notebook()
            bet = player.calculate_bet()
            if boundariesCheck(bet):
                player.reset_notebook()
                bet = player.calculate_bet()  # Recomputed after reset (5 with the initial notebook [1, 2, 3, 4]).
            wonResult = player.won(outcome)
            player.refresh_notebook(wonResult, bet)
            player.updateBalance(wonResult, bet)

    teamBalance = sum(player.balance for player in players)

    print("Team balance:", teamBalance)

    if teamBalance > 0:
        print("The team won.")
    elif teamBalance < 0:
        print("The team lost.")
    else:
        print("The team broke even.")

if __name__ == "__main__": 
    main()