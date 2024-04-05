

import sys
import os
 
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to 
# the sys.path.
sys.path.append(parent)


from pathlib import Path
import unittest
import os
from FileSystem import FileSystem
from Game import Game

class TestFileSystem(unittest.TestCase):

    def test_get_ExampleGameName(self):
        files = FileSystem('test_games')
        self.assertEqual(files.get_game('ExampleGame').name, 'ExampleGame')
    
    def test_get_ExampleGameMain(self):
        files = FileSystem('test_games')
        self.assertEqual(files.get_game('ExampleGame').game_main, Path('test_games/ExampleGame/main.py'))

    def test_get_ExampleGameDir(self):
        files = FileSystem('test_games')
        self.assertEqual(str(files.get_game('ExampleGame').game_directory), 'test_games/ExampleGame')
    
    def test_read_directories(self):
        files = FileSystem('test_games')
        directories = files.read_directories('test_games')

        self.assertEqual(directories.sort(), [Path('test_games/PandoraPong'),Path('test_games/ExampleGame'), Path('test_games/PandoraPong2')].sort())

    def test_make_ExampleGameName(self):
        files = FileSystem('test_games')
        self.assertEqual(files.make_game(Path('test_games/ExampleGame')).name, 'ExampleGame')
        
    def test_make_WithNameInsteadofMain(self):
        files = FileSystem('test_games')
        self.assertEqual(files.make_game(Path('test_games/PandoraPong2')).name, 'PandoraPong2')
    
    def test_get_ExampleGameMain(self):
        files = FileSystem('test_games')
        self.assertEqual(files.make_game(Path('test_games/ExampleGame')).game_main, Path('test_games/ExampleGame/main.py'))

    def test_get_ExampleGameDir(self):
        files = FileSystem('test_games')
        self.assertEqual(files.make_game(Path('test_games/ExampleGame')).game_directory, Path('test_games/ExampleGame'))

    def test_get_game_names(self):
        files = FileSystem('test_games')
        self.assertEqual(files.get_game_names().sort(), ['PandoraPong','ExampleGame', 'PandoraPong2'].sort())
    
    def test_set_games(self):
        files = FileSystem('test_games')
        games = files.set_games([Path('test_games/ExampleGame'), Path('test_games/PandoraPong')])
        games_paths = []
        for game in games:
            games_paths.append(game.game_main)
        self.assertEqual(games_paths.sort(), [Path('test_games/ExampleGame/main.py'), Path('test_games/PandoraPong/main.py')].sort())
    
    def test_get_games(self):
        files = FileSystem('test_games')
        games = files.get_games()
        games_paths = []
        for game in games:
            games_paths.append(game.game_directory)
        self.assertEqual(games_paths.sort(), [Path('test_games/PandoraPong'), Path('test_games/ExampleGame'), Path('test_games/PandoraPong2')].sort())
        
    def test_read_directories_type(self):
        files = FileSystem('test_games')
        directories = files.read_directories('test_games')
        self.assertEqual(type(directories), list)
    
    def test_make_game_type(self):
        files = FileSystem('test_games')
        game = files.make_game(Path('test_games/PandoraPong'))
        self.assertEqual(type(game), Game)
        
    def test_set_games_type(self):
        files = FileSystem('test_games')
        games = files.set_games([Path('test_games')])
        self.assertEqual(type(games), list)
        
    def test_get_game_type(self):
        files = FileSystem('test_games')
        game = files.get_game('ExampleGame')
        self.assertEqual(type(game), Game)

if __name__ == '__main__':
    unittest.main()
