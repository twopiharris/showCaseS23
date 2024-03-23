import pygame,simpleGE
import os,sys
"""
This file contains the start 
screen for an Arcade machine located
at Ball State in the Computer Science Department. 
All image citations below. 

Ball State Logo: Taken from official twitter page
Arcade Background Image: https://www.vecteezy.com/vector-art/5266448-vector-retro-futuristic-background
Arcade Font: https://www.dafont.com/arcade-ya.font
Selection Border: https://pngimg.com/image/90845


Nolan Meyer

March 21, 2023
"""

#Creates the class that contains the scene
class StartScreen(simpleGE.Scene):

    def __init__(self):
        super().__init__()
        
        #Creates the background image and sets the caption of the screen
        self.setCaption("Arcade Machine")
        self.background = pygame.image.load("arcadeBackground.jpg")
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background,self.screen.get_size())

        #Adds the image for the ball state logo in the corner
        self.ballState_logo = simpleGE.Sprite(self)
        self.ballState_logo.setImage("ballStateLogo.jpg")
        self.ballState_logo.setSize(80,80)
        self.ballState_logo.position = (600,445)

        #Creates the title image
        self.titleLabel = simpleGE.Label()
        self.titleLabel.text = "CS 120 Games!"
        self.titleLabel.center = (320,230)
        self.titleLabel.clearBack = True
        self.titleLabel.size = (400,400)
        self.titleLabel.font = pygame.font.Font("ARCADE_N.TTF",30)
        self.titleLabel.fgColor = (255,215,0)

        #Creates the pop up that tells what button to click when ready to play
        self.playLabel = simpleGE.Label()
        self.playLabel.text = "Click B to Play!"
        self.playLabel.center = (320,550)
        self.playLabel.clearBack = True
        self.playLabel.size = (500,400)
        self.playLabel.font = pygame.font.Font("ARCADE_N.TTF",30)
        self.playLabel.fgColor = (255,215,0)
        self.playLabel.hide()

        #Border that shows that something is selected
        self.selectBorder = simpleGE.Sprite(self)
        self.selectBorder.setImage("selectionBorder.png")
        self.selectBorder.setSize(120,120)
        self.selectBorder.position = (120,120)
        self.selectBorder.hide()

        #Border that shows that something is selected
        self.warriorsArenaLogo = simpleGE.Sprite(self)
        self.warriorsArenaLogo.setImage("warriors-arena-logo.png")
        self.warriorsArenaLogo.setSize(80,70)
        self.warriorsArenaLogo.position = (100,240)

        #Keeps track if a current game is selected or not
        self.gameSelected = ""
        self.startClicked = False
        


             
        


        #Adds all the sprites to the sprite list
        self.sprites = [self.ballState_logo,self.titleLabel,self.selectBorder,self.warriorsArenaLogo,self.playLabel]

    #This is going to look for keyboard input(Joystick mapping) and decide what the selection is
    def process(self):
        
        if self.isKeyPressed(pygame.K_d):
            self.selectBorder.show()
            self.selectBorder.position = self.warriorsArenaLogo.position
            self.playLabel.show()
            self.gameSelected = "Warriors-Arena"
            self.startClicked = True

        #Key that plays the gaem
        if self.isKeyPressed(pygame.K_b):

            if self.startClicked:
                self.stop()

            
        





#Main function that starts the scene
def main():

    startScreen = StartScreen()
    startScreen.start() 

    #Checks to see what game has been selcted
    if startScreen.gameSelected == "Warriors-Arena":
        pass






if __name__ == "__main__":
    main()