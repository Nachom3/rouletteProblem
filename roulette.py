import random
import constants

BET_NUMBERS = {
    "Red": constants.RedNumbers,
    "Black": constants.BlackNumbers,
    "High": constants.HighNumbers,
    "Low": constants.LowNumbers,
    "Odd": constants.OddNumbers,
    "Even": constants.EvenNumbers
}
class Player:

    def __init__(self, betType):
        self.betType = betType
        self.notebook = [1, 2, 3, 4]
        self.balance = 0

    def calculate_bet(self): # Calculates the bet acording the noteboook.
        if len(self.notebook) == 1:
            return self.notebook[0]

        return self.notebook[0] + self.notebook[-1]

    def reset_notebook(self): # It resets the notebook to the initial state.
        self.notebook = [1, 2, 3, 4]

    def refresh_notebook(self, won, bet): # It refresh the notebook acording the outcome(win, lose)
        if won:
            self.notebook.append(bet)
        else:
            self.notebook.pop(0)

            if len(self.notebook) > 0:
                self.notebook.pop()
    def won(self, outcome):
        return outcome in BET_NUMBERS[self.betType] # It retuns True if outcome is inside the betType numbers.

    def updateBalance(self, won, bet):
        if won:
            self.balance += bet
        else:
            self.balance -= bet

class Roulette:
    def spinRoulette(self):
        return random.randint(0, 36)

def boundariesCheck(bet):
    if bet > 4000 or bet < 5:
        return True
    else:
        return False 

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
