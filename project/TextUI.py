import FileSystem
import Getcha
import os

def print_games(games, current_game):
    games_string = 'Select a game:\n'
    for index in range(0, len(games)):
        if current_game == index:
            games_string += '> ' + games[index] + '\n'
        else:
            games_string += games[index] + '\n'
    return games_string
  
def Select(fileSystem):
    print('Select a game to play')
    games = fileSystem.get_game_names()
    current_game = 0
    buttonPressed = ''
    while(buttonPressed != '/'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(print_games(games, current_game))
        buttonPressed = Getcha.Getcha()
        # clean these ifs up
        if buttonPressed == 's' and current_game >= 0 and current_game < len(games)-1:
            current_game += 1
        elif buttonPressed == 'w' and current_game <= len(games)-1 and current_game > 0:
            current_game -= 1
    return games[current_game]


def Main():
    fileSystem = FileSystem.FileSystem('games')
    print('Welcome to the Arcade Machine')
    while True:
        selectedGame = Select(fileSystem)
        fileSystem.play(selectedGame)
        
    

if __name__ == '__main__':
    Main()

