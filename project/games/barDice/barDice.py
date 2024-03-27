# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:55:58 2023

@author: Braydon
"""
import simpleGE, random, pygame


class main:
    def __init__():
        pass
    
    def main():
        game = Game()
        game.start()

class Die(simpleGE.SuperSprite):
    def __init__(self,scene):
        super().__init__(scene)
        
        self.setImage("Dice1.png")
        self.setSize(75,75)
        
        self.images = [None,
                       pygame.image.load("Dice1.png"),
                       pygame.image.load("Dice2.png"),
                       pygame.image.load("Dice3.png"),
                       pygame.image.load("Dice4.png"),
                       pygame.image.load("Dice5.png"),
                       pygame.image.load("Dice6.png"),]
        for i in range(1,7):
            self.images[i] = pygame.transform.scale(self.images[i], (75,75))
        self.hide()
    
    def roll(self):
        self.value = random.randint(1,6)
        self.imageMaster = self.images[self.value]

    def reset(self):
        self.setImage("Dice1.png")
        self.setSize(75,75)
        
    def checkEvents(self):
        if self.scene.aceExist:
            if self.mouseDown():
                self.roll()
        
        
class BtnRollAll(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = (240,300)
        self.text = "Roll All"
        self.hide()
class LblNumRolls(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (100,50)
        self.text = "Rolls Left: 3"
        self.hide()
    def reset(self):
        self.text = "Rolls Left: 3"
class BtnNextPlayer(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Next Player"
        self.hide()
class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.center = (550, 50)
        self.text = "Score: 0"
        self.hide()
    def reset(self):
        self.text = "Score: 0"
class BtnStop(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.center = (400,300)
        self.text ="STOP"
        self.hide()
class LblResults(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "You got 100 points"
        self.size=(300,30)
        self.hide()
class BtnPlayAgain(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Play"
        self.center = (240,300)
class BtnQuit(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Quit"
        self.center = (400,300)
class BtnTwoPlayer(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Two"
        self.size = (100,30)
        self.hide()
class BtnThreePlayer(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Three"
        self.size = (100,30)

        self.hide()
class BtnFourPlayer(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Four"
        self.size = (100,30)

        self.hide()
class BtnFivePlayer(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Five"
        self.size = (100,30)

        self.hide()
class BtnSixPlayer(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Six"
        self.size = (100,30)

        self.hide()
class BtnAddOne(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Select"
        self.size = (100,30)
        self.hide()

class BtnAddTwo(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Select"
        self.size = (100,30)
        self.hide()

class BtnAddThree(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Select"
        self.size = (100,30)
        self.hide()

class BtnAddFour(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Select"
        self.size = (100,30)
        self.hide()

class BtnAddFive(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Select"
        self.size = (100,30)
        self.hide()
class BtnTakeOne(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Deselect"
        self.size = (100,30)
        self.hide()
class BtnTakeTwo(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Deselect"
        self.size = (100,30)
        self.hide()
class BtnTakeThree(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Deselect"
        self.size = (100,30)
        self.hide()
class BtnTakeFour(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Deselect"
        self.size = (100,30)
        self.hide()
class BtnTakeFive(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Deselect"
        self.size = (100,30)
        self.hide()
class LblIntro(simpleGE.MultiLabel):
    def __init__(self):
        super().__init__()
        self.textLines = ["Hello, welcome to Bar Dice. ",
                          "The rules are simple: try to get the most points possible. ",
                          "Your points are calculated by taking",
                          "the highest number of dice of the same number,",
                          "multiplying that number by 10, and adding the repeated number,",
                          "so if you roll three fours, your score is 34."]
        self.size = (640,300)
        self.center= (320,100)
class LblPlayers(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Select the number of players"
        self.size = (300,25)
        self.hide()
class LblEndResult(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "The highest score was 0"
        self.size=(300,30)
        self.hide()
class BtnRoll(simpleGE.Button):
    def __init__(self):
        super().__init__()
        self.text = "Roll"
        self.hide()
class Game (simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("pub_bg.png")
        self.background = pygame.transform.scale(self.background, (640,480))
        pygame.mixer.music.load("Flagonlord.wav")
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)
        self.rolls = 3
        self.numPlayers = 2
        self.score = 0
        self.highscore = 0
        self.oneCount = 0
        self.twoCount = 0
        self.threeCount = 0
        self.fourCount = 0
        self.fiveCount = 0
        self.sixCount = 0
        self.aceExist = False
        self.selected = []
        self.dice = []
        for i in range(5):
            newDice = Die(self)
            newDice.setPosition((80 + (i*120),150))
            self.dice.append(newDice)
        for i in range(len(self.dice)):
            self.dice[i].hide()
        self.lblScore = LblScore()
        self.btnRollAll = BtnRollAll()
        self.lblNumRolls = LblNumRolls()
        self.btnNextPlayer = BtnNextPlayer()
        self.lblResults = LblResults()
        self.btnStop = BtnStop()
        self.btnQuit =BtnQuit()
        self.btnPlayAgain = BtnPlayAgain()
        self.btnTwoPlayer = BtnTwoPlayer()
        self.btnThreePlayer = BtnThreePlayer()
        self.btnFourPlayer = BtnFourPlayer()
        self.btnFivePlayer = BtnFivePlayer()
        self.btnSixPlayer = BtnSixPlayer()
        self.lblIntro = LblIntro()
        self.lblPlayers = LblPlayers()
        self.lblEndResult = LblEndResult()
        self.btnAddOne = BtnAddOne()
        self.btnAddTwo = BtnAddTwo()
        self.btnAddThree = BtnAddThree()
        self.btnAddFour = BtnAddFour()
        self.btnAddFive = BtnAddFive()
        self.btnTakeOne = BtnTakeOne()
        self.btnTakeTwo = BtnTakeTwo()
        self.btnTakeThree = BtnTakeThree()
        self.btnTakeFour = BtnTakeFour()
        self.btnTakeFive = BtnTakeFive()
        self.btnRoll = BtnRoll()
        self.sprites = [self.lblIntro,self.lblEndResult,self.lblPlayers,self.btnTwoPlayer, self.btnThreePlayer, 
                        self.btnFourPlayer, self.btnFivePlayer, self.btnSixPlayer,self.dice, 
                        self.btnRollAll,self.btnPlayAgain,self.btnQuit, self.lblResults, 
                        self.btnStop, self.lblNumRolls, self.btnNextPlayer, self.lblScore,
                        self.btnAddFive,self.btnAddFour,self.btnAddThree,self.btnAddTwo,self.btnAddOne,
                        self.btnRoll, self.btnTakeFive, self.btnTakeFour, self.btnTakeThree, self.btnTakeTwo, self.btnTakeOne]
    def nextPlayer(self):
        for i in range(len(self.dice)):
            self.dice[i].hide()
        self.btnRollAll.hide()
        self.lblNumRolls.hide()
        self.btnStop.hide()
        self.lblScore.hide()
        self.btnRoll.hide()
        self.btnAddFive.hide()
        self.btnAddFour.hide()
        self.btnAddThree.hide()
        self.btnAddTwo.hide()
        self.btnAddOne.hide()
        self.lblResults.text = f"You got {self.score} points"

        self.btnNextPlayer.show((320,300))
        self.lblResults.show((320,200))
    def resetGame(self):
        self.btnNextPlayer.hide()
        self.score = 0
        self.oneCount = 0
        self.twoCount = 0
        self.threeCount = 0
        self.fourCount = 0
        self.fiveCount = 0
        self.sixCount = 0
        self.rolls = 3
        self.lblIntro.hide()
        self.btnRollAll.show((240,300))
        self.lblNumRolls.reset()
        self.lblNumRolls.show((100,50))
        self.lblScore.show((550, 50))
        self.lblScore.reset()
        self.btnStop.show((400,300))
        self.btnAddOne.show((75,220))
        self.btnAddTwo.show((200,220))
        self.btnAddThree.show((325,220))
        self.btnAddFour.show((450,220))
        self.btnAddFive.show((575,220))
        self.lblResults.hide()
        self.lblEndResult.hide()
        self.btnPlayAgain.hide()
        self.btnQuit.hide()
        self.btnTwoPlayer.hide()
        self.btnThreePlayer.hide()
        self.btnFourPlayer.hide()
        self.btnFivePlayer.hide()
        self.btnSixPlayer.hide()
        self.lblPlayers.hide()
        for i in range(len(self.dice)):
            self.dice[i].reset()
            self.dice[i].show()
            self.dice[i].setPosition((80 + (i*120),150))
    def playerSelect(self):
        self.btnTwoPlayer.show((75,300))
        self.btnThreePlayer.show((200,300))
        self.btnFourPlayer.show((325,300))
        self.btnFivePlayer.show((450,300))
        self.btnSixPlayer.show((575,300))
        self.lblPlayers.show((320,100))
        self.lblEndResult.hide()
        self.lblIntro.hide()
        self.btnPlayAgain.hide()
        self.btnQuit.hide()
    
    def switchImage(self):
        for i in range(len(self.selected)):
            if self.selected[i].value == 1:
                self.selected[i].setImage("Dice1H.png")
                self.selected[i].setSize(100,100)
                
            if self.selected[i].value == 2:
                self.selected[i].setImage("Dice2H.png")
                self.selected[i].setSize(100,100)

            if self.selected[i].value == 3:
                self.selected[i].setImage("Dice3H.png")
                self.selected[i].setSize(100,100)
                
            if self.selected[i].value == 4:
                self.selected[i].setImage("Dice4H.png")
                self.selected[i].setSize(100,100)
                
            if self.selected[i].value == 5:
                self.selected[i].setImage("Dice5H.png")
                self.selected[i].setSize(100,100)
                
            if self.selected[i].value == 6:
                self.selected[i].setImage("Dice6H.png")
                self.selected[i].setSize(100,100)
    def switchBack(self):
        for i in range(len(self.dice)):
            if self.dice[i].value == 1:
                self.dice[i].setImage("Dice1.png")
                self.dice[i].setSize(75,75)
            elif self.dice[i].value == 2:
                self.dice[i].setImage("Dice2.png")
                self.dice[i].setSize(75,75)

            elif self.dice[i].value == 3:
                self.dice[i].setImage("Dice3.png")
                self.dice[i].setSize(75,75)

            elif self.dice[i].value == 4:
                self.dice[i].setImage("Dice4.png")
                self.dice[i].setSize(75,75)

            elif self.dice[i].value == 5:
                self.dice[i].setImage("Dice5.png")
                self.dice[i].setSize(75,75)

            elif self.dice[i].value == 6:
                self.dice[i].setImage("Dice6.png")
                self.dice[i].setSize(75,75)
   
    def results(self):
        self.btnRollAll.hide()
        self.lblNumRolls.hide()
        self.lblScore.hide()
        self.btnStop.hide()
        self.btnRoll.hide()
        self.btnAddFive.hide()
        self.btnAddFour.hide()
        self.btnAddThree.hide()
        self.btnAddTwo.hide()
        self.btnAddOne.hide()
        self.lblEndResult.text = f"The highest score was {self.highscore}"
        self.btnPlayAgain.text = "Play Again"
        self.btnPlayAgain.show((240,300))
        self.btnQuit.show((400,300))
        self.lblEndResult.show((320,200))
        for i in range(len(self.dice)):
            self.dice[i].hide()
    def selectRoll(self):
        self.btnRollAll.hide()
        self.btnRoll.show((240,300))
        self.switchImage()
    def orginal(self):
        self.btnRollAll.show((240,300))
        self.switchBack()
        self.selected.clear()
        self.btnRoll.hide()
    def scoreUpdate(self):
        if self.twoCount > self.threeCount:
            if self.twoCount > self.fourCount:
                if self.twoCount > self.fiveCount:
                    if self.twoCount > self.sixCount:
                        self.score = 2 + (self.twoCount + self.oneCount) *10
        
        if self.threeCount >= self.twoCount:
            if self.threeCount > self.fourCount:
                if self.threeCount > self.fiveCount:
                    if self.threeCount > self.sixCount:
                        self.score = 3 + (self.threeCount + self.oneCount) *10
        
        if self.fourCount >= self.twoCount:
            if self.fourCount >= self.threeCount:
                    if self.fourCount > self.fiveCount:
                        if self.fourCount > self.sixCount:
                            self.score = 4 + (self.fourCount + self.oneCount) *10
        
        if self.fiveCount >= self.threeCount:
            if self.fiveCount >= self.fourCount:
                if self.fiveCount >= self.twoCount:
                    if self.fiveCount > self.sixCount:
                        self.score = 5 + (self.fiveCount+self.oneCount)*10
        
        if self.sixCount >= self.twoCount:
            if self.sixCount >= self.threeCount:
                if self.sixCount >= self.fourCount:
                    if self.sixCount >= self.fiveCount:
                        self.score = 6 + (self.sixCount+self.oneCount)*10
    def update(self):
        if self.rolls >= 0:
            if self.btnRollAll.clicked:
                self.score = 0
                self.oneCount = 0
                self.twoCount = 0
                self.threeCount = 0
                self.fourCount = 0
                self.fiveCount = 0
                self.sixCount = 0
                if self.rolls > 0:
                    for die in self.dice:
                        die.roll()
                for i in range(len(self.dice)):
                    if self.dice[i].value == 1:
                        self.oneCount += 1
                        self.aceExist = True
                    if self.dice[i].value == 2:
                        self.twoCount += 1
                    if self.dice[i].value == 3:
                        self.threeCount += 1   
                    if self.dice[i].value == 4:
                        self.fourCount += 1   
                    if self.dice[i].value == 5:
                        self.fiveCount += 1
                    if self.dice[i].value == 6:
                        self.sixCount += 1
                
                
                self.scoreUpdate()
                self.lblScore.text = f"Score: {self.score}"
                if self.rolls == 0:
                    if self.score > self.highscore:
                        self.highscore = self.score
                    if self.numPlayers > 1:
                        self.nextPlayer()
                    else:
                        self.results()
                if self.rolls > 0:
                    self.rolls -= 1
                    
                self.lblNumRolls.text = f"Rolls Left: {self.rolls}"
        elif self.numPlayers > 0:
            self.nextPlayer()
        else:
            self.results()
                
        if self.rolls > 0:
            if self.aceExist:
                if self.btnAddOne.clicked:
                    self.selected.append(self.dice[0])
                    self.selectRoll()
                if self.btnAddTwo.clicked:
                    self.selected.append(self.dice[1])
                    self.selectRoll()
                if self.btnAddThree.clicked:
                    self.selected.append(self.dice[2])
                    self.selectRoll()
                if self.btnAddFour.clicked:
                    self.selected.append(self.dice[3])
                    self.selectRoll()
                if self.btnAddFive.clicked:
                    self.selected.append(self.dice[4])
                    self.selectRoll()
        
        if self.btnRoll.clicked:
            self.score = 0
            self.oneCount = 0
            self.twoCount = 0
            self.threeCount = 0
            self.fourCount = 0
            self.fiveCount = 0
            self.sixCount = 0
            for i in range(len(self.selected)):
                self.selected[i].roll()
            for i in range(len(self.dice)):
                if self.dice[i].value == 1:
                    self.oneCount += 1
                    self.aceExist = True
                if self.dice[i].value == 2:
                    self.twoCount += 1
                if self.dice[i].value == 3:
                    self.threeCount += 1   
                if self.dice[i].value == 4:
                    self.fourCount += 1   
                if self.dice[i].value == 5:
                    self.fiveCount += 1
                if self.dice[i].value == 6:
                    self.sixCount += 1
            
            self.scoreUpdate()
            self.lblScore.text = f"Score: {self.score}"
            
            if self.rolls == 0:
                if self.score > self.highscore:
                    self.highscore = self.score
                if self.numPlayers > 1:
                    self.nextPlayer()
                else:
                    self.results()
            if self.rolls > 0:
                self.rolls -= 1
                
            self.lblNumRolls.text = f"Rolls Left: {self.rolls}"
            self.orginal()
        if self.btnStop.clicked:
            if self.score > self.highscore:
                self.highscore = self.score
            if self.numPlayers > 1:
                self.nextPlayer()
            else:
                self.results()
        if self.btnNextPlayer.clicked:
            self.numPlayers -= 1
            self.resetGame()
        if self.btnQuit.clicked:
            self.stop()
        if self.btnPlayAgain.clicked:
            self.playerSelect()
        if self.btnTwoPlayer.clicked:
            self.numPlayers = 2
            self.resetGame()
        if self.btnThreePlayer.clicked:
            self.numPlayers = 3
            self.resetGame()
        if self.btnFourPlayer.clicked:
            self.numPlayers = 4
            self.resetGame()
        if self.btnFivePlayer.clicked:
            self.numPlayers = 5
            self.resetGame()
        if self.btnSixPlayer.clicked:
            self.numPlayers = 6
            self.resetGame()

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
