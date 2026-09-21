from player import Player
from roulette import Roulette

def boundariesCheck(bet):
    if bet > 4000 or bet < 5:
        return True
    else:
        return False 

def main():
    playerA = Player("Red")
    playerB = Player("Black")
    playerC = Player("High")
    playerD = Player("Low")
    playerE = Player("Odd")
    playerF = Player("Even")

    players = [playerA, playerB, playerC, playerD, playerE, playerF] # I put the players in a list to iterate over them.
    roulette = Roulette() # Initialize the roulette.

    teamBalance = 0
    for _ in range(0,10000):
        outcome = roulette.spinRoulette()
        for player in players:
            if (len(player.notebook)== 0):
                player.reset_notebook()
            bet = player.calculate_bet()
            if boundariesCheck(bet):
                player.reset_notebook()
                bet = player.calculate_bet() # bet = 5.
            wonResult = player.won(outcome)
            player.refresh_notebook(wonResult, bet)
            player.updateBalance(wonResult, bet)

    teamBalance = sum(player.balance for player in players)

    print("Team balance:", teamBalance)

    if teamBalance > 0:
        print("The team won.")
    else: 
        print("The team lost.")


if __name__ == "__main__":
    main()