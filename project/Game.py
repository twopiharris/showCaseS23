import importlib.util 
import os, subprocess

class Game:
    def __init__(self, name, game_main, game_directory):
        self.name = name
        self.game_main = game_main
        self.game_directory = game_directory
    
    def run(self):
        os.chdir(self.game_directory)
        process = subprocess.Popen(["python",self.name + ".py"])
        process.wait()


        
