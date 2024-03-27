# How to Add Games

1. In the `project/games` directory create a folder that matches the name of the game
    - Do not include spaces
    - Do not place content into the `project/test_games` folder. This is for unit testing the software
2. Place the pygame and all of its content into this folder
3. The file you wish to run should either match the folder name or be named `main`
    - For example the folder `project/games/ExampleGame.py` folder would have the primary Python file be named `ExampleGame.py` 
4. There is no need to include the `simpleGE.py` file in the games directory, as that is provided in the root of the project.
5. It is likely that changes will be needed to be made to the games code to run.
6. Certain color names, file directory instructions, and various assumptions will need to be tested for and changed

## Updating the Game for the Software

1. The Arcade Machine runs without a keyboard or mouse, so any inputs that require typing, click or browsing with mouse will need replaced with inputs that are possible on the machine.

2. Sometimes the game will not be able to import assets. To fix this rename the import to have the correct file path

    - For example, the game `GamerGuy` will needs `Guy.png` but the game cannot find it and throws and error saying the file does not exist. To fix this when the image is loaded from path include the path relative to the project. `pygame.load.image(games\\GamerGuy\\Guy.png)` instead of `pygame.load.image(Guy.png)`
3. If the game has multiple python files, the imports will also need to be adjusted. `GamerGuy.py` imports `Inventory.py`
```
# import Inventory, simpleGE, time <- the old import statement is replaced with

import simpleGE, time
import games.GamerGuy.Inventory as Inventory
```
