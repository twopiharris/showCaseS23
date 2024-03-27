#Documentation on path lib
# https://docs.python.org/3/library/pathlib.html#pathlib.Path
from pathlib import Path
import Game
import unittest
import os

class FileSystem:
    def __init__(self, games_directory: str):
        self.directories = self.read_directories(games_directory)
        self.games = self.set_games(self.directories)
        
    def read_directories(self, games_directory: str):
        directories = []
        games = Path(games_directory)
        for entry in games.iterdir():
            if entry.is_dir():
                directories.append(entry)
        return directories
    
    def make_game(self, directory: Path) -> Game:
        main_directory = ''
        for item in directory.iterdir():
            if directory.name in item.name or 'main' in item.name:
                main_directory = item
        return Game.Game(directory.name, main_directory, directory)
    
    
    def set_games(self, directories: list[Path]) -> list[Game]:
        games = []
        for directory in directories:
            games.append(self.make_game(directory))
        return games
    
    def get_game(self, name: str) -> Game:
        for game in self.games:
            if name == game.name:
                return game

    def get_games(self) -> list[Game]:
        return self.games
        
    def play(self, game):
        self.get_game(game).run()
        os.chdir('../..')
     
    def get_game_names(self) -> list[str]:
        game_names = []
        for game in self.get_games():
            game_names.append(game.name)
        return game_names
