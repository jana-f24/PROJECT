
import random


class NumbersGame:

    def __init__(self , lower, higher):
        
        self.LOWER = lower
        self.HIGHER = higher

    
    def pick_a_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    
    def start(self):
        
        random_number = self.pick_a_random_number()

        print(f"Guess the randomly picked number from {self.LOWER} to {self.HIGHER}")

        
        chances = 0
        while True:
            chosen_number = int(input("Enter your guessed number: "))
            if chosen_number == random_number:
                print(f"amazing! You got it in {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif chosen_number < random_number:
                print(" Your number is less than the number")
            else:
                print(" Your number is greater than the number")
            chances += 1
        





game1 = NumbersGame(1, 10)
game2 = NumbersGame(1, 50)
game3 = NumbersGame(1, 100)

choose_level = int (input("******welcome to the game******\n 1. level(1)\n 2. level(2)\n 3. level(3)\n choose a level :"))

if choose_level == 1:
    game1.start()
elif choose_level == 2:
    game2.start()
else:
    game3.start()


