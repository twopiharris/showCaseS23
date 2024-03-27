# -*- coding: utf-8 -*-
"""
https://opengameart.org/content/animated-top-down-survivor-player
https://opengameart.org/content/animated-top-down-zombie
https://opengameart.org/content/light-machine-gun
https://www.behance.net/gallery/6363497/Top-down-shooter-map
https://wallpapercave.com/w/HEGhEeg
https://opengameart.org/content/handgun-reload-sound-effect
https://opengameart.org/content/grunts-male-death-and-pain
https://opengameart.org/content/night-of-the-streets-horrorsuspense
https://opengameart.org/content/2d-pixel-art-guns
https://opengameart.org/content/demon-voice-game-over


Created on Mon Nov 20 10:08:07 2023

@author: sport
"""

import pygame
import random
import simpleGE

class main:
    def __init__():
        pass
    
    def main():
        startMenu = StartMenu()
        startMenu.start()

class Gunner(simpleGE.SuperSprite):
    def __init__(self, scene):
        simpleGE.SuperSprite.__init__(self, scene)
        self.setImage("GunnerPistol.png")
        self.setSize(60,60)
        self.setPosition((300,250))
        self.health = 100
        self.damageCooldown = simpleGE.Timer()
    
    def CheckEvents(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5
        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_s]:
            self.y += 5
 
        self.x = max(0, min(self.x, self.scene.screen.get_width()))
        self.y = max(0, min(self.y, self.scene.screen.get_height()))   
 
        mouseX, mouseY = pygame.mouse.get_pos()
        self.setAngle(self.dirTo((mouseX, mouseY)))
        
    def getPosition(self):
        return self.x, self.y
   
    def canTakeDamage(self):
        return self.damageCooldown.getElapsedTime() >= 1.25    
   
    def takeDamage(self, damage):
        if self.canTakeDamage():
            self.health -= damage
            if self.health <= 0:
                self.health = 0
            self.damageCooldown.start()
            
    def getHealth(self):
        return self.health

        
class Zombie(simpleGE.SuperSprite):
    def __init__(self, scene):
        simpleGE.SuperSprite.__init__(self, scene)
        self.setImage("ZombieMove.gif")
        self.setSize(56, 56)
        self.reset()
        
    def checkEvents(self):
        self.moveToGunner()
        self.checkBounds()
        
    def reset(self):
        self.dx = 1
        self.dy = 1
        self.damage = 20
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            self.setPosition((random.randint(0, self.screen.get_width()), 0))
            self.dy = random.randint(1, 3)
            self.dx = random.randint(-3, 3)
        elif side == "bottom":
            self.setPosition((random.randint(0, self.screen.get_width()), self.screen.get_height()))
            self.dy = random.randint(-3, -1)
            self.dx = random.randint(-3, 3)
        elif side == "left":
            self.setPosition((0, random.randint(0, self.screen.get_height())))
            self.dx = random.randint(1, 3)
            self.dy = random.randint(-3, 3)
        elif side == "right":
            self.setPosition((self.screen.get_width(), random.randint(0, self.screen.get_height())))
            self.dx = random.randint(-3, -1)
            self.dy = random.randint(-3, 3)
                
        self.updateVector()
        
        self.scene.zombiesSpawned += 1
        
    def moveToGunner(self):
        gunnerPos = self.scene.gunner.getPosition()
        angle = self.dirTo(gunnerPos)
        self.setAngle(angle)
        self.setSpeed(0.7)
        
    def dealDamage(self):
        gunnerHit = self.collides(self.scene.gunner)
        if gunnerHit:
            if self.scene.gunner.canTakeDamage():
                self.scene.gunner.takeDamage(self.damage)
    
class Bullet(simpleGE.SuperSprite):    
    pistolSound = pygame.mixer.Sound("games\\ZombieLand\\HandgunSound.mp3")
    def __init__(self, scene):
        simpleGE.SuperSprite.__init__(self, scene)
        self.setImage("Bullet.png")
        self.setSize(10, 5)
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
        self.show()
        self.setPosition(self.scene.gunner.rect.center)
        self.setMoveAngle(self.scene.gunner.rotation)
        self.setSpeed(20)
        
    def reset(self):
        self.hide()
        
class Game(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.background = pygame.image.load("top down shooter map.png")
        self.background = pygame.transform.scale(self.background, (640,480))
        self.setCaption("Zombie Land")
        self.gunner = Gunner(self)
        
        pygame.mixer.music.load("InGameBackground.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1)
       
        self.NUM_BULLETS = 16
        self.currentBullet = 16
        self.zombiesKilled = 0
        self.zombiesSpawned = 3
        
        
        self.zombies = []
        for i in range(2):
            self.zombies.append(Zombie(self))

        self.bullets = []
        for i in range(self.NUM_BULLETS):
            self.bullets.append(Bullet(self))
                                                
                
        self.zombieGroup = self.makeSpriteGroup(self.zombies)
        self.addGroup(self.zombieGroup)        
        
        self.lblKills = simpleGE.Label()
        self.lblKills.text = f"Kills: {self.zombiesKilled}"
        self.lblKills.font = pygame.font.Font(None, 35)
        self.lblKills.center = (550, 35)
        self.lblKills.fgColor = (255, 255, 255)
        self.lblKills.bgColor = (0, 0, 0)
        
        self.lblBullets = simpleGE.Label()
        self.lblBullets.text = f"Bullets Left: 16/ {self.currentBullet}"
        self.lblBullets.font = pygame.font.Font(None, 35)
        self.lblBullets.center = (310, 460)
        self.lblBullets.size = (220, 30)
        self.lblBullets.fgColor = (255, 255, 255)
        self.lblBullets.bgColor = (0, 0, 0)

        self.lblHealth = simpleGE.Label()
        self.lblHealth.text = f"Health: {self.gunner.getHealth()}"
        self.lblHealth.font = pygame.font.Font(None, 35)
        self.lblHealth.center = (100, 35)
        self.lblHealth.fgColor = (255, 255, 255)
        self.lblHealth.bgColor = (0, 0, 0)

        self.gameOver = False
        self.sprites = [self.lblHealth, self.lblKills, self.lblBullets, self.zombies, self.gunner, self.bullets]
        
    def resetGame(self):
        if not self.gameOver:
            self.gunner.setPosition((300, 250))
            
            for zombie in self.zombies:
                zombie.reset()
                
            for bullet in self.bullets:
                bullet.hide()
                                    
    def doEvents(self, event):
        if not self.gameOver:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.currentBullet > 0:
                    self.currentBullet -= 1
                    self.bullets[self.currentBullet].fire()
                    Bullet.pistolSound.set_volume(0.5)
                    Bullet.pistolSound.play()
                elif self.currentBullet == 0:    
                    print("Out of bullets")
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.currentBullet = min(self.NUM_BULLETS, self.currentBullet + 16)
                    reload = simpleGE.Sound("reload.wav")
                    reload.play()
        elif event.type == pygame.QUIT: 
            pygame.quit()
                            
    def update(self):
        self.gunner.CheckEvents()
        
        if not self.gameOver:   
            self.lblKills.text = f"Kills: {self.zombiesKilled}"
            self.lblBullets.text = f"Bullets Left: 16/{self.currentBullet}"
            self.lblHealth.text = f"Health: {self.gunner.getHealth()}"        
        
        zombieHitGunner = self.gunner.collidesGroup(self.zombies)
        if zombieHitGunner:
            self.gunner.takeDamage(20)
            hit = simpleGE.Sound("GettingHitSound.wav")
            hit.play()
            if self.gunner.getHealth() == 0:
                dyingSound = simpleGE.Sound("DyingSound.wav")
                dyingSound.play()
                    
                self.gameOver = True
                gameOverScene = GameOverScene(self.zombiesKilled)
                gameOverScene.start()
                    
                    
        for bullet in self.bullets:
            if bullet.visible:
                zombieHitBullet = bullet.collidesGroup(self.zombies)
                if zombieHitBullet:
                    self.zombiesKilled += 1
                    zombieHit = simpleGE.Sound("ZombieHitSound.wav")
                    zombieHit.play()
                    bullet.reset()
                    zombieHitBullet.reset()
                        
                    if self.zombiesKilled % 10 == 0:
                        self.spawnMoreZombies(2)
                                    
        for zombie in self.zombies:
            zombie.checkEvents()
            zombie.update()
        
    def spawnMoreZombies(self, moreZombies):
        for i in range(moreZombies):
            newZombie = Zombie(self)
            self.zombies.append(newZombie)
            self.zombieGroup.add(newZombie)
            
class StartMenu(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.background = pygame.image.load("FrontZombieScreen.webp")
        self.background = pygame.transform.scale(self.background, (640,480))
        
        pygame.mixer.music.load("ZombieBackgroundMusic.mp3")
        pygame.mixer.music.set_volume(3)
        pygame.mixer.music.play(3)
        
        self.addLabels()
        self.startButton()
        self.addMultiLabel()
        
        self.sprites = [self.lblTitle, self.label,
                        self.lblButton, self.button,
                        self.multi]
    
    def addLabels(self):        
        
        
        self.lblTitle = simpleGE.Label()
        self.lblTitle.text = "Zombie Land"
        self.lblTitle.font = pygame.font.Font("ZombieFont.otf", 50)
        self.lblTitle.center = (200, 60)
        self.lblTitle.size = (355, 80)
        self.lblTitle.fgColor = (255, 255, 255)
        self.lblTitle.bgColor = (0, 0, 0)
        
        self.label = simpleGE.Label()
        self.label.text = "High Score: "
        self.label.center = (200, 235)
        self.label.size = (155, 30)
        self.label.fgColor = (0, 0, 0)
        self.label.bgColor = (0, 0, 0)
        
    def startButton(self): 
        self.lblButton = simpleGE.Label()
        self.lblButton.center = (180, 2000)
        self.lblButton.text = "START!"
        self.lblButton.size = (200, 90)
        self.lblButton.fgColor = (255, 255, 255)
        self.lblButton.bgColor = (0, 0, 0)
        
        self.button = simpleGE.Button()
        self.button.center = (180, 200)
        self.button.text = "START!"
        self.button.font = pygame.font.Font("ZombieFont.otf", 35)
        self.button.size = (200, 90)
        self.button.fgColor = (255, 255, 255)
        self.button.bgColor = (0, 0, 0)
        self.button.onRelease = self.startGame
    
    def addMultiLabel(self):
        self.multi = simpleGE.MultiLabel()
        self.multi.textLines = [
            "How to Play:",
            "Use the W and S keys,",
            "to go forward and backwards.",
            "Use the A and D keys to move to side.",
            "Use the mouse to aim and shoot at Zombies.",
            "Press R to reload bullets "
            ]
        self.multi.font = pygame.font.Font("ZombieFont.otf", 13)
        self.multi.size = (390, 195)
        self.multi.center = (185, 350)
        self.multi.fgColor = (255, 255, 255)
        self.multi.bgColor = (0, 0, 0)
        
    def update(self):        
        if self.button.clicked:
            game = Game()
            game.start()
        
    def startGame(self):
        gameScene = Game()
        gameScene.start()
        
class GameOverScene(simpleGE.Scene):
    def __init__(self, zombiesKilled):
        simpleGE.Scene.__init__(self)
        self.zombiesKilled = zombiesKilled
        
        pygame.mixer.music.load("GameOverVoice.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(1)
        
        self.gameOverLabel()
        self.finalWaveLabel()
        self.playAgain()
        self.restartAction()
        self.quitAction()
        
        self.sprites = [self.lblGameOver, self.lblFinalKills,
                        self.lblButton, self.lblPlayAgain, self.restartButton,
                        self.lblQuitButton, self.quitButton]
    
    def gameOverLabel(self):
        self.lblGameOver = simpleGE.Label()
        self.lblGameOver.text = "Game Over"
        self.lblGameOver.font = pygame.font.Font("ZombieFont.otf", 70)
        self.lblGameOver.fgColor = ("red")
        self.lblGameOver.bgColor = (0, 0, 0)
        self.lblGameOver.center = (310, 250)
        self.lblGameOver.size = (450, 200)
        
    def finalWaveLabel(self):    
        self.lblFinalKills = simpleGE.Label()
        self.lblFinalKills.text = f"You Killed {self.zombiesKilled} Zombies"
        self.lblFinalKills.center = (310,285)
        self.lblFinalKills.fgColor = ("white")
        self.lblFinalKills.bgColor = (0, 0, 0)
        self.lblFinalKills.size = (250, 50)
    
    def playAgain(self):
        self.lblPlayAgain = simpleGE.Label()
        self.lblPlayAgain.center = (310, 345)
        self.lblPlayAgain.text = "Play Again?"
        self.lblPlayAgain.fgColor = (255, 255, 255)
        self.lblPlayAgain.bgColor = (0, 0, 0)
    
    def restartAction(self):
        self.lblButton = simpleGE.Label()
        self.lblButton.center = (270, 400)
        self.lblButton.text = "Yes"
        self.lblButton.size = (75, 75)
        self.lblButton.fgColor = (255, 255, 255)
        self.lblButton.bgColor = (0, 0, 0)
        
        self.restartButton = simpleGE.Button()
        self.restartButton.center = (270, 400)
        self.restartButton.text = "Yes"
        self.restartButton.size = (75, 75)
        self.restartButton.fgColor = (255, 255, 255)
        self.restartButton.bgColor = (0, 0, 0)
        self.restartButton.onRelease = self.startGame
    
    def quitAction(self):
        self.lblQuitButton = simpleGE.Label()
        self.lblQuitButton.center = (350, 400)
        self.lblQuitButton.text = "No"
        self.lblQuitButton.size = (75, 75)
        self.lblQuitButton.fgColor = (255, 255, 255)
        self.lblQuitButton.bgColor = (0, 0, 0)
        
        self.quitButton = simpleGE.Button()
        self.quitButton.center = (350, 400)
        self.quitButton.text = "No"
        self.quitButton.size = (75, 75)
        self.quitButton.fgColor = (255, 255, 255)
        self.quitButton.bgColor = (0, 0, 0)
        self.quitButton.onRelease = self.quit
            
    def update(self):
        if self.restartButton.clicked:
            game = Game()
            game.start()
        if self.quitButton.clicked:
            self.stop()
    
    def startGame(self):
        gameScene = Game()
        gameScene.start()
    
    def quit(self):
        pygame.quit()
        
def main():
    startMenu = StartMenu()
    startMenu.start()
    
if __name__ == "__main__":
    main()
