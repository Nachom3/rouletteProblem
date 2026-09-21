import random
class Roulette:
    def spinRoulette(self):
        return random.randint(0, 36)

def boundariesCheck(bet):
    if bet > 4000 or bet < 5:
        return True
    else:
        return False 
