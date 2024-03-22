
# How to import from parent directory taken from this tutorial
# https://www.geeksforgeeks.org/python-import-from-parent-directory/
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

from TextUI import print_games
import unittest


class TestFileSystem(unittest.TestCase):

    def test_print_games(self):
        games = ['test_games', 'fortnite', 'Earth Defense Force']
        current_game = 2
        self.assertMultiLineEqual(print_games(games, current_game), ('Select a game:\ntest_games\nfortnite\n> Earth Defense Force\n'))
    
    
if __name__ == '__main__':
    unittest.main()