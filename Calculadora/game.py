import ti_system
import time

def clear():
    ti_system.disp_clr()

class Game :
    def __init__(self, theme : str, word : str):
        self.isRunning = True
        self.theme = theme
        self.word = word
        self.fails = 0
        self.hiddenWord = '_' * len(self.word)

    def start(self):
        self.writeLetters()
        time.sleep(2)
        input('Press enter to play again...')
        clear()
        startNewGame()

    manParts = [' ', 'O', '|', '/', '\\', '/', '\\']
    letterNotInWord = ''

    def writeLetters(self):
        clear()
        print(self.theme)
        print(self.drawHangMan(self.fails))
        print(self.hiddenWord)
        print(self.letterNotInWord)

        if self.winOrLose():
            return

        letter = input('\nType a letter: ')

        '''if len(letter) > 1:
            print('You need to type a single letter')
            time.sleep(1)
            self.writeLetters()
            return'''

        lowerWord = self.word.lower()

        for l in letter:
            for i in range(len(self.word)):
                if lowerWord[i] == l.lower():
                    self.hiddenWord = self.hiddenWord[:i] + self.word[i] + self.hiddenWord[i + 1:]
        if not letter.lower() in lowerWord and not letter.lower() in self.letterNotInWord: 
            self.letterNotInWord += letter.lower() + ', '
            self.fails += 1 
            
        self.writeLetters()

    def winOrLose(self):
        if self.hiddenWord == self.word:
            print('You Won')
            return True
        elif self.fails >= 6:
            print('You suck')
            return True
            

    def drawHangMan(self, fails : int) -> str:
        
        
        hang = '''
          ____ 
          |  |
          |  {head}
          | {leftArm}{torso}{rightArm}
          | {leftLeg} {rightLeg}
        __|_____'''
        
        manParts = self.manParts

        hang = hang.format(
            head = manParts[1 if fails >= 1 else 0], 
            torso = manParts[2 if fails >= 2 else 0], 
            leftArm = manParts[3 if fails >= 3 else 0], 
            rightArm = manParts[4 if fails >= 4 else 0], 
            leftLeg = manParts[5 if fails >= 5 else 0], 
            rightLeg = manParts[6 if fails >= 6 else 0])

        return hang

def startNewGame():
    clear()
    game = Game(input('Theme: '), input('Name: '))
    game.start()

startNewGame()