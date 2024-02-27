# -*- coding: utf-8 -*-
"""
Store Simulator - Carter Leckron

In this "game" you must solve the "puzzle" or else meet your doom...that being
purchasing groceries. This project has undergone several versions, and sadly
I wasn't able to add nearly as much as I wanted. With that being said, what is
here I am still proud of, and I hope you enjoy. Also, for descriptions and thought
processes on lines of code, check the comments and the README.

Also, yes I chose beans to be the placeholder image, and yes, beans.png is still
kind of funny to me.
"""

#importing the three major programs
import simpleGE, pygame, random

#node class gets information from the NodeList which is setup in the main function
#data is setup into maptitle and images, self explanatory, the name of the current area and the image associated with it
#hotspot data gives the name of the hotspot, the locations and sizes of the hotspot, and the indexes which will be used to call the next node
class Node(object):
    def __init__(self,mapTitle,mapImage,option1Name,option1Hotspot,option1Index,option2Name,option2Hotspot,option2Index,option3Name,option3Hotspot,option3Index):
        self.mapTitle = mapTitle
        self.mapImage = mapImage
        
        self.option1Name = option1Name
        self.option1Hotspot = option1Hotspot
        self.option1Index = option1Index
        
        self.option2Name = option2Name
        self.option2Hotspot = option2Hotspot
        self.option2Index = option2Index
        
        self.option3Name = option3Name
        self.option3Hotspot = option3Hotspot
        self.option3Index = option3Index
        
#game class sets up each of the sprites and handles most of the "game"
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        #Setting the basic scene information
        self.background = pygame.image.load("background-exterior-front.png")
        self.background = pygame.transform.scale(self.background,(640,480))
        self.setCaption("Store Simulator - An Accurate Retail Experience")
        #Important information for items, these lists are connected to the nodes through the indexes, data stored in each of these is pulled in the PlaceItems function
        self.itemNameList = [["Car","Cashier"],["Cashier","Key"],["Empty","Empty"],["Beans","Cereal"],["Empty","Empty"],["Empty","Empty"],["Egg","Empty"],["Egg","Empty"],["Cashier","Key"],["Cashier","Key"],["Empty","Empty"],["Empty","Empty"],["Empty","Empty"]]
        self.itemImageList = [["car-item.png","cashier-car.png"],["cashier-register.png","key-item.png"],["beans.png","beans.png"],["beans.png","cereal-item.png"],["beans.png","beans.png"],["beans.png","beans.png"],["egg-carton-item.png","beans.png"],["beans.png","beans.png"],["cashier-register.png","key-item.png"],["cashier-register.png","key-item.png"],["beans.png","beans.png"],["beans.png","beans.png"],["beans.png","beans.png"]]
        self.itemPositionList =[[[380,390,200,130],[680,520,10,10]],[[180,172,100,150],[120,155,20,40]],[[680,520,10,10],[680,520,10,10]],[[250,90,65,87],[495,183,65,85]],[[680,520,10,10],[680,520,10,10]],[[260,10,45,80],[680,520,10,10]],[[100,65,95,45],[680,520,10,10]],[[680,520,10,10],[680,520,10,10]],[[180,172,100,150],[120,155,20,40]],[[180,172,100,150],[120,155,20,40]],[[680,520,10,10],[680,520,10,10]],[[680,520,10,10],[680,520,10,10]],[[680,520,10,10],[680,520,10,10]]]
        self.itemInteractableList = [["Clickable","Clickable"],["Clickable","Clickable"],["Pickup","Pickup"],["Pickup","Pickup"],["Empty","Empty"],["Empty","Empty"],["Pickup","Empty"],["Empty","Empty"],["Empty","Empty"],["Empty","Empty"],["Empty","Empty"],["Empty","Empty"],["Empty","Empty"]]
        self.itemInInventory = "None"
        #Click description label defining, setting the font and creating the sprite
        self.lblClickDescription = simpleGE.Label()
        self.lblClickDescription.center = (0,0)
        self.lblClickDescription.size = (70,20)
        self.lblClickDescription.font = pygame.font.Font("Bangers-Regular.ttf", 12)
        self.lblClickDescription.hide()
        #Interaction text, essentially working as the character's textboxes
        self.lblInteractionText = simpleGE.Label()
        self.lblInteractionText.center = (430,340)
        self.lblInteractionText.size = (250,20)
        self.lblInteractionText.font = pygame.font.Font("Bangers-Regular.ttf", 12)
        self.lblInteractionText.hide()
        
        self.carEgged = False
        #Creating the hotspots using the hotspot class
        self.hotSpot1 = Hotspot(self)
        self.hotSpot2 = Hotspot(self)
        self.hotSpot3 = Hotspot(self)
        #Creating the items using the item class
        self.item1 = Item(self)
        self.item2 = Item(self)
        #Creating the list U.I element
        self.list = List(self)
        #Setting the background, so that the background can actually change images without breaking
        self.backGround = BackGround(self)
        
        self.sprites = [self.backGround,self.list,self.hotSpot1,self.hotSpot2,self.hotSpot3,self.item1,self.item2,self.lblClickDescription,self.lblInteractionText]
        
    def LoadNode (self,node):
        #taking information from the node class and assigning them to variables
        self.hotSpot1Name = node.option1Name
        self.hotSpot2Name = node.option2Name
        self.hotSpot3Name = node.option3Name
        #Variables are then used to give information on where the hotspots should be located in each node
        self.hotSpot1.givePosition((node.option1Hotspot[0],node.option1Hotspot[1]))
        self.hotSpot1.setSize(node.option1Hotspot[2],node.option1Hotspot[3])
        
        self.hotSpot2.givePosition((node.option2Hotspot[0],node.option2Hotspot[1]))
        self.hotSpot2.setSize(node.option2Hotspot[2],node.option2Hotspot[3])
        
        self.hotSpot3.givePosition((node.option3Hotspot[0],node.option3Hotspot[1]))
        self.hotSpot3.setSize(node.option3Hotspot[2],node.option3Hotspot[3])
        #Defining the index which is used to determine the next nod when clicked on
        self.hotspot1Index = node.option1Index
        self.hotspot2Index = node.option2Index
        self.hotspot3Index = node.option3Index
        #Determining which image should be placed on the background
        self.mapImage = node.mapImage
        #If the key is in the player's inventory, hotspot two is removed so the door can be interacted with.
        if self.itemInInventory == "Key":
            if self.hotSpot2Name == "Locked Door":
                self.hotSpot2.givePosition([680,520,10,10])
                self.list.hide()
        
    def PlaceItems (self,index):
        #Getting the lists from the main variables
        self.itemNames = self.itemNameList[index]
        self.itemImages = self.itemImageList[index]
        self.itemPositions = self.itemPositionList[index]
        self.itemInteractable = self.itemInteractableList[index]
        #Assigning the data from the lists to item sprites, so they are placed in the correct areas
        #Includes a check to see if item is in inventory, if so, the item is placed outside the screen area
        if self.itemNames[0] == self.itemInInventory:
            self.item1.LoadImage("Offscreen","beans.png",[680,520,10,10])
        else:    
            self.item1.LoadImage(self.itemNames[0], self.itemImages[0], self.itemPositions[0])
            
        if self.itemNames[1] == self.itemInInventory:
            self.item2.LoadImage("Offscreen","beans.png",[680,520,10,10])
        else:    
            self.item2.LoadImage(self.itemNames[1], self.itemImages[1], self.itemPositions[1])     
        
        #Check to see if the egg item has been used on the car. If so, load alternate sprite locations
        if self.carEgged == True:
            if index == 0:
                self.item1.LoadImage("Car","egged-car-item.png",[380,390,200,130])
                self.item2.LoadImage("Cashier","cashier-car.png",[90,420,70,160])
            elif index == 1:
                self.item1.LoadImage("Offscreen","beans.png",[680,520,10,10])

        
    def update(self): 
        #updating to get mouse location for hotspots
        mouseXY= pygame.mouse.get_pos()
        #basic mouse interaction with node triggers. When moused over, sets text to hotspot name
        if self.hotSpot1.rect.collidepoint(mouseXY):
            self.lblClickDescription.center = (mouseXY[0]+45,mouseXY[1]-8)
            self.lblClickDescription.text = (self.hotSpot1Name)
            if self.hotSpot1.clickedOn:
                self.PlaceItems(self.hotspot1Index)
                self.LoadNode(self.nodeList[(self.hotspot1Index)])
                self.backGround.updateBG(self.mapImage)
        elif self.hotSpot2.rect.collidepoint(mouseXY):
            self.lblClickDescription.center = (mouseXY[0]+45,mouseXY[1]-8)
            self.lblClickDescription.text = (self.hotSpot2Name)
            if self.hotSpot2.clickedOn:
                self.PlaceItems(self.hotspot2Index)
                self.LoadNode(self.nodeList[(self.hotspot2Index)])
                self.backGround.updateBG(self.mapImage)
        elif self.hotSpot3.rect.collidepoint(mouseXY):
            self.lblClickDescription.center = (mouseXY[0]+45,mouseXY[1]-8)
            self.lblClickDescription.text = (self.hotSpot3Name)
            if self.hotSpot3.clickedOn:
                self.PlaceItems(self.hotspot3Index)
                self.LoadNode(self.nodeList[(self.hotspot3Index)])
                self.backGround.updateBG(self.mapImage)
        else:
            self.lblClickDescription.hide()
        #mouse interaction with items
        #Also includes code to determine if an item is a pickup or interactable.
        if self.item1.rect.collidepoint(mouseXY):
            self.lblClickDescription.center = (mouseXY[0]+45,mouseXY[1]-8)
            self.lblClickDescription.text = (self.item1.itemValue)
            if self.item1.clicked:
                if self.itemInteractable[0] == "Pickup":
                    if self.itemInInventory == "None":
                        self.itemInInventory = self.itemNames[0]
                        self.item1.hide()
                        self.item1.clicked = False
                    else:
                        self.lblClickDescription.text = "Inventory Full!"
                elif self.itemInteractable[0] == "Clickable":
                    self.item1.ClickableActions()
                    self.lblInteractionText.text = self.item1.currentLine
                    self.lblInteractionText.center = (self.item1.centerValue[0],self.item1.centerValue[1])
                    self.item1.clicked = False
                    #line below included so that  text appears when hovering over item2
        elif self.item2.rect.collidepoint(mouseXY) != True:
            self.lblInteractionText.hide()
        
        if self.item2.rect.collidepoint(mouseXY):
            self.lblClickDescription.center = (mouseXY[0]+45,mouseXY[1]-8)
            self.lblClickDescription.text = (self.item2.itemValue)    
            if self.item2.clicked:
                if self.itemInteractable[1] == "Pickup":
                    if self.itemInInventory == "None":
                        self.itemInInventory = self.itemNames[1]
                        self.item2.hide()
                    else:
                        self.lblClickDescription.text = "Inventory Full!"
                elif self.itemInteractable[1] == "Clickable":
                    self.item2.ClickableActions()
                    self.lblInteractionText.text = self.item2.currentLine
                    self.lblInteractionText.center = (self.item2.centerValue[0],self.item2.centerValue[1])
                    self.item2.clicked = False 
#item class, fairly standard with some unique functions
class Item(simpleGE.BasicSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.x = 680
        self.y = 520
        self.setImage("beans.png")
        self.itemValue = "None"
        self.activated = False
        self.clicked = False
    #Load image function, takes information from PlaceItem and applies it to the sprite
    def LoadImage(self,itemName,imageFile,location):
        self.itemValue = itemName
        self.setImage(imageFile)
        self.x = location[0]
        self.y = location[1]
        self.setSize(location[2],location[3])
        self.rect = self.image.get_rect()
    #Check events used to determine if mouse interaction is taking place 
    def checkEvents (self):
        self.clickedOn = False
        if pygame.mouse.get_pressed() == (1,0,0):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.activated = True
        if self.activated == True:
            if pygame.mouse.get_pressed() == (0,0,0):
                self.activated = False
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True
    #Clickable actions determine what the item should do if it can be clicked on multiple times
    def ClickableActions(self):
        #Defining the variables and lists used for the function
        self.carLines = ["This is the cashier's car.","Splat","The car has egg all over it!"]
        self.cashierLines = ["Welcome to Generic Mart.","If you need to check out, just bring an item here.","I swear, this job is so boring sometimes.","Are you actually going to buy anything?","You see that car out there? That's my pride and joy.","So uh...how about that weather.","No way, you aren't touching this key.","There you go, you should be checked out now.","Hey, give me my keys back!", "MY CAR! NOOOOOOOOOOOOOO!", "WHY! IT WAS THE ONE THING I LIKED.","HOW COULD YOU?!"]
        self.currentLine = ""
        self.centerValue = [0,0]
        #Determine lines for the car sprite depending on what items the player has
        if self.itemValue == "Car":
            if self.scene.itemInInventory == "Egg":
                self.scene.carEgged = True
                self.scene.itemInInventory = "None"
                self.scene.PlaceItems(0)
                self.currentLine = self.carLines[1]
                self.centerValue = [430,340]
                
            elif self.scene.carEgged == True:
                self.currentLine = self.carLines[2]
                self.centerValue = [430,340]
            else:
                self.centerValue = [430,340]
                self.currentLine = self.carLines[0]
        #Determine the cashier's lines based both on what the player has done, and random chance
        if self.itemValue == "Cashier":
            if self.scene.itemInInventory == "Key":
                self.currentLine = self.cashierLines[8]
                self.centerValue = [200,190]
            elif self.scene.itemInInventory == "Egg":
                self.currentLine = self.cashierLines[7]
                self.centerValue = [200,190]
            elif self.scene.carEgged == True:
                self.currentLine = self.cashierLines[random.randint(9,11)]
                self.centerValue = [400,320]
            elif self.scene.itemInInventory != "None":
                self.currentLine = self.cashierLines[7]
                self.centerValue = [200,190]
                if self.scene.itemInInventory == self.scene.list.correctItem:
                    self.scene.LoadNode(self.scene.nodeList[8])
                    self.scene.list.hide()
                else:
                    self.scene.LoadNode(self.scene.nodeList[9])
                    self.scene.list.hide()
            else:
                self.currentLine = self.cashierLines[random.randint(0,5)]
                self.centerValue = [200,190]
        #Makes sure the player cannot click on the key unless the puzzle is completed.    
        if self.itemValue == "Key":
            if self.scene.carEgged == True:
               self.scene.item2.hide() 
               self.scene.itemInInventory = "Key"
               self.scene.carEgged = False
            else:
                self.currentLine = self.cashierLines[6]
                self.centerValue = [200,190]
                
class BackGround(simpleGE.BasicSprite):
    #Sets the background depending on what image it recieves in updateBG
    def __init__(self,scene):
        super().__init__(scene)
        self.setImage("background-exterior-front.png")
        self.setSize(640,480)
        self.x = 320
        self.y = 240
    def updateBG(self,image):
        self.setImage(image)
        self.setSize(640,480)
        self.x= 320
        self.y = 240
    #Hotspot class is transparent, used to navigate the map. Determines if it is clicked on using check events
class Hotspot(simpleGE.BasicSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.image = pygame.Surface((100,100), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255,255,255,0))
        self.rect = self.image.get_rect()
        self.activated = False
        self.clickedOn = False
        
    def checkEvents (self):
        self.clickedOn = False
        if pygame.mouse.get_pressed() == (1,0,0):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.activated = True
        if self.activated == True:
            if pygame.mouse.get_pressed() == (0,0,0):
                self.activated = False
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clickedOn = True
        
    def givePosition(self,position):
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
#List is very simple, basic image with light randomization
class List(simpleGE.BasicSprite):
    def __init__(self,scene):
        super().__init__(scene)
        self.whichItem = random.randint(0, 1)
        if self.whichItem == 0:
            self.setImage("shopping-list-beans.png")
            self.correctItem = "Beans"
        else:
            self.setImage("shopping-list-cereal.png")
            self.correctItem = "Cereal"
        self.x = 600
        self.y = 430
        
def main():
    nodeList = []
    #Area 0
    nodeList.append(Node(
    "Store Front", "background-exterior-front.png",
    "Cash Register",[159,315,114,135], 1,
    "Back Alley", [580,300,114,165],2,
    "Offscreen",[680,520,10,10],0))
    #Area 1
    nodeList.append(Node(
    "Main Entrance","background-cash-register.png",
    "Store Front",[320,440,340,100], 0,
    "General Goods",[470,150,230,225],3,
    "Offscreen",[680,520,10,10],0))
    #Area 2
    nodeList.append(Node(
    "Back Alley", "background-exterior-side.png",
    "Store Front",[25,400,200,150], 0,
    "Offscreen",[680,520,10,10],0,
    "Offscreen",[680,520,10,10],0))
    #Area 3
    nodeList.append(Node(
    "General Goods","background-main-shopping-area.png",
    "Main Entrance",[320,440,340,100], 1,
    "Bulletin Board",[600,305,120,150],4,
    "Frozen Foods",[125,150,135,230],6))
    #Area 4
    nodeList.append(Node(
    "Bulletin Board","background-bulletinboard.png",
    "General Goods",[25,400,200,150], 3,
    "Locked Door",[515,235,120,225],4,
    "Locked Door",[515,235,120,225],4))
    #Area 5
    nodeList.append(Node(
    "Bulletin Board","background-bulletinboard.png",
    "General Goods",[25,400,200,150], 3,
    "Locked Door",[515,235,120,225],4,
    "Employee Lounge",[515,235,120,225],5))
    #Area 6 
    nodeList.append(Node(
    "Frozen Foods","background-frozen-section.png",
    "General Goods",[320,440,340,100], 3,
    "Office Entrance",[600,305,120,150],7,
    "Offscreen",[680,520,10,10],0))
    #Area 7
    nodeList.append(Node(
    "Office Entrance","background-office-entrance.png",
    "Frozen Foods",[25,400,200,150], 6,
    "Locked Door",[455,235,120,225],7,
    "Unknown Area",[455,235,120,225],12))
    #Area 8 - Boring Ending
    nodeList.append(Node(
    "Regular Ending Variant","background-cash-register.png",
    "Go Home",[320,440,340,100], 10,
    "Offscreen",[680,520,10,10],3,
    "Offscreen",[680,520,10,10],0))
    #Area 9 - Bad Ending
    nodeList.append(Node(
    "Regular Ending Variant","background-cash-register.png",
    "Go Home",[320,440,340,100],11,
    "Offscreen",[680,520,10,10],3,
    "Offscreen",[680,520,10,10],0))
    #Area 10 - Boring Ending Screen
    nodeList.append(Node(
    "Regular Ending Variant","background-boring-ending.png",
    "Offscreen",[680,520,10,10], 9,
    "Offscreen",[680,520,10,10],3,
    "Offscreen",[680,520,10,10],0))
    #Area 11 = Bad Ending Screen
    nodeList.append(Node(
    "Regular Ending Variant","background-bad-ending.png",
    "Offscreen",[680,520,10,10], 9,
    "Offscreen",[680,520,10,10],3,
    "Offscreen",[680,520,10,10],0))
    #Area 12 - True Ending Screen
    nodeList.append(Node(
    "Regular Ending Variant","background-true-ending.png",
    "Offscreen",[680,520,10,10], 9,
    "Offscreen",[680,520,10,10],3,
    "Offscreen",[680,520,10,10],0))
    game = Game()
    game.nodeList = nodeList
    game.LoadNode(nodeList[0])
    game.PlaceItems(0)
    game.start()

    
if __name__ == "__main__":
    main()
    