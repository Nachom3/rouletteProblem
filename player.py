import constants

BET_NUMBERS = { # We create a dictonary so we map each betType to its winning numbers.
    "Red": constants.RedNumbers,
    "Black": constants.BlackNumbers,
    "High": constants.HighNumbers,
    "Low": constants.LowNumbers,
    "Odd": constants.OddNumbers,
    "Even": constants.EvenNumbers
}
class Player: # It cointains 5 methods. 
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

    def updateBalance(self, won, bet): # It updates the balance acording the outcome(win or lose)
        if won:
            self.balance += bet
        else:
            self.balance -= bet