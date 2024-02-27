"""
MMGE has been produced by Jeremy Escobar
"""
import sys,os,time,json,random

def clear():
    #quick screen clear function
    os.system("cls")

class char(object):
    def __init__(self,name="default",maxHP=20,HP=20,armor=1,armName="stained cloth",weapon="fists",maxMP=5,MP=5,magic=[],
                 gold=0,XP=0,LVL=1,maxDamage=5,accuracy=85,backpack=[]):
        #char(name,maxHP,HP,armor,armName,weapon,maxMP,MP,magic,gold,XP,LVL,maxDamage,accuracy,backpack)
        #main character class
        self.name = name
        self.maxHP = maxHP
        self.HP = HP
        self.armor = armor
        self.armName = armName
        self.weapon = weapon
        self.maxMP = maxMP
        self.MP = MP
        self.magic = magic
        self.gold = gold
        self.XP = XP
        self.LVL = LVL
        self.maxDamage = maxDamage
        self.accuracy = accuracy
        self.backpack = backpack

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def maxHP(self):
        return self.__maxHP
    @maxHP.setter
    def maxHP(self,value):
        self.__maxHP = value
    @property
    def HP(self):
        return self.__HP
    @HP.setter
    def HP(self,value):
        #defining limits to HP
        if value < 0:
            value = 0
        else:
            self.__HP = value
        if self.__HP > self.__maxHP:
            self.__HP = self.__maxHP
        if type(value) == float:
            value = int(round(value))
            self.__HP = value
    @property
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self,value):
        self.__armor = value
    @property
    def armName(self):
        return self.__armName
    @armName.setter
    def armName(self,value):
        self.__armName = value
    @property
    def weapon(self):
        return self.__weapon
    @weapon.setter
    def weapon(self,value):
        self.__weapon = value
    @property
    def maxMP(self):
        return self.__maxMP
    @maxMP.setter
    def maxMP(self,value):
        self.__maxMP = value
    @property
    def MP(self):
        return self.__MP
    @MP.setter
    def MP(self,value):
        #defining limits to MP
        self.__MP = value
        if self.__MP > self.__maxMP:
            self.__MP = self.__maxMP
        if self.__MP < 0:
            self.__MP = 0
    @property
    def magic(self):
        return self.__magic
    @magic.setter
    def magic(self,value):
        self.__magic = value
    @property
    def gold(self):
        return self.__gold
    @gold.setter
    def gold(self,value):
        self.__gold = value
    @property
    def XP(self):
        return self.__XP
    @XP.setter
    def XP(self,value):
        self.__XP = value
    @property
    def LVL(self):
        return self.__LVL
    @LVL.setter
    def LVL(self,value):
        self.__LVL = value
    @property
    def maxDamage(self):
        return self.__maxDamage
    @maxDamage.setter
    def maxDamage(self,value):
        self.__maxDamage = value
    @property
    def accuracy(self):
        return self.__accuracy
    @accuracy.setter
    def accuracy(self,value):
        self.__accuracy = value
    @property
    def backpack(self):
        return self.__backpack
    @backpack.setter
    def backpack(self,value):
        self.__backpack = value

class monsterChar(object):
    def __init__(self,name="Gooner",maxHP=10,HP=10,LVL=1,maxDamage=5,accuracy=70,armor=0,fleeDisabled="N"):
        #Standard monster 
        super().__init__()
        self.name = name
        self.maxHP = maxHP
        self.HP = HP
        self.LVL = LVL
        self.maxDamage = maxDamage
        self.accuracy = accuracy
        self.armor = armor
        self.fleeDisabled = fleeDisabled

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def maxHP(self):
        return self.__maxHP
    @maxHP.setter
    def maxHP(self,value):
        self.__maxHP = value
    @property
    def HP(self):
        return self.__HP
    @HP.setter
    def HP(self,value):
        self.__HP = value
    @property
    def LVL(self):
        return self.__LVL
    @LVL.setter
    def LVL(self,value):
        self.__LVL = value
    @property
    def maxDamage(self):
        return self.__maxDamage
    @maxDamage.setter
    def maxDamage(self,value):
        self.__maxDamage = value
    @property
    def accuracy(self):
        return self.__accuracy
    @accuracy.setter
    def accuracy(self,value):
        self.__accuracy = value
    @property
    def armor(self):
        return self.__armor
    @armor.setter
    def armor(self,value):
        self.__armor = value
    @property
    def fleeDisabled(self):
        return self.__fleeDisabled
    @fleeDisabled.setter
    def fleeDisabled(self,value):
        self.__fleeDisabled = value
        
def slowPrint(text,speed):
    #text variable is what you want to be printed out and speed variable is how fast in seconds each letter will appear
    if speed != 0:
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(speed)
        print()
   
def getScript():
    #getting the script for the intro to the game
    try:
        inFile = open("assets\prompts.txt", "r")
        prompt = ""
        for line in inFile:
            line.strip()
            prompt += line

        return prompt
    except:
        return "You broke it >:("
    
def new():
    #gives the char class a name that isn't "" default or DEFAULT
    keepGoing = True
    while keepGoing:
        print("Name your hero")
        name = input(">>> ")
        clear()
        if name in ("","default","DEFAULT"):
            print("Please select a different name")
        else:
            keepGoing = False
            return name

def menu(CONTS):
    #this takes the content of a list or dictionary and displays it with a number. an input attempts to become an int but will return blank string if the input cannot become an integer
    print()
    for id,CONT in enumerate(CONTS):
        print(f"    {id}) {CONT}")
    try:
        sel = int(input("\n>>> "))
        clear()
    except:
        sel = ""
        clear()
    return sel

def progressBar(self,type):
    #displays a progress bar depending on the bar type
    maxDashes = 20
    if type == "HP":
        maxType = self.maxHP
        barType = self.HP
    elif type == "MP":
        maxType = self.maxMP
        barType = self.MP
    dashConvert = maxType/maxDashes
    currentDashes = int(barType/dashConvert)
    remainingType = maxDashes - currentDashes

    typeDisplay = "+" * currentDashes
    remainingDisplay = "-" * remainingType

    print("\n"+self.name,type+":")
    print(f"    {type} Remaining: |{typeDisplay} {remainingDisplay}|  {barType}/{maxType}")

def venture(hero):
    #determines whether hero will encounter a monster
    enChance = random.randrange(0,100)
    print("Wandering around")
    slowPrint("...",1)
    if enChance <= 80:
        op = getMonster(hero)
        battle(hero,op)
    else:
        print(f"\n{hero.name} felt bored and returned to town.")

def getMonster(self):
    #gets a dictionary of monsters and randomly select one from the dictionary
    inFile = open("assets\monsters\monsters.json","r")
    MONSTERS = json.load(inFile)
    inFile.close()
    potMonsters = []
    crit = monsterChar()
    lowLvl = self.LVL - 10
    highLvl = self.LVL + 2
    for monster in MONSTERS:
        if MONSTERS[monster][1] in range(lowLvl,highLvl):
            potMonsters.append(monster)
    chance = random.randrange(0,len(potMonsters))
    for num,monName in enumerate(potMonsters):
        for monster in MONSTERS:
            if chance == num:
                if monster == monName:
                    crit.name = monster
                    crit.maxHP = MONSTERS[monster][0]
                    crit.HP = crit.maxHP
                    crit.LVL = MONSTERS[monster][1]
                    crit.maxDamage = MONSTERS[monster][2]
                    crit.accuracy = MONSTERS[monster][3]
                    crit.armor = MONSTERS[monster][4]
                    crit.fleeDisabled = MONSTERS[monster][5]
    return crit
    
def battle(hero,op):
    #Main battle menu that show health and options available
    keepGoing = True
    if op.fleeDisabled == "Y":
        fleeDisabled = True
    else:
        fleeDisabled = False
    initDefense = hero.armor
    opinitDefence = op.armor
    print(f"\n{hero.name} encountered {op.name} while walking aimlessly")
    while keepGoing:
        skip = ""
        op.armor = opinitDefence
        hero.armor = initDefense
        opsel = random.randint(0,100)
        progressBar(hero,"HP")
        progressBar(hero,"MP")
        progressBar(op,"HP")
        print("\n    What will you do?")
        battleMenu = ["Flee","Attack","Magic","Defend","Item"]
        sel = menu(battleMenu)
        
        if sel == 1:
            if opsel > 85:
                defend(op)
            attack(hero,op,.8)
        elif sel == 2:
            skip = magic(hero,op)
            if skip:
                continue
        elif sel == 3:
            defend(hero)
            print(hero.name,"defended this turn")
            time.sleep(1)
        elif sel == 4:
            skip = item(hero)
            if skip:
                continue
        elif sel == 0:
            print("attempting to flee")
            slowPrint("...",.6)
            fleeChance = random.randrange(0,100)
            if fleeDisabled != True:
                if fleeChance <= 50:
                    print("You've fled this battle")
                    keepGoing = False
                    continue
                else:
                    print("you've tripped and fell onto the dirt")
            else:
                print("You cannot flee from this battle")
                continue
        else:
            clear()
        #checks hp values to determine when to end the battle
        if op.HP != 0:
            if opsel < 85:
                attack(op,hero,0)
            else:
                print(op.name,"defended this turn")
                time.sleep(1)
        if hero.HP <= 0:
            keepGoing = False
            print(f"{hero.name} passed out from lack of health")
            time.sleep(2), clear()
            found(hero)
        elif op.HP <= 0:
            print(f"{hero.name} won this battle!")
            keepGoing = False
            gainXP(hero,op)
            gainGold(hero,op)

    check(hero)
    input("\npress ENTER to continue")
    clear()
        
def attack(self,char,ti):
    #attack sequence for opponent
    hitSuccess = random.randrange(0,100)
    damageAmount = random.randrange(1,self.maxDamage) - char.armor
    if damageAmount < 0:
        damageAmount = 0
    
    slowPrint("...",ti)
    if hitSuccess <= self.accuracy:
        if damageAmount != 0:
            print(f"{self.name} hit {char.name} for {damageAmount} HP!")
        else:
            print(f"{char.name} was not affected by {self.name}'s attack")
        if damageAmount > (self.maxDamage-2):
            print("Critical Hit!")
        if char.HP <= damageAmount:
            char.HP = 0
        char.HP -= damageAmount
    else:
        print(f"{self.name} tripped over their confidence and landed face first into the dirt")

def defend(self):
    #defend sequence.. planning to add more varaibles that determine defence
    self.armor += 5

def magic(self,op):
    #magic menu that uses magic that is in the hero's magic class variable. will not work without a spellbook present
    keepGoing = True
    if "Spellbook" not in self.magic:
        keepGoing = False
        print("You are lacking a spellbook!")
        return True
    inFile = open("assets\items\items.json","r")
    ITEMS = json.load(inFile)
    inFile.close()
    spells = self.magic
    spells.remove("Spellbook")
    while keepGoing:
        print("Select a spell to cast!\n")
        for count,spell in enumerate(spells):
            for i in ITEMS:
                if i == spell:
                    print(f"    {count}) {spell}    Cost {ITEMS[i][2]} MP")
        try:
            sel = int(input("\n>>> "))
            clear()
        except:
            sel = ""
            clear()
        num = 0
        if sel == "":
            keepGoing = False
            spells.append("Spellbook")
            return True
        for spell in spells:
            if sel == num:
                print(f"{self.name} attempts to casts {spell}")
                for i in ITEMS:
                    if spell == i:
                        if ITEMS[i][2] > self.MP:
                            print("you do not have enough MP to cast this spell!")
                        elif ITEMS[i][1] < 0:
                            slowPrint("...",.8)
                            #healing type spells
                            healing = ITEMS[i][1] * -1
                            print(f"{self.name} heals for {healing} HP!")
                            self.HP += healing
                            self.MP -= ITEMS[i][2]
                            keepGoing = False
                            spells.append("Spellbook")
                            continue
                        else:
                            #damage spells
                            slowPrint("...",.8)
                            print(f"{self.name}'s {spell} did {ITEMS[i][1]} damage on {op.name}!")
                            op.HP -= ITEMS[i][1]
                            self.MP -= ITEMS[i][2]
                            keepGoing = False
                            spells.append("Spellbook")
                            continue
            num += 1

def item(self):
    #Menu to use items in the battle sequence
    print("\nSelect an Item to use or press ENTER to return back to previous screen")
    sel = menu(self.backpack)
    if type(sel) == int:
        selNum = 0
        for item in self.backpack:
            if sel == selNum:
                useItem(self,item)
            selNum += 1
    else:
        skip = True
        return skip
    
def gainXP(hero,op):
    #based on opponent level, determines how much xp is gained
    xpGained = random.randrange(1,(op.LVL*2))
    print(f"You Gained {xpGained} XP!")
    hero.XP += xpGained

def gainGold(hero,op):
    #based on opponent level, determines how much gold is gained
    minGold = 2*op.LVL
    maxGold = 5*op.LVL
    goldGained = random.randrange(minGold,maxGold)
    hero.gold += goldGained
    print(f"you Gained {goldGained} Gold!")

def check(hero):
    #checks the current amount of XP of the hero and increases LVL, HP, and MP
    lvlCheck = 2*(2**hero.LVL)
    if lvlCheck <= hero.XP:
        hero.LVL += 1
        hero.maxHP += 3
        hero.maxMP += 3
        hero.HP = hero.maxHP
        hero.MP = hero.maxMP
        print("Level up!")
        print("HP and MP has been increased!")

def found(self):
    #death sequence if hero hp falls below 1
    print("The town's inn keeper found you on the ground while they were doing their normal stroll"), time.sleep(3), clear()
    print("Inn Keeper: "), slowPrint("Oh you're finally awake..", .05)
    input("\n press <ENTER> to continue"), clear()
    print("Inn Keeper: "), slowPrint("I dragged you here and took care of you for a few days while you recovered.", .05)
    input("\n press <ENTER> to continue"), clear()
    print("Inn Keeper: "), slowPrint("You can be on your way & I'll just take 25 gold in exchange for rescuing your life.",.05)
    input("\n press <ENTER> to continue"), clear()
    print(f"{self.name} paid the Inn Keeper 25 gold")
    self.gold -= 25
    self.HP += 10

def load():
    #loads a save file that contains dictionary values in json format
    saves = os.listdir("assets\saves")
    print("select a save to load")
    for num,save in enumerate(saves):
        dispsave = save.replace(".json","")
        print(f"   {num}) {dispsave}")
    try:
        sel = int(input("\n>>> "))
        for num,save in enumerate(saves):
            if sel == num:
                inFile = open(f"assets\saves\{save}", "r")
                loadSave = json.load(inFile)
                for items in loadSave.values():
                    stat = items
                for items in loadSave.keys():
                    heroName = items
                hero = char(heroName,stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],stat[6],stat[7],stat[8],stat[9],stat[10],stat[11],stat[12],stat[13])
                clear()
                print("Save loaded successfully")
                return hero
    except:
        clear()
        print("That was not a valid option!")
        hero = char()
        return hero
    
def save(self):
    #saves a new file containing a dictionary in json format
    NEWSAVE = {}
    saves = os.listdir("assets\saves")
    saves.append("new")
    NEWSAVE[self.name] = (self.maxHP,self.HP,self.armor,self.armName,self.weapon,self.maxMP,self.MP,self.magic,self.gold,
                          self.XP,self.LVL,self.maxDamage,self.accuracy,self.backpack)
    print("select a file to save to")
    sel = menu(saves)
    for num,item in enumerate(saves):
        if sel == num:
            outFile = open(f"assets\saves\{self.name}.json","w")
            json.dump(NEWSAVE,outFile,indent=2)
            outFile.close()

def checkInventory(char):
    #displpays stats of the hero and what is in the backpack variable
    keepGoing = True
    lvlCheck = 2*(2**char.LVL)
    while keepGoing:
        progressBar(char,"HP")
        progressBar(char,"MP")
        print(f"""
    Level: {char.LVL}
    XP til next LVL: {lvlCheck}
    XP: {char.XP}
    Gold: {char.gold}G
    Current Weapon: '{char.weapon}' 
    Max Damage amount: ({char.maxDamage})
    Current Armor: '{char.armName}' ({char.armor})

    Select an Item to use or press ENTER to return back to previous screen""")
        sel = menu(char.backpack)
        if type(sel) == int:
            selNum = 0
            for item in char.backpack:
                if sel == selNum:
                    useItem(char,item)
                selNum += 1
        else:
            keepGoing = False
            
def useItem(char,use):
    #takes in the item selection and checks it against a dictionary of items pulled from a file containing item dictionaries.
    #removes the item once used
    #if item does not match with any in the dictionary of items, item will disappear without any stat changes
    inFile = open("assets\\items\items.json", "r")
    ITEMS = json.load(inFile)
    inFile.close()
    begone = 0
    begoneCheck = 0
    for num,item in enumerate(ITEMS):
        begone += num + 1
        pass
    for num,item in enumerate(ITEMS):
        if item == use:
            if ITEMS[item][0] == "N":
                #Consumables
                print(f"{char.name} consumed {item}")
                HP = ITEMS[item][1]
                MP = ITEMS[item][2]
                if HP != 0:
                    char.HP += HP
                    print(f"{char.name} regained {HP} HP!")
                if MP != 0:
                    char.MP += MP
                    print(f"{char.name} regained {MP} MP!")
                char.backpack.remove(item)
                continue

            elif ITEMS[item][0] == "Y":
                #Equipment
                print(f"{char.name} equipped {item}")
                try:
                    newMaxArmor = ITEMS[item][1]
                    newMaxAttack = ITEMS[item][2]
                except:
                    newMaxArmor = 1
                    newMaxAttack = 5
                if newMaxArmor != 0:
                    char.backpack.append(char.armName)
                    char.armName = item
                    char.armor = newMaxArmor
                if newMaxAttack != 0:
                    char.backpack.append(char.weapon)
                    char.weapon = item
                    char.maxDamage = newMaxAttack
                char.backpack.remove(item)
                continue

            elif ITEMS[item][0] =="S":
                #spells
                if item == "Spellbook":
                    print(f"{char.name} now has the ability to use magic in battle!")
                else:
                    print(f"{char.name} learned how to cast {item}")
                char.magic.append(item)
                char.backpack.remove(item)
                continue

        begoneCheck += num + 1

    if begoneCheck == begone:
        print(f"{char.name} tried to use {use} but {use} suddenly vanished from their hand. +2 mental scarring")
        char.backpack.remove(use)

def shop(self,town):
    #Displays items in certain item sets based on which town is currently present
    keepGoing = True
    print("Shop Keeper: Welcome to my shop!\n")
    while keepGoing:
        print("Shop Keeper: If there is something you like, just let me know!")
        print(f"\n    Gold: {self.gold}G")
        sel = menu(["ITEMS", "EQUIPMENT", "SPELLCRAFT"])
        if sel == 0:
            shopMenu(self,town,"N")
        if sel == 1:
            shopMenu(self,town,"Y")
        if sel == 2: 
            shopMenu(self,town,"S")
        if sel == "":
            keepGoing = False
            print("Shop Keeper: Have a good day!")

def getItems(self,type,town):
    #gets a dictionary of items based on the town that the shop is present in
    if town == "Town of Beginnings":
        fileType = "beginnings"
    inFile = open(f"assets\items\{fileType}_items.json","r")
    ITEMS = json.load(inFile)
    inFile.close()
    newITEMS = {}
    print(f"\n   Gold: {self.gold}G")
    if type == "N":
        print("\n   Available Items\n")
    elif type == "Y":
        print("\n   Available Equipment\n")
    elif type == "S":
        print("\n   Available Spellcraft Equipment\n")
    print
    for item in ITEMS:
        if ITEMS[item][0] == type:
            newITEMS[item] = (ITEMS[item][0],ITEMS[item][1],ITEMS[item][2],ITEMS[item][3],ITEMS[item][4])
    return newITEMS

def shopMenu(self,town,type):
    #prints out items and matches it with the selection
    ITEMS = getItems(self,type,town)
    for num,item in enumerate(ITEMS):
        print(f"    {num}) {item} - {ITEMS[item][3]}G")
    try:
        sel = int(input("\n>>> "))
    except:
        sel = ""
    clear()
    for num,item in enumerate(ITEMS):
        if sel == num:
            if ITEMS[item][3] < self.gold:
                self.backpack.append(item)
                self.gold -= ITEMS[item][3]
                print(f"\nPurchaced {item} for {ITEMS[item][3]}G\n")
            else:
                print(f"Shop Keeper: I'm sorry {self.name}. I don't do tabs. Come back when you're a little mmmm wealthier.")

def visitInn(self):
    #displays available services for the inn
    keepGoing = True
    while keepGoing:
        print("Inn Keeper: Welcome to the Inn! Take a look at our menu options and please let me know what you'll like")
        print("\nPress ENTER to return to the previous screen")
        sel = menu(["Basic Package - 20 G", "Comfort Package - 50 G", "Comfort with Breakfast Package - 75 G", "Deluxe Package - 100G"])
        if sel == 0:
            innSleep(self,"As you were trying to rest, rats came to your bed to sleep. You managed to sleep through the night",4,20)
        elif sel == 1:
            innSleep(self,"You were suprised to find your room in neat order. You were able to sleep soundly tonight",3,50)
        elif sel == 2:
            innSleep(self,"You enjoyed the night and woke up to a hearty breakfast",2,75)
        elif sel == 3:
            innSleep(self,"Your bed frame was made of solid gold and the mattress was out of the world. You woke up in \nthe morning feeling like a million bucks",1,100)
        elif sel == "":
            print("Inn Keeper: Have a good day!")
            keepGoing = False
            
        else:
            print("Inn Keeper: I'm sorry, I didn't understand your request.")

def innSleep(self,message,rate,gold):
    #takes gold from hero gold variable and replenishes stats based on the rate of the room then prints the message that has been provided
        if self.gold > gold:
            slowPrint("...",1.5)
            print(message)
            self.HP += self.maxHP / rate
            self.MP += self.maxMP / rate
            self.gold -= gold
            if self.HP > self.maxHP:
                self.HP = self.maxHP
            if self.MP > self.maxMP:
                self.MP = self.maxMP
        else:
            print("You do not have enough gold for that!")
            print(f"needed: {gold}  Current Gold: {self.gold} ")

def play(hero):
    #main game menu 
    keepGoing = True
    if hero.name == "default":
        hero.name = new()
    town = "Town of Beginnings"
    while keepGoing:
        print(f"\n   Welcome to the {town}")
        gamemenu = ["Quit", "Venture out", "Inventory", "save", "Visit the shop",
                   "visit the inn", "Visit another town(not implimented)"]
        sel = menu(gamemenu)
        if sel == 0:
            #quit
            keepGoing = False
        if sel == 1:
            #venture out
            venture(hero)
        if sel == 2:
            #inventory
            checkInventory(hero)
        if sel == 3:
            #save
            save(hero)
            print("saved")
        if sel == 4:
            #shop
            shop(hero,town)
        if sel == 5:
            #inn
            visitInn(hero)
        if sel == 6:
            #change town which is not implimented
            pass