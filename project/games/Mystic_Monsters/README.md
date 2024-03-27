# Mystic_Monsters
Final exam code for CS120
This code is still in a work in progress stage.

I plan to finish the entire code as this project has really got my gears turning on what I can do in a python text environment.

Do make sure that you extract all files as show in the directory. 

How to play:

Menus will be shown in the window.

type in the number and only the number that corresponds to the option you want to select and press <ENTER>

if no quit button is available, press <ENTER> to return back to the previous menu (Usually in battle menus and in inventory menus.

Your objective is to venture out and defeat any monsters you may encounter.

Use the town's shop and inn to your advantage if you have the gold for it of course.

There are final bosses in the game but only one has been included.


There is a debug menu included in the code to be able to test out certain functions of the program.

if you wish to access this menu, type in 63 and press <ENTER> 

(NOTE) The debug menu is not meant for normal operation of the code therefore the debug menu code has not been refined or "idiot proofed" in any way due to the interest of time.

You may experience crashes if you use this menu. You have been warned..

Initial Game Document

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

Some things I chose to change from my original goals were to not include charm. I've also included an INN system as well.

Technologies I used were
importing other python files,
Dictionaries,
Lists,
Functions,
Classes,
While & for loops,
File IO,
and
Random number generators

No External resources used besides pointers on how to create certain lines of code.

In the beginning, there was nothing.. then I said "Let there be code" and it was beautiful..
Some of the things I've learned was more effective stratigies on accessing dictionary values,
using file IO with directories, and using external built in tools.

I really didn't get stuck often but when I did, usually in the planning phase when I wanted to figure out how I wanted certain things to work then translate it into code.

I really wish I could improve on getting more assets to use in the game as in its current stage, is really easy to play and finish.. maybe add a final boss type thing? a lot of monsters and creativity goes into that.

I was pretty close to my original game document with only a few additions and 1 concept removed entirely. Multi monster combat is still in the works I just didn't have enough time to plan and execute the code as I was more focused on geting the general system working first.

I kept goals and when I was not working on my code, spent time thinking on what I could make my code do. Example of this would be how I developed the magic/item cross reference system and the INN. I really wanted a quick way to heal up chunks of health and MP when not in battle

