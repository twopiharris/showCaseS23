# -*- coding: utf-8 -*-
"""
Music Puzzle Game

Alexander Murray

background https://creator.nightcafe.studio/studio?open=creation&panelContext=%28jobId%3A3obwZPuQlAGD4ZVIlkUS%29
button sounds https://freesound.org/search/?f=grouping_pack:%2217749_Do%2C%20re%2C%20mi%2C%20fa%2C%20so%2C%20la%2C%20ti%2C%20do%22&s=Date+added+(newest+first)&g=1
piano https://opengameart.org/content/simple-piano
lights https://opengameart.org/content/simple-colored-particle-lights
Simon buttons https://opengameart.org/content/magic-buttons
sad loop https://opengameart.org/content/emotional-piano-loop
Fugue in B minor https://opengameart.org/content/fugue-in-b-minor
organ notes for button keys A-G recorded by myself through BandLab
"""

import pygame, simpleGE, random, time

class main:
    def __init__():
        pass
    
    def main():
        game = Game()
        game.start()

class Game(simpleGE.Scene):
    solutionGuide = [""]
    solutionKey = ""
    simonKey = ""
    simonNum = 1
    currentScore = 0
    highscore = "0"
    highscoreInt = 0
   
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.background = pygame.image.load("organ1.jpg")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Music Puzzle")
        self.inputlen = 0
        
        self.addLabels()
        self.addButton()
        self.addMultiLabel()
        
        self.greenBtn = SimonButtons(self)
        self.greenBtn.setImage("Magic_button_green.png")
        self.greenBtn.setSize(90, 90)
        self.greenBtn.setPosition((150, 240))
        
        self.greenLight = SimonButtons(self)
        self.greenLight.setImage("greenlight.png")
        self.greenLight.setSize(110, 110)
        self.greenLight.setPosition((150, 240))
        
        self.yellowBtn = SimonButtons(self)
        self.yellowBtn.setImage("Magic_button_yellow.png")
        self.yellowBtn.setSize(90, 90)
        self.yellowBtn.setPosition((250, 240))
        
        self.yellowLight = SimonButtons(self)
        self.yellowLight.setImage("yellowlight.png")
        self.yellowLight.setSize(110, 110)
        self.yellowLight.setPosition((250, 240))
        
        self.blueBtn = SimonButtons(self)
        self.blueBtn.setImage("Magic_button_blue.png")
        self.blueBtn.setSize(90, 90)
        self.blueBtn.setPosition((350, 240))
        
        self.blueLight = SimonButtons(self)
        self.blueLight.setImage("bluelight.png")
        self.blueLight.setSize(110, 110)
        self.blueLight.setPosition((350, 240))
        
        self.redBtn = SimonButtons(self)
        self.redBtn.setImage("Magic_button_red.png")
        self.redBtn.setSize(90, 90)
        self.redBtn.setPosition((450, 240))
        
        self.redLight = SimonButtons(self)
        self.redLight.setImage("redlight.png")
        self.redLight.setSize(110, 110)
        self.redLight.setPosition((450, 240))
        
        self.piano = PianoKeys(self)
        
        self.sprites = [self.btnPuzzle, self.btnSimon, self.lblTitleSimon, self.multiSimon, self.lblTitle, self.multi, self.btnStart, self.btnStartSimon, self.lblInputSimon, self.lblCurrentScore, self.btnKeyA, self.btnKeyB, self.btnKeyC, self.btnKeyD, self.btnKeyE, self.btnKeyF, self.btnKeyG, self.piano,  self.btnSimonTrial, self.btnGreen, self.btnRed, self.btnYellow, self.btnBlue, self.lblInput, self.lblHint, self.btnCheck, self.btnSimonSolve, self.lblHighscore, self.btnClear, self.btnClue, self.multiClue, self.btnClueHide, self.greenBtn, self.yellowBtn, self.blueBtn, self.redBtn, self.greenLight, self.yellowLight, self.blueLight, self.redLight, self.lblAttempts, self.btnReset, self.btnQuit]
        self.lblTitle.hide()
        self.btnStart.hide()
        self.multi.hide()
        self.lblInput.hide()
        self.btnKeyA.hide()
        self.btnKeyB.hide()
        self.btnKeyC.hide()
        self.btnKeyD.hide()
        self.btnKeyE.hide()
        self.btnKeyF.hide()
        self.btnKeyG.hide()
        self.btnQuit.hide()
        self.btnCheck.hide()
        self.btnClear.hide()
        self.lblHint.hide()
        self.lblAttempts.hide()
        self.btnClue.hide()
        self.multiClue.hide()
        self.btnClueHide.hide()
        self.btnReset.hide()
        self.btnStartSimon.hide()
        self.btnSimonSolve.hide()
        self.lblTitleSimon.hide()
        self.multiSimon.hide()
        self.btnGreen.hide()
        self.btnYellow.hide()
        self.btnBlue.hide()
        self.btnRed.hide()
        self.lblInputSimon.hide()
        self.lblHighscore.hide()
        self.lblCurrentScore.hide()
        self.btnSimonTrial.hide()
        self.greenBtn.hide()
        self.yellowBtn.hide()
        self.blueBtn.hide()
        self.redBtn.hide()
        self.greenLight.hide()
        self.yellowLight.hide()
        self.blueLight.hide()
        self.redLight.hide()
        self.piano.hide()
        
    
        
    def addLabels(self):
        self.lblTitle = simpleGE.Label()
        self.lblTitle.text = "Music Puzzle"
        self.lblTitle.center = (320,40)
        self.lblTitle.size = (300, 30)
        
        self.lblTitleSimon = simpleGE.Label()
        self.lblTitleSimon.text = "Simon Says"
        self.lblTitleSimon.size = (300, 30)
        self.lblTitleSimon.center = (320, 40)
        
        self.lblInput = simpleGE.Label()
        self.lblInput.text = ""
        self.lblInput.center = (320,40)
        self.lblInput.size = (150,30)
        
        self.lblInputSimon = simpleGE.Label()
        self.lblInputSimon.text = ""
        self.lblInputSimon.size = (550, 30)
        self.lblInputSimon.center = (320, 100)
        
        self.lblHint = simpleGE.Label()
        self.lblHint.text = ""
        self.lblHint.center = (320, 130)
        self.lblHint.size = (350, 30)
        
        self.lblAttempts = simpleGE.Label()
        self.lblAttempts.center = (500, 80)
        self.lblAttempts.size = (150, 30)
        
        self.lblCurrentScore = simpleGE.Label()
        self.lblCurrentScore.text = "Score: " + str(self.currentScore)
        self.lblCurrentScore.center = (500, 80)
        self.lblCurrentScore.size = (150, 30)
        
        self.lblHighscore = simpleGE.Label()
        self.lblHighscore.center = (100, 80)
        self.lblHighscore.size = (150, 30)
    
        
    def addButton(self):
        self.btnStart = simpleGE.Button()
        self.btnStart.text = "Start Game"
        self.btnStart.center = (320, 440)
        
        self.btnStartSimon = simpleGE.Button()
        self.btnStartSimon.text = "Start Game"
        self.btnStartSimon.center = (320,440)
        
        self.btnPuzzle = simpleGE.Button()
        self.btnPuzzle.text = "Puzzle Game"
        self.btnPuzzle.center = (320, 220)
        
        self.btnSimon = simpleGE.Button()
        self.btnSimon.text = "Simon Says"
        self.btnSimon.center = (320, 320)
        
        self.btnSimonSolve = simpleGE.Button()
        self.btnSimonSolve.text = "Solve"
        self.btnSimonSolve.center = (500, 30)
        
        self.btnSimonTrial = simpleGE.Button()
        self.btnSimonTrial.text = "Start Trial"
        self.btnSimonTrial.center = (320, 440)

        self.btnReset = simpleGE.Button()
        self.btnReset.text = "New Game"
        self.btnReset.center = (320, 440)
        
        self.btnClue = simpleGE.Button()
        self.btnClue.text = "Clue"
        self.btnClue.center = (100, 440)
        
        self.btnClueHide = simpleGE.Button()
        self.btnClueHide.text = "Hide Clue"
        self.btnClue.center = (100, 440)
        
        self.btnClear = simpleGE.Button()
        self.btnClear.text = "Clear"
        self.btnClear.center = (100,30)

        self.btnCheck = simpleGE.Button()
        self.btnCheck.text = "Solve"
        self.btnCheck.center = (500,30)
        
        self.btnKeyA = simpleGE.Button()
        self.btnKeyA.text = "A"
        self.btnKeyASound = simpleGE.Sound("OrganA.wav")
        self.btnKeyA.center = (100, 240)
        self.btnKeyA.size = (30, 160)
        
        self.btnKeyB = simpleGE.Button()
        self.btnKeyB.text = "B"
        self.btnKeyBSound = simpleGE.Sound("OrganB.wav")
        self.btnKeyB.center = (175, 240)
        self.btnKeyB.size = (30, 160)
        
        self.btnKeyC = simpleGE.Button()
        self.btnKeyC.text = "C"
        self.btnKeyCSound = simpleGE.Sound("OrganC.wav")
        self.btnKeyC.center = (250, 240)
        self.btnKeyC.size = (30, 160)
        
        self.btnKeyD = simpleGE.Button()
        self.btnKeyD.text = "D"
        self.btnKeyDSound = simpleGE.Sound("OrganD.wav")
        self.btnKeyD.center = (325, 240)
        self.btnKeyD.size = (30, 160)
        
        self.btnKeyE = simpleGE.Button()
        self.btnKeyE.text = "E"
        self.btnKeyESound = simpleGE.Sound("OrganE.wav")
        self.btnKeyE.center = (400, 240)
        self.btnKeyE.size = (30, 160)
        
        self.btnKeyF = simpleGE.Button()
        self.btnKeyF.text = "F"
        self.btnKeyFSound = simpleGE.Sound("OrganF.wav")
        self.btnKeyF.center = (475, 240)
        self.btnKeyF.size = (30, 160)
        
        self.btnKeyG = simpleGE.Button()
        self.btnKeyG.text = "G"
        self.btnKeyGSound = simpleGE.Sound("OrganG.wav")
        self.btnKeyG.center = (550, 240)
        self.btnKeyG.size = (30, 160)
        
        self.btnGreen = simpleGE.Button()
        self.btnGreen.text = "Green"
        self.btnGreenSound = simpleGE.Sound("si.wav")
        self.btnGreen.size = (60, 40)
        self.btnGreen.center = (150 ,240)
        
        self.btnYellow = simpleGE.Button()
        self.btnYellow.text = "Yellow"
        self.btnYellowSound = simpleGE.Sound("re.wav")
        self.btnYellow.size = (60, 40)
        self.btnYellow.center = (250, 240)
        
        self.btnBlue = simpleGE.Button()
        self.btnBlue.text = "Blue"
        self.btnBlueSound = simpleGE.Sound("fa.wav")
        self.btnBlue.size = (60, 40)
        self.btnBlue.center = (350, 240)
        
        self.btnRed = simpleGE.Button()
        self.btnRed.text = "Red"
        self.btnRedSound = simpleGE.Sound("do.wav")
        self.btnRed.size = (60, 40)
        self.btnRed.center = (450, 240)
        
        
        #self.btnKeys.itemSound = simpleGE.Sound("")
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit Game"
        self.btnQuit.center = (320, 420)
        
        
        
    def addMultiLabel(self):
        self.multi = simpleGE.MultiLabel()
        self.multi.textLines = [
            "Solve the music riddle",
            "Play the notes to add it to your answer",
            "Press the check button to compare it to the solution"
            ]
        self.multi.center = (325,245)
        self.multi.size = (550,300)
        
        self.multiSimon = simpleGE.MultiLabel()
        self.multiSimon.textLines = [
            "This is Simon Says",
            "Simon will play notes",
            "Match the notes",
            "See how long you can last"
            ]
        self.multiSimon.size = (550, 300)
        self.multiSimon.center = (325, 245)
        
        self.multiClue = simpleGE.MultiLabel()
        self.multiClue.center = (325, 245)
        self.multiClue.size = (550, 300)
        
    
    def createKey(self):
        keyList = ["A", "B", "C", "D", "E", "F", "G"]
        solution1 = random.sample(keyList, 4) 
        self.solutionKey = (f"{solution1[0]}{solution1[1]}{solution1[2]}{solution1[3]}")
        for i in range(len(solution1)):
            if solution1[i] == "A":
                solution1[i] = "Alex"
            if solution1[i] == "B":
                solution1[i] = "Beth"
            if solution1[i] == "C":
                solution1[i] = "Charlie"
            if solution1[i] == "D":
                solution1[i] = "Daniel"
            if solution1[i] == "E":
                solution1[i] = "Elaine"
            if solution1[i] == "F":
                solution1[i] = "Fred"
            if solution1[i] == "G":
                solution1[i] = "Gemma"
        print(solution1)
        print(self.solutionKey)
        self.solutionGuide = [
            f"{solution1[1]} is not in last place.",
            f"{solution1[2]} is beating {solution1[3]}",
            f"{solution1[2]} is losing to {solution1[0]}.",
            f"{solution1[0]} is beating {solution1[1]}.",
            f"{solution1[3]} is not winning."
            ]
        self.solutionGuide = random.sample(self.solutionGuide, 5)
        print(self.solutionGuide)
        
        
    def createSimon(self):
        simonList = ["G", "Y", "B", "R"]
        solution2 = random.choices(simonList, k = self.simonNum)
        for x in range(len(solution2)):
            time.sleep(.75)
            if solution2[x] == "G":
                self.btnGreenSound.play()
                #self.greenLight.show()
                #self.greenLight.update()
                #time.sleep(2)
                #self.greenLight.hide()
            if solution2[x] == "Y":
                self.btnYellowSound.play()
                #self.yellowLight.show()
                #time.sleep(2)
                #self.yellowLight.hide()
            if solution2[x] == "B":
                self.btnBlueSound.play()
                #self.blueLight.show()
                #time.sleep(2)
                #self.blueLight.hide()
            if solution2[x] == "R":
                self.btnRedSound.play()
                #self.redLight.show()
                #time.sleep(2)
                #self.redLight.hide()
        self.simonKey = "".join(solution2)
        print(self.simonKey)
        
        
    def getHighScore(self):
        score = open("simonHS.txt", "r")
        self.highscore = score.read()
        if self.highscore == "":
            self.highscore = "0"
        self.highscoreInt = int(self.highscore)
        score.close()
        
    def saveHighScore(self):
        score = open("simonHS.txt", "w")
        if self.currentScore > self.highscoreInt:
            score.write(str(self.currentScore))
        score.close()
        
    

        
        
        
    def update(self):
        if self.btnPuzzle.clicked:
            self.lblTitle.show((320, 40))
            self.btnStart.show((320, 440))
            self.multi.show((325,245))
            self.btnPuzzle.hide()
            self.btnSimon.hide()
            
            
        if self.btnSimon.clicked:
            self.getHighScore()
            self.btnSimon.hide()
            self.btnPuzzle.hide()
            self.btnStartSimon.show((320, 440))
            self.lblTitleSimon.show((320, 40))
            self.multiSimon.show((325, 245))
            
        if self.btnStartSimon.clicked:
            self.lblTitleSimon.hide()
            self.btnSimon.hide()
            self.btnStartSimon.hide()
            self.multiSimon.hide()
            self.screen.blit(self.background, (0,0))
            self.btnQuit.show((540,440))
            self.lblInputSimon.show((320,150))
            self.lblHighscore.show((100, 40))
            self.lblHighscore.text = "Highscore: " + self.highscore
            self.lblCurrentScore.show((540, 40))
            self.btnClear.show((100,80))
            self.btnSimonSolve.show((540,80))
            self.btnGreen.show((150 ,240))
            self.greenBtn.show()
            self.btnYellow.show((250 ,240))
            self.yellowBtn.show()
            self.btnBlue.show((350 ,240))
            self.blueBtn.show()
            self.btnRed.show((450 , 240))
            self.redBtn.show()
            self.btnSimonTrial.show((320, 440))
          
            
        if self.btnSimonTrial.clicked:
            self.btnSimonTrial.hide()
            self.createSimon()
            
        
        if self.btnStart.clicked:
            self.lblTitle.hide()
            self.btnStart.hide()
            self.multi.hide()
            self.screen.blit(self.background, (0,0))
            self.btnQuit.show((540,440))
            self.btnKeyA.show((190,240))
            self.btnKeyB.show((235,240))
            self.btnKeyC.show((280,240))
            self.btnKeyD.show((320,240))
            self.btnKeyE.show((365,240))
            self.btnKeyF.show((405,240))
            self.btnKeyG.show((450,240))
            self.lblInput.show((320,40))
            self.btnCheck.show((540,40))
            self.btnClear.show((100,40))
            self.lblAttempts.show((540, 80))
            self.btnClue.show((100, 440))
            self.piano.show()
            self.counter = 3
            self.lblAttempts.text = "Attempts: " + str(self.counter)
            self.createKey()
            
            
            
        if self.inputlen < 4:
            if self.btnKeyA.clicked:
                self.btnKeyASound.play()
                self.lblInput.text += "A"
                self.inputlen += 1
            if self.btnKeyB.clicked:
                self.lblInput.text += "B"
                self.btnKeyBSound.play()
                self.inputlen += 1
            if self.btnKeyC.clicked:
                self.lblInput.text += "C"
                self.btnKeyCSound.play()
                self.inputlen += 1
            if self.btnKeyD.clicked:
                self.lblInput.text += "D"
                self.btnKeyDSound.play()
                self.inputlen += 1
            if self.btnKeyE.clicked:
                self.lblInput.text += "E"
                self.btnKeyESound.play()
                self.inputlen += 1
            if self.btnKeyF.clicked:
                self.lblInput.text += "F"
                self.btnKeyFSound.play()
                self.inputlen += 1
            if self.btnKeyG.clicked:
                self.lblInput.text += "G"
                self.btnKeyGSound.play()
                self.inputlen += 1
                
        if self.btnGreen.clicked:
            self.btnGreenSound.play()
            #self.greenLight.show()
            self.lblInputSimon.text += "G"
            #time.sleep(.75)
            #self.greenLight.hide()
        if self.btnYellow.clicked:
            self.btnYellowSound.play()
            self.lblInputSimon.text += "Y"
        if self.btnBlue.clicked:
            self.btnBlueSound.play()
            self.lblInputSimon.text += "B"
        if self.btnRed.clicked:
            self.btnRedSound.play()
            self.lblInputSimon.text += "R"
        """    
        if self.isKeyPressed(pygame.K_1):
            self.btnGreenSound.play()
            self.lblInputSimon.text += "G"
            """
            
            
        
                
                
        if self.btnReset.clicked:
            pygame.mixer.music.stop()
            game = Game()
            game.start()
            
            
        if self.btnClear.clicked:
            self.lblHint.hide()
            self.lblInputSimon.text = ""
            self.lblInput.text = ""
            self.inputlen = 0
            
        if self.btnClue.clicked:
            self.multiClue.textLines = self.solutionGuide
            self.multiClue.show((325,245))
            self.btnClue.hide()
            self.btnClueHide.show((100, 440))
            
        if self.btnClueHide.clicked:
            self.multiClue.hide()
            self.btnClueHide.hide()
            self.btnClue.show((100,440))
            
        if self.btnSimonSolve.clicked:
            if self.lblInputSimon.text == self.simonKey:
                self.lblInputSimon.text = ""
                self.lblCurrentScore.text = str(self.simonNum)
                self.currentScore += 1
                self.simonNum += 1
                self.createSimon()
            else:
                self.lblHint.show((320, 340))
                self.lblHint.size = (150, 30)
                self.lblHint.text = "You Lose!"
                pygame.mixer.music.load("sadloop.wav")
                pygame.mixer.music.set_volume(.8)
                pygame.mixer.music.play(-1)
                self.btnReset.show((320,440))
                self.saveHighScore()
            
        if self.btnCheck.clicked:
            self.lblHint.show((320,130))
            if self.lblInput.text == self.solutionKey:
                print("You win!")
                print(self.counter)
                print(self.lblInput.text)
                pygame.mixer.music.load("FugueInBMinor.flac")
                pygame.mixer.music.set_volume(.4)
                pygame.mixer.music.play(-1)
                self.lblHint.text = "Congratulations! You win!"
                self.btnReset.show((320,440))
            elif self.counter == 0:
                print("You lose!")
                pygame.mixer.music.load("sadloop.wav")
                pygame.mixer.music.set_volume(.8)
                pygame.mixer.music.play(-1)
                self.btnKeyA.hide()
                self.btnKeyB.hide()
                self.btnKeyC.hide()
                self.btnKeyD.hide()
                self.btnKeyE.hide()
                self.btnKeyF.hide()
                self.btnKeyG.hide()
                self.btnReset.show((320,440))
                self.lblHint.text = "You lose. Try again."
            elif self.lblInput.text == "":
                self.lblHint.text = "No Input. Please try again"
            elif self.lblInput.text != "":
                self.counter -= 1
                self.lblAttempts.text = "Attempts: " + str(self.counter)
                self.inputlen = 0
                print(self.counter)
                print(self.lblInput.text)
                self.lblHint.text = "Incorrect Response. Try Again"
                
        if self.btnQuit.clicked:
            self.stop()
        

            
class PianoKeys(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Piano2.png")
        self.setSize(300, 200)
        self.setPosition((320, 240))
        
class SimonButtons(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        
        

# def main():
    # game = Game()
    # game.start()
    
    
# if __name__ == "__main__":
    # main()
        
    
        
        

