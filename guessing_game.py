import random
class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.correct = False
        

    def guess(self, user_guess):
        if user_guess > self.answer:
            print("high")
        elif user_guess < self.answer:
            print("low")
        else: 
            user_guess == self.answer
            print('Perfect')
            self.correct = True
        
    def solved(self):
        print(self.correct)

x = GuessingGame(5)
x.guess(2)

