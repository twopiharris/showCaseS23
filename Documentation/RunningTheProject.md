# Running the text front end

1. Pygame and getch will need to be installed on non-Windows operating systems, other operating systems only need to install Pygame.
2. Open a terminal instance
3. Run the following commands inside the BSUArcademachine directory
```
pip install pygame
pip install getch # if you are not on Windows
cd project
python TextUI.py
```
3. Move up and down the menu with the left stick. Press the left side button to select a game
4. The game should support closing and this will return focus to the interface

# Testing the software

1. The software has a few automated tests. With the terminal in the `BSUArcadeMachine/project` directory run the following command
```
python -m unittest
```
2. This will not test any of the games in the system, just the system itself.