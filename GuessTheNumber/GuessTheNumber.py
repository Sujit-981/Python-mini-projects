import random 


class Player:
    
    def __init__(self, rangeOfNumbers):
        self.rangeOfNumbers = rangeOfNumbers
        self.computerChoice = random.randint(1, rangeOfNumbers)
        print('Guess the number that computer has secretly choosen.')
        print('----------------')
        
    def guessTheNumber(self):
        userGuess = 0
        count = 0
        while userGuess != self.computerChoice:
            userGuess = int(input(f'Guess a number between 1 and {self.rangeOfNumbers}: '))
            if userGuess < self.computerChoice:
                print("Sorry, guess again. Too low.")
            elif userGuess > self.computerChoice:
                print("Sorry, guess again. Too high.")
            count+=1
        
        print(f'Congrats, You have guessed the correct number {self.computerChoice} in {count} tries.')

class Computer:
    def __init__(self, rangeOfNumbers):
        self.rangeOfNumbers = rangeOfNumbers
        print('Secretly select a number between your range and let the computer guess it.')
        print('----------------')
        
        
    def guessTheNumber(self):
        low = 1
        high = self.rangeOfNumbers
        feedback = ''
        count = 0
        while feedback != 'c':
            if low != high:
                computerGuess = random.randint(low, high)
            else:
                computerGuess = low
            feedback = input(f'Is {computerGuess} too high (H), too low (L), or Correct (C): ').lower()
            if feedback == 'h':
                high = computerGuess-1
            elif feedback == 'l':
                low = computerGuess+1
            count+=1
            
        print(f'Computer guessed your number {computerGuess} correctly in {count} tries.')
        

if __name__ == "__main__":
    print("Welcome to the game Guess the Number")
    print("____________________________________")
    while True:
        gameChoice = input("If you want to guess the number press (Y) and enter, if you want computer to guess the number press(N) and enter: ")
    
        if gameChoice == "Y":
            player = Player(int(input(f'Lower range being 1, what would you like your upper range be: ')))
            player.guessTheNumber()
            
        else:
            computer = Computer(int(input(f'Lower range being 1, what would you like your upper range be: ')))
            computer.guessTheNumber()
    
        nextMatch = input("Would you like to play again? (Y) or (N): ")
        if nextMatch == "Y":
            continue 
        else:
            break