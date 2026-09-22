import constants

BET_NUMBERS = {  # Maps each betType to its winning numbers.
    "Red": constants.RedNumbers,
    "Black": constants.BlackNumbers,
    "High": constants.HighNumbers,
    "Low": constants.LowNumbers,
    "Odd": constants.OddNumbers,
    "Even": constants.EvenNumbers
}
class Player:  # Holds the player state; constructor plus 5 methods. 
    def __init__(self, betType):
        self.betType = betType
        self.notebook = [1, 2, 3, 4]
        self.balance = 0

    def calculate_bet(self):  # Calculates the bet from the notebook (first + last, or the only one left).
        if len(self.notebook) == 1:
            return self.notebook[0]

        return self.notebook[0] + self.notebook[-1]

    def reset_notebook(self):  # Resets the notebook to its initial state.
        self.notebook = [1, 2, 3, 4]

    def refresh_notebook(self, won, bet):  # Updates the notebook according to the outcome (win or loss).
        if won:
            self.notebook.append(bet)
        else:
            self.notebook.pop(0)

            if len(self.notebook) > 0:
                self.notebook.pop()
    def won(self, outcome):
        return outcome in BET_NUMBERS[self.betType]  # Returns True if the outcome is in the betType's winning numbers.

    def updateBalance(self, won, bet):  # Updates the balance according to the outcome (win or loss).
        if won:
            self.balance += bet
        else:
            self.balance -= bet