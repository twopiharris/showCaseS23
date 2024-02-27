# -*- coding: utf-8 -*-
"""
Cannon Defense 

Karter West 

Castle defense game 
Final 

"""

import simpleGe, random, pygame


class Wall(simpleGe.SuperSprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("WallPlaceHolder.png")
        self.setBoundAction(self.CONTINUE)
        self.setPosition((999,999))
        
class BasicEnemy(simpleGe.SuperSprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("Zombie.png")
        self.x = 999
        self.y = 20
        self.setBoundAction(self.CONTINUE)
        self.dmg = 1
        self.value = 1
        self.force = .04
        self.bounce = 3
        self.health = 5
        self.hitPoints = self.health
        
    def reset(self):
        self.setDY(0)
        self.y = 20
        self.x = random.randint(20,620)
        
    def kill(self):
        self.scene.enemiesLeft -= 1
        self.scene.money += self.value
        self.setDY(0)
        self.x = 999
        
    def checkEvents(self):    
        if self.x < 900:
            self.addForce(self.force, 270)
            
        if self.collidesWith(self.scene.wall):
            self.scene.wallHealth -= self.dmg
            self.setDY(0)
            self.addForce(self.bounce, 90) 
                    
        if self.collidesGroup(self.scene.CBs):
            if self.scene.upgrade1.center == (320,450):
                self.hitPoints -= 1
            elif self.scene.upgrade2.center == (320,450):
                self.hitPoints -= 3
            elif self.scene.upgrade3.center == (320,450):
                self.hitPoints-= 5
            elif self.scene.upgrade4.center == (320,450):
                self.hitPoints -=7
            elif self.scene.maxDmg.center == (320,450):
                self.hitPoints -= 10
        
        for cb in self.scene.CBs:
            if self.collidesGroup(self.scene.CBs):
                cb.hide()
                    
        if self.hitPoints <= 0:
            self.kill()
            self.hitPoints = self.health
                
class Boss(simpleGe.SuperSprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("Boss.png")
        self.health = 500
        self.hide()
        
    def reset(self):
        self.show()
        self.x = 320
        self.y = 100
        
    def checkEvents(self):
        if self.visible == True:
            self.addForce(.1, 270)
            
        if self.collidesGroup(self.scene.CBs):
            if self.scene.upgrade1.center == (320,450):
                self.health -= 1
            elif self.scene.upgrade2.center == (320,450):
                self.health -= 3
            elif self.scene.upgrade3.center == (320,450):
                self.health-= 5
            elif self.scene.upgrade4.center == (320,450):
                self.health -=7
            elif self.scene.maxDmg.center == (320,450):
                self.health -= 10
                
            
        for cb in self.scene.CBs:
            if self.collidesGroup(self.scene.CBs):
                cb.hide()
                
        if self.collidesWith(self.scene.wall):
            self.scene.wallHealth -= 8
            self.setDY(0)
            self.addForce(4, 90) 
        
        
class Cannon(simpleGe.SuperSprite):
    
    def __init__(self, scene):
        super().__init__(scene)
        
        self.setImage("Cannon.png")
        self.setSize(60,60)
        self.setPosition((999,999))
        self.setBoundAction(self.CONTINUE)
        self.rotateBy(90)
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= 5
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += 5
            
        if self.scene.isKeyPressed(pygame.K_a):
            self.x -= 5
        if self.scene.isKeyPressed(pygame.K_d):
            self.x += 5

class CannonBalls(simpleGe.SuperSprite):
    
    def __init__(self, scene, parent):
        super().__init__(scene)
        
        self.parent = parent
        self.setImage("CannonBall.png")
        self.setSize(20,20)
        self.dmg = 1
        self.setBoundAction(self.HIDE)
        self.hide()
        
    def fire(self):
        self.show()
        self.setPosition(self.parent.rect.center)
        self.setMoveAngle(self.parent.rotation)
        self.setSpeed(20)

class Begin(simpleGe.Button):
    
    def __init__(self, scene):
        super().__init__()
        
        self.text = "Start"
        self.show((340,400))
        
class UpgradeDmg(simpleGe.Button):
    
    def __init__(self,scene):
        
        super().__init__()
        
        self.text = "10 Coins: Upgrade Dmg: lvl 1"
        self.hide()
        self.size = (300,30)

class Game(simpleGe.Scene):
    
    def __init__(self):
        super().__init__()
        
        self.background = pygame.image.load("TitleScreen.png")
        
        pygame.mixer.music.load("CannonDefenseMusic.mp3")
        pygame.mixer.music.set_volume(.1)
        pygame.mixer.music.play(-1)
        
        self.wall = Wall(self)
        self.cannon = Cannon(self)
        self.NUM_CB = 100
        self.currentCB = 0
        self.CBs = []
        for i in range(self.NUM_CB):
            self.CBs.append(CannonBalls(self, self.cannon))
            
        self.enemies = []
        for i in range(40):
            self.enemies.append(BasicEnemy(self))
        self.waveNum = 0
        self.enemiesLeft = 0
        self.boss = Boss(self)
            
        self.disMoney = simpleGe.Label()
        self.disMoney.text = "Money: 0"
        self.disMoney.center = 999,999
        self.money = 0
        
        self.disWallHealth = simpleGe.Label()
        self.disWallHealth.text = "Health: 100"
        self.disWallHealth.center = 999,999
        self.wallHealth = 200
        
        self.disWave = simpleGe.Label()
        self.disWave.text = "Wave: 1"
        self.disWave.center = 999,999
        
        self.disBossHealth = simpleGe.Label()
        self.disBossHealth.text = "Boss Health: 100"
        self.disBossHealth.center = 999,999
        
        self.begin = Begin(self)
        self.quit = Begin(self)
        self.quit.hide()
        self.quit.text = 'Quit'
        self.restart = Begin(self)
        self.restart.hide()
        self.restart.text = 'Restart'
        self.upgrade1 = UpgradeDmg(self)
        self.upgrade2 = UpgradeDmg(self)
        self.upgrade2.text = "20 coins: Upgrade Dmg: lvl 2"
        self.upgrade3 = UpgradeDmg(self)
        self.upgrade3.text = "30 coins: Upgrade Dmg: lvl 3"
        self.upgrade4 = UpgradeDmg(self)
        self.upgrade4.text = "40 coins: Upgrade Dmg: lvl 4"
        self.maxDmg = simpleGe.Label()
        self.maxDmg.text = "Damage Maxed!"
        self.maxDmg.hide()
        
        self.sprites = [self.wall, self.maxDmg, self.upgrade4, self.upgrade3, self.upgrade2, self.upgrade1, self.restart, self.quit, self.begin, self.disBossHealth, self.boss, self.cannon, self.CBs, self.enemies, self.disMoney, self.disWallHealth, self.disWave]
        
    def update(self):
        if self.begin.clicked == True:
            self.begin.hide()
            self.background = pygame.image.load("MainBackGround.png")
            self.screen.blit(self.background, (0, 0))
            self.disMoney.center = 60,450
            self.disWallHealth.center = 320,300
            self.disWave.center = 580,450
            self.upgrade1.show((320,450))
            self.cannon.setPosition((320, 380))
            self.wall.setPosition((320,300))
            for enemies in self.enemies[:5]:
                enemies.reset()
                self.enemiesLeft += 1
            self.waveNum += 1
        
        self.disMoney.text = f"Money: {self.money}"
        self.disWallHealth.text = f"Health: {self.wallHealth}"
        self.disWave.text = f"Wave: {self.waveNum}"
        self.disBossHealth.text = f"Boss Health: {self.boss.health}"
        
        if self.money >= 10:
            if self.upgrade1.clicked == True:
                self.money -=10
                self.upgrade1.hide()
                self.upgrade2.show((320,450))
        if self.money >= 20:
            if self.upgrade2.clicked == True:
                self.money -=20
                self.upgrade2.hide()
                self.upgrade3.show((320,450))
        if self.money >= 30:
            if self.upgrade3.clicked == True:
                self.money -=30
                self.upgrade3.hide()
                self.upgrade4.show((320,450))
        if self.money >= 40:
            if self.upgrade4.clicked == True:
                self.money -=40
                self.upgrade4.hide()
                self.maxDmg.show((320,450))
        
        if self.wallHealth <= 0:
            self.background = pygame.image.load("LosingScreen.png")
            self.screen.blit(self.background, (0, 0))
            self.quit.show((300,200))
            self.boss.hide()
            for sprite in self.mainSprites:
                sprite.x = 999
                sprite.y = 999
                sprite.center = (999,999)
            self.wallHealth -= 1
        
        if self.enemiesLeft == 0:
            
            if self.waveNum == 1:
                self.waveNum += 1
                for enemies in self.enemies[:10]:
                    enemies.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 2:
                self.waveNum += 1
                
                for enemies in self.enemies[:5]:
                    enemies.setImage("Slime.png")
                    enemies.force = .15
                    enemies.dmg = .5
                    enemies.bounce = 5
                    enemies.value = 2
                    enemies.health = 3
                    
                for enemies in self.enemies[:15]:
                    enemies.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 3:
                self.waveNum += 1
                
                for enemies in self.enemies[:10]:
                    enemies.setImage("Slime.png")
                    enemies.force = .15
                    enemies.dmg = .5
                    enemies.bounce = 5
                    enemies.value = 2
                    enemies.health = 3
                    
                for enemies in self.enemies[:20]:
                    enemies.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 4:
                self.waveNum += 1
                
                for enemies in self.enemies[10:15]:
                    enemies.setImage("Heavy.png")
                    enemies.force = .01
                    enemies.dmg = 5
                    enemies.bounce = 1.5
                    enemies.value = 3
                    enemies.health = 15
                    
                for enemies in self.enemies[:25]:
                    enemies.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 5:
                self.waveNum += 1
                
                for enemies in self.enemies[10:20]:
                    enemies.setImage("Heavy.png")
                    enemies.force = .01
                    enemies.dmg = 5
                    enemies.bounce = 1.5
                    enemies.value = 3
                    enemies.health = 15
                    
                for enemies in self.enemies[:30]:
                    enemies.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 6:
                self.waveNum += 1 
                
                for enemies in self.enemies[5:20]:
                    enemies.setImage("Heavy.png")
                    enemies.force = .01
                    enemies.dmg = 5
                    enemies.bounce = 1.5
                    enemies.value = 3
                    enemies.health = 15
                    
                for enemies in self.enemies[:35]:
                    enemies.reset()
                    self.enemiesLeft += 1
                    
            elif self.waveNum == 7:
                self.waveNum += 1
                
                self.boss.reset()
                self.disBossHealth.center = 60,30
                
            elif self.waveNum == 8:
                if self.boss.health == 0:
                    self.background = pygame.image.load("WinningScreen.png")
                    self.screen.blit(self.background, (0, 0))
                    self.quit.show((300,200))
                    self.restart.show((300,300))
                    self.boss.hide()
                    for sprite in self.mainSprites:
                        sprite.x = 999
                        sprite.y = 999
                        sprite.center = (999,999)
                    self.boss.health -= 1
                
        if self.restart.clicked == True:
            self.money = 0
            self.waveNum = 0
            self.enemiesLeft = 0
            self.restart.center = 999,999
            self.background = pygame.image.load("MainBackGround.png")
            self.screen.blit(self.background, (0, 0))
            self.disMoney.center = 60,450
            self.disWallHealth.center = 320,300
            self.disWave.center = 580,450
            self.cannon.setPosition((320, 380))
            self.wall.setPosition((320,300))
            for enemies in self.enemies[:5]:
                enemies.reset()
                self.enemiesLeft += 1
            self.waveNum += 1
            
        if self.quit.clicked == True:
            self.stop()
        
    def doEvents(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.currentCB += 1
                if self.currentCB >= self.NUM_CB:
                    self.currentCB = 0
                self.CBs[self.currentCB].fire()
        
        
def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()