"""
Mystic Monsters AKA MM
has been produced by Jeremy Escobar
Goals:
develop the fighting mechanic (PRIORITY)
    -Monster
        -predetermined based off of player LVL if implimented
    -Player
    -Health
    -Attack
    -Defense
    -Magic
    -Block
    -Gold gained if implimented
    -EXP gained if implimented
    
    -Multi monster battle based on LVL if implimented
develop the menu(PRIORITY)
    -Venture to a dungeon
    -Check inventory
        -Equip
        -Items
        -Magic
    -Save Game
        -Save data such as player HP,MP,EXP,ITEMS,
    -Load Game
        -Display Game
    -Quit
develop the LVL System
    -decides the type of monster that player will be fighting.
    -decides the amount of HP and MP the player has.
    -Changes the item shop item stats based on the player lvl ie. instead of a lvl 1 potion, shops will show lvl 2 at a certain LVL
develop the items
    -Healing items
    -Mana Items
    -Armor
    -Weapons
    -Charms
develop the shop
    -Currency system based on gold
    
"""
import MMGE,os,time,json

def clear():
    #quick screen clear function
    os.system("cls")

def intro():
    #prints the intro of the game
    prompt = MMGE.getScript()
    MMGE.slowPrint(prompt,0.05)
    time.sleep(2)
    clear()
    MMGE.slowPrint("Welcome to Mystic Monsters!",0.1)
    time.sleep(1)
    input("Press ENTER to continue to main menu...")
    clear()

def create():
    #Creates items and adds them into their specific groupset and the main item dictionary
    #will crash if the wrong input not put in as this is a debug/developer feature
    keepGoing = True
    filetype = input("item groupset: ")
    try:
        inFile = open(f"assets\items\{filetype}_items.json", "r")
        items = json.load(inFile)
        inFile.close()
    except:
        items = {}
    num = 0
    while keepGoing:
        print(num)
        item = input("input item name: ")
        isEquipable = input("is it equipable(Y/N/S): ")
        isEquipable = isEquipable.upper()
        if isEquipable == "N":
            HP = int(input("HP gained: "))
            MP = int(input("MP gained: "))
            cost = int(input("cost: "))
            lvl = int(input("lvl: "))
            clear()
            items[item] = (isEquipable,HP,MP,cost,lvl)
        if isEquipable == "Y":
            permArmor = int(input("armor increased to: "))
            permAttack = int(input("attack increased to: "))
            cost = int(input("cost: "))
            lvl = int(input("lvl: "))
            items[item] = (isEquipable,permArmor,permAttack,cost,lvl)
            clear()
        if isEquipable == "S":
            damage = int(input("Spell damage: "))
            MPcost = int(input("MP cost: "))
            cost = int(input("cost: "))
            lvl = int(input("lvl: "))
            items[item] = (isEquipable,damage,MPcost,cost,lvl)
        if item == "":
            keepGoing = False
        num += 1
    if filetype != "":
        outFile = open(f"assets\items\{filetype}_items.json", "w")
        json.dump(items,outFile,indent=2)
        outFile.close()
    try:
        inFile = open(f"assets\items\items.json","r")
        current = dict(json.load(inFile))
        inFile.close()
    except:
        current = {}
    current.update(items)
    outFile = open("assets\items\items.json","w")
    json.dump(current,outFile,indent=2)
    outFile.close()
    
def editStat(self):
    #edits stats of the current hero directly
    #will crash if the wrong input not put in as this is a debug/developer feature
    keepGoing = True
    while keepGoing:
        print("char(name,maxHP,HP,armor,armName,weapon,maxMP,MP,magic,gold,XP,LVL,maxDamage,accuracy,backpack\n")
        print("If default value is an integer or string please input the same type used.\nInput as list format if called for ie '>>> item1,item2,item3")
        sel = input("\nType in a stat to edit\n\n>>> ")
        clear()
        if sel == "":
            keepGoing = False
            continue
        if sel == "name":
            print(f"    current({self.name})")
            self.name = input("\n>>> ")
        if sel == "maxHP":
            print(f"    current({self.maxHP})")
            self.maxHP = int(input("\n>>> "))
        if sel == "HP":
            print(f"    current({self.HP})")
            self.HP = int(input("\n>>> "))
        if sel == "armor":
            print(f"    current({self.armor})")
            self.armor = int(input("\n>>> "))
        if sel == "armName":
            print(f"    current({self.armName})")
            self.armName = input("\n>>> ")
        if sel == "weapon":
            print(f"    current({self.weapon})")
            self.weapon = input("\n>>> ")
        if sel == "maxMP":
            print(f"    current({self.maxMP})")
            self.maxMP = int(input("\n>>> "))
        if sel == "MP":
            print(f"    current({self.MP})")
            self.MP = int(input("\n>>> "))
        if sel == "gold":
            print(f"    current({self.gold})")
            self.gold = int(input("\n>>> "))
        if sel == "magic":
            print(f"    current({self.magic})")
            newValue = input("\n>>> ")
            self.magic = newValue.split(",")
        if sel == "XP":
            print(f"    current({self.XP})")
            self.XP = int(input("\n>>> "))
        if sel == "LVL":
            print(f"    current({self.LVL})")
            self.LVL = int(input("\n>>> "))
        if sel == "maxDamage":
            print(f"    current({self.maxDamage})")
            self.maxDamage = int(input("\n>>> "))
        if sel == "accuracy":
            print(f"    current({self.accuracy})")
            self.accuracy = int(input("\n>>> "))
        if sel == "backpack":
            print(f"    current({self.backpack})")
            newValue = input("\n>>> ")
            self.backpack = newValue.split(",")
        
def addMonster():
    #adds monsters to the main dictionary. based on LVL will determine where they show up
    #will crash if the wrong input not put in as this is a debug/developer feature
    keepGoing = True
    try:
        inFile = open("assets\monsters\monsters.json","r")
        MONSTERS = json.load(inFile)
        inFile.close()
    except:
        MONSTERS = {}
    while keepGoing:
        print(MONSTERS)
        name = input("Monster name: ")
        if name == "":
            keepGoing = False
            continue
        HP = int(input("Max HP threshold: "))
        LVL = int(input("LVL: "))
        Max = int(input("Max damage threshold: "))
        accuracy = int(input("Accuracy: "))
        armor = int(input("Armor threshold: "))
        disable = input("Disable flee Y/N: ")
        disable = disable.upper()
        MONSTERS[name] = (HP,LVL,Max,accuracy,armor,disable)
        clear()
    outFile = open("assets\monsters\monsters.json","w")
    json.dump(MONSTERS,outFile,indent=2)
    outFile.close()

    
def debug(self):
    #the debug menu.. super secret developer stuff & jargon
    #to get here, type '63' in the main menu instead of the options shown
    keepGoing = True
    while keepGoing:
        print("Welcome to the debug menu")
        sel = MMGE.menu(["Create New town(not Implimented)","Create new items","Adjust stats","Add Monsters"])
        if sel == 0:
            pass
        if sel == 1:
            create()
        if sel == 2:
            editStat(self)
        if sel ==3:
            addMonster()
        if sel == "":
            keepGoing = False
        clear()

def main():
    #DA MAIN MENU!!
    intro()
    keepGoing = True
    hero = MMGE.char()
    mainMenu = ["Quit", "Play Game", "Load a save file"]
    while keepGoing:
        print("\n   Main Menu")
        sel = MMGE.menu(mainMenu)
        if sel == 0:
            keepGoing = False
        elif sel == 1:
            MMGE.play(hero)
        elif sel == 2:
            hero = MMGE.load()
        elif sel == 63:
            debug(hero)
        else:
            print("Invalid Selection")


if __name__ == "__main__":
    main()