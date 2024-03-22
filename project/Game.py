import importlib.util 
import os

class Game:
    def __init__(self, name, game_main, game_directory):
        self.name = name
        self.game_main = game_main
        self.game_directory = game_directory
    
    def run(self):
        # documentation used
        #https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
        spec = importlib.util.spec_from_file_location(self.name, self.game_main)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        os.chdir(self.game_directory)
        module.main.main()
        