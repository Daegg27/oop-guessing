import random
class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.correct = False
        print(answer)

    def guess(self, user_guess):
        if user_guess > self.answer:
            print('high')
        elif user_guess < self.answer:
            print('low')
        else: 
            user_guess == self.answer
            print('correct')
            self.correct = True
    def solved(self):
        print(self.correct)

x = GuessingGame(random.randrange(10))
x.guess(6)
x.solved()