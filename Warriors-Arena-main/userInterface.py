import simpleGE,pygame,game,time
"""
User interface for the start screen. This allows you to 
select your character's then start the game. All citing for
images/sound is located in the game file source code.

Nolan Meyer

Novemeber 28, 2023
"""

#Class that controls the user interface
class UserInterface(simpleGE.Scene):

    def __init__(self):
        
        super().__init__()

        #Setup the screen
        self.setCaption("Start Screen")
        self.background = pygame.Surface((self.screen.get_size()))
        self.background.fill("black")

        #Logo
        self.logo = simpleGE.SuperSprite(self)
        self.logo.imageMaster = pygame.image.load("UI/logo.png")
        self.logo.setPosition((320,200))
        self.logo.setSize(300,300)


        #Knight Headshot
        self.knightHeadshot = simpleGE.SuperSprite(self)
        self.knightHeadshot.imageMaster = pygame.image.load("Knight/knight_headshot.png")
        self.knightHeadshot.setSize(75,75)
        self.knightHeadshot.setPosition((50,400))
        self.knightHeadshot.hide()
        

        #Minotuar HeadShot
        self.minotaurHeadshot = simpleGE.SuperSprite(self)
        self.minotaurHeadshot.imageMaster = pygame.image.load("Minotaur/minotaur_headshot.png")
        self.minotaurHeadshot.setSize(75,75)
        self.minotaurHeadshot.setPosition((590,400))
        self.minotaurHeadshot.hide()


        #Talos Headshot
        self.talosHeadshot = simpleGE.SuperSprite(self)
        self.talosHeadshot.imageMaster = pygame.image.load("Talos/talos_headshot.png")
        self.talosHeadshot.setSize(75,75)
        self.talosHeadshot.setPosition((320,400))
        self.talosHeadshot.hide()


        #Control label
        self.P1control = simpleGE.MultiLabel()
        self.P1control.textLines = ["Player Controls: Hit- Red, Block- White, LT Walk- Stick LT", 
                                    "RT Walk- Stick RT, Jump- Stick Up, Special- Yellow",
                                    "Player 1 Left Controls, Player 2 Right Controls.", "Use joystick and red key to select character" ]
        self.P1control.size = (620,150)
        self.P1control.bgColor = ("orange")
        self.P1control.hide()

        #Sounds
        self.player1Sound = simpleGE.Sound("UI/player_1.wav")
        self.player2Sound = simpleGE.Sound("UI/player_2.wav")
        self.chooseCharacter = simpleGE.Sound("UI/choose_your_character.wav")
        self.selectSound = simpleGE.Sound("UI/click.wav")

        self.selectionTurn = 1

        #Background music
        pygame.mixer.music.load("UI/loadingScreenSound.mp3")
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play(-1)

        #Red Border
        self.redBorder = simpleGE.SuperSprite(self)
        self.redBorder.imageMaster = pygame.image.load("UI/redBorder.png")
        self.redBorder.setSize(90,90)
        self.redBorder.setPosition((320,400))
        self.redBorder.hide()

        #Creates the pop up that tells what button to click when ready to play
        self.startLabel = simpleGE.Label()
        self.startLabel.text = "Player 1 Click Red To Begin!"
        self.startLabel.center = (320,375)
        self.startLabel.bgColor = (0,0,0)
        self.startLabel.size = (620,70)
        self.startLabel.font = pygame.font.Font("UI/ARCADE_N copy.TTF",20)
        self.startLabel.fgColor = (255,215,0)

        #Variables that will contain the selections
        self.player1 = ""
        self.player2 = ""
        
        #Keeps track of where the user is selecting and variable for if you're on the start screen
        self.selectionNumber = 0
        self.startScreen = True

        self.sprites = [self.knightHeadshot,self.minotaurHeadshot,self.logo,self.P1control,self.talosHeadshot,self.redBorder,self.startLabel]


    #Checks that both characters have selected a character and ready to fight
    def update(self):

        if self.isKeyPressed(pygame.K_f) and self.startScreen == True:

            self.logo.hide()
            self.knightHeadshot.show()
            self.minotaurHeadshot.show()
            self.talosHeadshot.show()
            self.P1control.show((320,180))
            self.startLabel.hide()
            self.startScreen = False

            self.player1Sound.play()
            time.sleep(1)
            self.chooseCharacter.play()


        if self.selectionTurn == 3 and self.isKeyPressed(pygame.K_f):
            pygame.mixer.music.stop()
            self.stop()
    
        if self.selectionTurn == 1:
            if self.isKeyPressed(pygame.K_d):
                
                if self.selectionNumber == 4:
                    self.selectionNumber = 1
                    time.sleep(0.2)

                else:
                    self.selectionNumber += 1
                    time.sleep(0.2)

            if self.isKeyPressed(pygame.K_a):
                if self.selectionNumber == 1:
                    self.selectionNumber = 3
                    time.sleep(0.2)

                else:
                    self.selectionNumber -=1
                    time.sleep(0.2)
        
        if self.selectionTurn == 2:

            if self.isKeyPressed(pygame.K_l):
                
                if self.selectionNumber == 4:
                    self.selectionNumber = 1
                    time.sleep(0.2)
                    

                else:
                    self.selectionNumber += 1
                    time.sleep(0.2)

            if self.isKeyPressed(pygame.K_j):

                if self.selectionNumber == 1:
                    self.selectionNumber = 3
                    time.sleep(0.2)

                else:
                    self.selectionNumber -=1
                    time.sleep(0.2)
            
        if self.selectionNumber == 1:
            self.redBorder.setPosition((self.knightHeadshot.x,self.knightHeadshot.y))
        
        elif self.selectionNumber == 2:
            self.redBorder.setPosition((self.talosHeadshot.x,self.talosHeadshot.y))

        elif self.selectionNumber == 3:
            self.redBorder.setPosition((self.minotaurHeadshot.x,self.minotaurHeadshot.y))
        
        elif self.selectionNumber == 4:
            self.selectionNumber = 1
        
        elif self.selectionNumber == -1:
            self.selectionNumber = 3

        
        if self.isKeyPressed(pygame.K_f):

            #Selection for the knight character
                if (self.selectionTurn == 1) and self.selectionNumber == 1:
                    self.selectSound.play()
                    self.knightHeadshot.imageMaster = pygame.image.load("Knight/knight_headshotSelected.png")
                    self.knightHeadshot.setSize(75,75)
                    self.selectionTurn += 1 
                    self.player1 = "knight"
                    self.player2Sound.play()
                    time.sleep(1)
                    self.chooseCharacter.play()
                    self.redBorder.hide()
                    self.selectionNumber = 0


                #Minotaur selection
                if (self.selectionTurn == 1) and self.selectionNumber == 3:
                    self.selectSound.play()
                    self.minotaurHeadshot.imageMaster = pygame.image.load("Minotaur/minotaur_headshotSelected.png")
                    self.minotaurHeadshot.setSize(75,75)
                    self.selectionTurn += 1 
                    self.player1 = "minotaur"
                    self.player2Sound.play()
                    time.sleep(1)
                    self.chooseCharacter.play()
                    self.redBorder.hide()
                    self.selectionNumber = 0
                    
                
                #Talos Selection
                if (self.selectionTurn == 1) and self.selectionNumber == 2:
                    self.selectSound.play()
                    self.talosHeadshot.imageMaster = pygame.image.load("Talos/talos_headshotSelected.png")
                    self.talosHeadshot.setSize(75,75)
                    self.selectionTurn += 1 
                    self.player1 = "talos"
                    self.player2Sound.play()
                    time.sleep(1)
                    self.chooseCharacter.play()
                    self.redBorder.hide()
                    self.selectionNumber = 0
        

        #Code for player 2 selection
        if self.isKeyPressed(pygame.K_h):

            if (self.selectionTurn == 2) and (self.selectionNumber == 1) and (self.player1 != "knight") :
                self.selectSound.play()
                self.knightHeadshot.imageMaster = pygame.image.load("Knight/knight_headshotSelected.png")
                self.knightHeadshot.setSize(75,75)
                self.selectionTurn += 1 
                self.player2 = "knight"
                self.redBorder.hide()
                self.selectionNumber = 0
                self.startLabel.show((320,70))
                self.startLabel.text = "Player 1: Click Red to Fight!"
            
            if (self.selectionTurn == 2) and (self.selectionNumber == 3) and (self.player1 != "minotaur"):
                self.selectSound.play()
                self.minotaurHeadshot.imageMaster = pygame.image.load("Minotaur/minotaur_headshotSelected.png")
                self.minotaurHeadshot.setSize(75,75)
                self.selectionTurn += 1 
                self.player2 = "minotaur"
                self.redBorder.hide()
                self.selectionNumber = 0
                self.startLabel.show((320,70))
                self.startLabel.text = "Player 1: Click Red to Fight!"
            
            if (self.selectionTurn == 2) and (self.selectionNumber == 2) and (self.player1 != "talos"):

                self.selectSound.play()
                self.talosHeadshot.imageMaster = pygame.image.load("Talos/talos_headshotSelected.png")
                self.talosHeadshot.setSize(75,75)
                self.selectionTurn += 1 
                self.player2 = "talos"
                self.redBorder.hide()
                self.selectionNumber = 0
                self.startLabel.show((320,70))
                self.startLabel.text = "Player 1: Click Red to Fight!"
            

            





#Main function that declares the scene
def main():
   
    UI = UserInterface()
    UI.start()

    player1 = UI.player1
    player2 = UI.player2

    try:
        gameplay = game.Game(player1,player2)
        gameplay.start()
    
    except:
        pass


#Calls the main function
if __name__ == "__main__":

    main()