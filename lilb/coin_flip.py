import random

class CoinFlip:
    def __init__(self):
        self.heads = 0
        self.tails = 0

    def flip(self):
        return random.choice(['heads', 'tails'])

    def flip_n_times(self, n):
        for i in range(n):
            result = self.flip()
            if result == 'heads':
                self.heads += 1
            else:
                self.tails += 1

    def get_results(self):
        return self.heads, self.tails