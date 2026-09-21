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

    def calculate_bet(self):

        if len(self.notebook) == 0:
            self.notebook = [1, 2, 3, 4]

        if len(self.notebook) == 1:
            bet = self.notebook[0]
        else:
            bet = self.notebook[0] + self.notebook[-1]

        if bet < 5 or bet > 4000:
            self.notebook = [1, 2, 3, 4]
            bet = 5

        return bet

    def won(self, outcome):
        return outcome in BET_NUMBERS[self.betType]

    def refreshNotebook(self, won, bet):

        if won:
            self.notebook.append(bet)

        else:
            self.notebook.pop(0)

            if len(self.notebook) > 0:
                self.notebook.pop()


class Roulette:

    def spinRoulette(self):
        return random.randint(0, 36)


playerA = Player("Red")
playerB = Player("Black")
playerC = Player("High")
playerD = Player("Low")
playerE = Player("Odd")
playerF = Player("Even")

for _ in range(0,10000):
    print("Aura")