import simpleGE, pygame, math, json, os

class main:
    def __init__():
        pass
    
    def main():
        game = Game()
        game.start()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((1300, 1000 ))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((0, 0, 0))

        with open('levelData.json', 'r') as f:
            levelData = json.load(f)
            self.floorCount = levelData["floors"]
            self.__currentFloor = 0
            self.platforms = self.makeSpriteGroup([Platform(self, platformData) for platformData in levelData["plats"]])

        self.STARTMENU, self.DIRMENU, self.PLAYING, self.RESET, self.PAUSEMENU, self.WINMENU, self.QUIT = range(0,7)
        self.__gamestate = -1
        self.gameStarted = False

        self.character = Character(self)

        self.startMenu = self.getMenuSpriteGroup('jump guy', {'play': [lambda: self.setGamestate(self.DIRMENU)], 
                                                              'quit': [lambda: self.setGamestate(self.QUIT)]})
        self.pauseMenu = self.getMenuSpriteGroup('jump guy', {'continue': [lambda: self.setGamestate(self.PLAYING)], 
                                                              'reset': [lambda: self.setGamestate(self.RESET)], 
                                                              'quit': [lambda: self.setGamestate(self.QUIT)]})
        self.winMenu = self.getMenuSpriteGroup('you won!', { 'reset': [lambda: self.setGamestate(self.RESET)], 
                                                              'quit': [lambda: self.setGamestate(self.QUIT)]})
        self.dirMenu = self.getDirectionsSpriteGroup()

        self.floorImages = [pygame.image.load(f'images/floors/{i}.png').convert_alpha() for i in range(0,7)]
        self.platformImages = [pygame.image.load(f'images/platform/{i}.png').convert_alpha() for i in range(0,7)]

        self.sprites = [self.character]
        self.spriteGroups = [self.platforms, self.startMenu, self.dirMenu, self.pauseMenu, self.winMenu]
        for spriteGroup in self.spriteGroups:
            self.addGroup(spriteGroup)

        self.setGamestate(self.STARTMENU)
    
    def changeBackground(self):
        floorImg = self.floorImages[self.__currentFloor % 7]


        self.background.blit(floorImg, (0,0))
        self.screen.blit(self.background, (0,0))

        
    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.gamestate in [self.PLAYING, self.PAUSEMENU]:
                    if self.gamestate == self.PLAYING:
                        self.setGamestate(self.PAUSEMENU)
                    else: self.setGamestate(self.PLAYING)

    def texturePlatforms(self):
        platImg = self.platformImages[self.__currentFloor % 7]
        # for plat in self.platforms:
        #     plat.imageMaster = platImg.subsurface(plat.rect)
            
            
    def getMenuSpriteGroup(self, titleText, options):
        sprites = []
        title = Title(titleText)
        sprites.append(title)

        for text, actions in options.items():
            option = Option(text, actions, len(sprites))
            sprites.append(option)

        return self.makeSpriteGroup(sprites)
    
    def getDirectionsSpriteGroup(self):
        sprites = []

        options = {'back': [lambda: self.setGamestate(self.STARTMENU)], 'play': [lambda: self.setGamestate(self.PLAYING)]}
        for text, actions in options.items():
            option = Button(self, text, actions, len(sprites))
            sprites.append(option)

        instructions = Instructions(self)
        sprites.append(instructions)

        return self.makeSpriteGroup(sprites)

    #region floor change related code
    @property
    def floor(self):
        return self.__currentFloor
    
    @floor.setter
    def floor(self, newFloor):
        self.handleFloorChange(newFloor)
    
    def handleFloorChange(self, newFloor):
        if self.floor == newFloor: return
        if newFloor not in range(0, self.floorCount):
            if newFloor == self.floorCount:
                self.setGamestate(self.WINMENU)
                return
            newFloor = 0
        
        floorChange = newFloor - self.floor

        # print(f"changing floor to: {newFloor}")
        for plat in self.platforms:
            if plat.name not in ['left', 'right']:
                plat.y += 1000 * (floorChange)
        self.__currentFloor = newFloor
        self.changeBackground()
    #endregion

    def hideAllSprites(self):
        for sprite in self.sprites:
                sprite.hide()
        for spriteGroup in self.spriteGroups:
            for sprite in spriteGroup.sprites():
                sprite.hide()
    #region gamestate related code
    @property
    def gamestate(self):
        return self.__gamestate
    
    def setGamestate(self, newGamestate):
        self.handleGamestateChange(newGamestate)
    
    def handleGamestateChange(self, newGamestate):
        if self.gamestate == newGamestate: return
        
        if newGamestate == self.STARTMENU:
            self.__gamestate = self.STARTMENU
            self.hideAllSprites()

            for sprite in self.startMenu:
                sprite.show(sprite.position)
            
            self.changeBackground()

        if newGamestate == self.DIRMENU:
            self.__gamestate = self.DIRMENU
            self.hideAllSprites()

            for sprite in self.dirMenu:
                sprite.show(sprite.position)

        if newGamestate == self.PLAYING:
            self.__gamestate = self.PLAYING
            self.hideAllSprites()

            for plat in self.platforms:
                plat.show()
            self.texturePlatforms()
            self.character.show()

            if not self.gameStarted:
                self.gameStarted = True   

        if newGamestate == self.PAUSEMENU:
            self.__gamestate = self.PAUSEMENU
            self.hideAllSprites()

            for sprite in self.pauseMenu:
                sprite.show(sprite.position)    

        if newGamestate == self.RESET:
            self.__gamestate = self.PLAYING
            self.hideAllSprites()
                     
            for plat in self.platforms:
                plat.show()
            
            self.floor = 0
            self.character.show()
            self.character.setDX(0)
            self.character.setDY(0)
            self.character.x = self.character.spawn[0]
            self.character.y = self.character.spawn[1]
        
        if newGamestate == self.WINMENU:
            self.__gamestate = self.WINMENU
            self.hideAllSprites()

            for sprite in self.winMenu:
                sprite.show(sprite.position)   
    
        if newGamestate == self.QUIT:
            self.stop()
        
    #endregion
        
#region sprites
class Character(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage('character.png')
        self.setSize(85,100)

        self.gravity = 1.35
        self.walkSpeed = 20
        self.bounceAmount = .8
        self.maxJump = {"power": 45, "angle": 65, "l": False, "r": False}

        self.x = self.y = 600
        self.spawn = (self.x, self.y)

        self.enableDataTrace = False

        self.__currentJump = {"power": 0, "angle": 0}
        self.__isJumping = False
        self.__jumped = False
        self.__colliding = {"t": False, "r": False, "b": False, "l": False}
        self.__walking = {"l": False, "r": True}

    def handleCollisions(self):
        pTheta = self.dir / 180.0 * math.pi
        pDx = math.cos(pTheta) * self.speed
        pDy = math.sin(pTheta) * self.speed
        pDy *= -1

        oldColliding = self.__colliding
        newColliding = {"t": False, "r": False, "b": False, "l": False}

        #region platform bounds
        for plat in self.scene.platforms:
            willCollideRight = self.rect.left + int(pDx) <= plat.rect.right and self.rect.right + int(pDx) > plat.rect.right
            willCollideLeft = self.rect.right + int(pDx) >= plat.rect.left and self.rect.left + int(pDx) < plat.rect.left
            willCollideTop = self.rect.bottom + int(pDy) >= plat.rect.top - 1 and self.rect.top + int(pDy) < plat.rect.top and self.y < plat.y
            willCollideBottom = self.rect.top + int(pDy) < plat.rect.bottom and self.rect.bottom + int(pDy) > plat.rect.bottom and self.y > plat.y

            inVertRange = (self.rect.top < plat.rect.bottom and self.rect.top > plat.rect.top) or (self.rect.bottom > plat.rect.top and self.rect.bottom < plat.rect.bottom) #or (self.rect.left < plat.rect.left and self.rect.right > plat.rect.right and (self.x - self.rect.left) > (plat.x - plat.rect.left))
            inHoriRange = (self.rect.left > plat.rect.left and self.rect.left < plat.rect.right) or (self.rect.right > plat.rect.left and self.rect.right < plat.rect.right)

             # top edge bound
            if willCollideTop and inHoriRange:
                self.setDY(0)
                self.y = math.floor(plat.rect.top - (self.image.get_height()/2))
                self.__jumped = False
                newColliding['b'] = True
            
            # bottom edge bound
            if willCollideBottom and inHoriRange:
                if not oldColliding["t"]:
                    self.setDY(0)
                    self.y = plat.rect.bottom + math.floor((self.image.get_height()/2)) 
                newColliding["t"] = True

            # right edge bound
            if willCollideRight and inVertRange:
                newColliding["l"] = True
                if oldColliding['b'] and not self.__jumped:
                    self.setDX(0)
                    self.x = math.floor(plat.rect.right + (self.x - self.rect.left)) + 1
                else:
                    self.setDX(self.dx*-self.bounceAmount)
                    if newColliding['b'] or newColliding['t']:
                        self.setDY(self.dy*-self.bounceAmount)

            # left edge bound
            if willCollideLeft and inVertRange:
                newColliding["r"] = True
                if self.__walking['r'] and not self.__jumped:
                    self.setDX(0)
                    self.x = math.floor(plat.rect.left - (self.x - self.rect.left)) - 1
                else:
                    self.setDX(self.dx*-self.bounceAmount)
                    if newColliding['b'] or newColliding['t']:
                        self.setDY(self.dy*-self.bounceAmount)
            
            self.__colliding = newColliding 
        #endregion
    
    def update(self):
        if not self.visible: 
            super().update()
            return
        
        if not self.__colliding['b']:
            self.addForce(self.gravity, 270)

        if self.__colliding["b"]:
            if not self.__isJumping:
                if not self.__colliding["l"] and self.__walking["l"]:
                    self.setDX(-self.walkSpeed)
                if not self.__colliding["r"] and self.__walking["r"]:
                    self.setDX(self.walkSpeed)
            if not self.__walking["l"] and not self.__walking["r"]:
                if self.__currentJump["angle"] == 0:
                    self.setDX(0)

        if self.__isJumping:
            self.__currentJump["angle"] += self.maxJump["angle"] * .035
            self.__currentJump["power"] += self.maxJump["power"] * .035
            if self.__currentJump["angle"] > self.maxJump["angle"]:
                self.__currentJump["angle"] = self.maxJump["angle"] 
            if self.__currentJump["power"] > self.maxJump["power"]:
                self.__currentJump["power"] = self.maxJump["power"] 
        else:
            if self.__currentJump["angle"] != 0:
                self.setDX(0)
                self.setDY(0)
                if self.scene.isKeyPressed(pygame.K_RIGHT):
                    self.addForce(self.__currentJump["power"], self.__currentJump["angle"])
                elif self.scene.isKeyPressed(pygame.K_LEFT):
                    self.addForce(self.__currentJump["power"], 180 - self.__currentJump["angle"])
                else:
                    self.addForce(self.__currentJump["power"], 90)
                self.__jumped = True
                self.__currentJump["angle"] = 0
                self.__currentJump["power"] = 0

        self.handleCollisions()
        super().update()
        
    def checkEvents(self):
        if not self.visible: return

        if self.enableDataTrace:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.dataTrace()
 
        if self.scene.isKeyPressed(pygame.K_r):
            self.x = self.y = 600
        if self.scene.isKeyPressed(pygame.K_t):
            self.enableDataTrace = not self.enableDataTrace
        if self.scene.isKeyPressed(pygame.K_y):
            self.scene.setGamestate(self.scene.WINMENU)

        if self.scene.isKeyPressed(pygame.K_c):
            self.x = pygame.mouse.get_pos()[0]
            self.y = pygame.mouse.get_pos()[1]

        self.__walking["l"] = self.scene.isKeyPressed(pygame.K_LEFT)
        self.__walking["r"] = self.scene.isKeyPressed(pygame.K_RIGHT)
        if self.__colliding['b']:
            if self.scene.isKeyPressed(pygame.K_SPACE):
                if not self.__isJumping:
                    self.__isJumping = True
                    self.setDX(0)
            else:
                self.__isJumping = False

    def dataTrace(self):
        print(f"""
            x: {self.x}, y: {self.y}
            speed: {self.speed}, dir: {self.dir}
            dx: {self.dx}, dy: {self.dy}
            {self.__colliding}
            rect: {self.rect}
            current jump: {self.__currentJump}""")
    
    def checkBounds(self):
        if not self.visible: return
        scrHeight = self.screen.get_height()
        
        offTop = offBottom = False

        if self.y > scrHeight:
            offBottom = True
        if self.y < 0:
            offTop = True
        
        if offBottom:
            if self.scene.floor - 1 in range(0, self.scene.floorCount):
                self.y = 0
            self.scene.floor -= 1
        if offTop:
            if self.scene.floor + 1 in range(0, self.scene.floorCount):
                self.y = scrHeight
            self.scene.floor += 1
    
    def show(self):
        if self.visible: return
        super().show()

    def hide(self):
        if not self.visible: return
        self.oldPosition = (self.x, self.y)
        self.x = -1000
        self.y = -1000
        self.visible = False

class Platform(simpleGE.SuperSprite):
    def __init__(self, scene, data):
        super().__init__(scene)
        self.setBoundAction(self.CONTINUE)
        self.image.fill((0xff,0xff,0xff))
        self.name = data["name"]
        self.setSize(data["width"], data["height"])
        self.x = data["x"] + (data["width"]/2)
        self.y = (data["y"] + (data["height"]/2)) - (1000 * (scene.floorCount - 1))
        
    def hide(self):
        if not self.visible: return
        self.oldPosition = (self.x, self.y)
        self.x = -1000
        self.y = -1000
        self.visible = False
    
    def show(self):
        if self.visible: return
        return super().show()

class Walls(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setBoundAction(self.CONTINUE)
        self.setImage('walls.png')

        self.mask = pygame.mask.from_surface(self.image)

        screenSize = scene.screen.get_size()
        self.x = screenSize[0]/2
        self.y = screenSize[1]
#endregion

#region UI
class Title(simpleGE.Label):
    def __init__(self, titleText, fontName="SpaceMono.ttf"):
        super().__init__(fontName)
        self.text = titleText
        self.size = (460,175)
        self.font = pygame.font.Font('SpaceMono.ttf', 95)
        self.x = 100 + self.size[0]/2
        self.y = 260 + self.size[1]/2
        self.position = (self.x, self.y)

class Option(simpleGE.Button):
    def __init__(self, text, actions, index):
        super().__init__()
        self.text = text
        self.actions = actions
        self.size = (93,41)
        self.x = 100 + self.size[0]/2
        optionSpacing = 8
        self.y = (521 + ((self.size[1] + optionSpacing )* (index)))+ self.size[1]/2
        self.position = (self.x, self.y)
    
    def update(self):
        super().update()
        if self.clicked:
            for action in self.actions:
                action()

class Button(Option):
    def __init__(self, scene, text, actions, index):
        super().__init__(text, actions, index)
        self.position = ((scene.screen.get_width()/2) - 100 + (index * 200), scene.screen.get_height() - 100)
        self.x = self.position[0]
        self.y = self.position[1]

class Instructions(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setBoundAction(self.CONTINUE)
        self.imageMaster = pygame.image.load('instructions.png').convert_alpha()
        self.x = scene.screen.get_width()/2 + 50
        self.y = 450
        self.position = (0, 0)
        
    def hide(self):
        if not self.visible: return
        self.oldPosition = (self.x, self.y)
        self.x = -1000
        self.y = -1000
        self.visible = False
    
    def show(self, pos):
        if self.visible: return
        return super().show()
#endregion

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()
