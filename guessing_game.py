import random
class GuessingGame:
    def __init__(self, answer):
        self.answer = answer
        self.correct = False
        

    def guess(self, user_guess):
        if user_guess > self.answer:
            print("High")
            self.solved()
        elif user_guess < self.answer:
            print("Low")
            self.solved()
        else: 
            user_guess == self.answer
            print('Correct')
            self.correct = True
            self.solved()
        
    def solved(self):
        print(self.correct)
    

first_game = GuessingGame(5)
first_game.guess(4)

