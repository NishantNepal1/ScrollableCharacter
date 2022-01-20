from pyblinkpico import *;
import time

class character():
    def __init__(self):
        self.m = display
        self.m.fill(0)
        self.m.auto_show(True)
        
    def __get_character_matrix(self, char):
        #returns the character matrix of the char value, the char value can't have length more than one
        
        dict = {'A' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0]], 
            'B' :[[0,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,0,0]],
            'C' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
            'D' : [[0,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,0,0]], 
            'E' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
            'F' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0]],
            'G' : [[0,0,1,1,1,1,1,0],[0,1,1,0,0,0,1,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,1,1,1,0,0]],
            'H' : [[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0]],
            'I' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
            'J' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,0,1,1,1,1,0,0]],
            'K' : [[0,1,1,0,0,0,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,1,1,0,0],[0,1,1,1,1,0,0,0],[0,1,1,1,0,0,0,0],[0,1,1,1,1,0,0,0],[0,1,1,0,1,1,0,0],[0,1,1,0,0,1,1,0]],
            'L' : [[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
            'M' :[[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,0,1,1,0,1,0],[0,1,0,1,1,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0]],
            'N': [[0,1,1,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,1,0,1,0,0,1,0],[0,1,0,1,0,0,1,0],[0,1,0,0,1,0,1,0],[0,1,0,0,1,0,1,0],[0,1,0,0,0,1,1,0],[0,1,0,0,0,1,1,0]],
            'O' : [[0,0,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,0,1,1,1,1,0,0]],
            'P' : [[0,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0]],
            'Q' :[[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,0]],
            'R' : [[0,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,0,0],[0,1,1,1,1,0,0,0],[0,1,1,0,1,1,1,0],[0,1,1,0,0,1,1,0]],
            'S' :[[0,0,1,1,1,1,1,0],[0,0,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,0,0]],
            'T' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
            'U' : [[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0]],
            'V' : [[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,1,1,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
            'W' :[[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,1,1,0,1,0],[0,1,0,1,1,0,1,0],[0,1,0,1,1,0,1,0],[0,0,1,0,0,1,0,0]],
            'X' :[[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,0,1,0]],
            'Y' : [[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,1,0,0,1,1,0],[0,0,1,1,1,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
            'Z' :[[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,0]],
            'a' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,0]],
            'b' : [[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            'c' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            'd' : [[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,1,0,0]],
            'e' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,1,1,1,1,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,0,0]],
            'f' :[[0,0,0,0,1,1,0,0],[0,0,0,1,0,0,1,0],[0,0,0,1,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]],
            'g' : [[0,0,0,1,1,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0]],
            'h' :[[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0]],
            'i' : [[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]],
            'j' : [[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]],
            'k' : [[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,1,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0],[0,1,0,0,1,0,0,0]],
            'l': [[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]],
            'm' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0]],
            'n' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0]],
            'o' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            'p' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0]],
            'q' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,1,0,0]],
            'r' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0],[0,0,1,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]],
            's' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            't' : [[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,1,1,0]],
            'u' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0]],
            'v' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
            'w' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,1,1,0,1,0],[0,0,1,1,1,0,1,0],[0,0,1,0,0,1,0,0]],
            'x' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,0,1,0]],
            'y' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,0],[0,1,0,1,0,0,0,0],[0,0,1,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,1,1,1,0,0,0,0]],
            'z' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,1,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,1,1,1,0,0,0]],
            '0' : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,1,1,0],[0,1,0,0,0,1,1,0],[0,1,0,0,1,0,1,0],[0,1,0,1,1,0,1,0],[0,1,1,1,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,1,1,1,0,0]],
             0  : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,1,1,0],[0,1,0,0,0,1,1,0],[0,1,0,0,1,0,1,0],[0,1,0,1,1,0,1,0],[0,1,1,1,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,1,1,1,0,0]], 
            '1' : [[0,0,0,0,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,1,1,1,1,1,0]],
            1   : [[0,0,0,0,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,1,1,1,1,1,0]],
            '2' : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,1,0]], 
            2   : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,1,0]],
            '3' : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
            3   : [[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            '4' : [[0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0]],
            4   : [[0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0]],
            '5' : [[0,0,1,1,1,1,1,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,1,1,1,1,1,0,0]],
            5   : [[0,0,1,1,1,1,1,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,1,1,1,1,1,0,0]],
            '6' : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            6   : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            '7' :[[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0]],
            7   :[[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0]],
            '8' : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            8   : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            '9' : [[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            9   : [[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
            ' '   : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
            '-' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
            ',': [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,1,1,0,0,0],[0,1,1,1,0,0,0,0]],
            "block": [[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1]],
            '.': [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,0,0],[0,0,1,1,1,1,0,0],[0,0,1,1,1,1,0,0],[0,0,1,1,1,1,0,0]]
        }
        return dict[char]
    def get_padding(self, letter):
        dict = {
          'A': [0,7], 'B': [0,7], 'C': [0,7], 'D': [0,7], 'E': [0,7], 'F': [0,7], 'G': [0,7], 'H': [0,7], 'I': [0,7], 'J': [0,7], 'K': [0,7], 'L': [0,7], 'M': [0,7], 'N': [0,7], 'O': [0,7], 'P': [0,7], 'Q': [0,7], 'R': [0,7], 'S': [0,7], 'T': [0,7], 'U': [0,7], 'V': [0,7], 'W': [0,7], 'X': [0,7], 'W': [0,7], 'Z': [0,7],'Y':[0,7],
          'a': [0,7], 'b': [1,6], 'c': [0,6], 'd': [0,6], 'e': [0,6], 'f': [0,7], 'g': [1,6], 'h': [2,6], 'i': [2,4], 'j': [0,5], 'k': [0,5], 'l': [2,4], 'm': [0,7], 'n': [0,6], 'o': [0,6], 'p': [1,6], 'q': [2,7], 'r': [0,6], 's': [1,6], 't': [0,7], 'u': [2,6], 'v': [0,7], 'w': [0,7], 'x': [0,7], 'y': [0,4], 'z': [0,4],' ':[0,6],
          0: [0,7], '0':[0,7], 1:[0,7] , 2:[0,7] , 3:[0,6] , 4:[0,6], 5:[0,7] , 6:[0,6] , 7:[0,7] , 8:[0,6] , 9:[1,6],'1':[0,7] , '2':[0,7] , '3':[0,6] , '4':[0,6], '5':[0,7] , '6':[0,6] , '7':[0,7] , '8':[0,6] , '9':[1,6],",": [1,5],'-':[1,6],".":[2,6] 
}
        return dict[letter]
    
    def __get_ind_mat(self, char):
        char_mat = self.__get_character_matrix(char)
        char_pad = self.get_padding(char)
        length = char_pad[1]-char_pad[0]
        mat = [[None for i in range(length+2)] for i in range(8)]
        k = 0
        for i in range(8):
            k = 0
            for j in range(char_pad[0]-1, char_pad[1]+1):
                x = char_mat[i][j]
                mat[i][k] = char_mat[i][j]
                k +=1
        return mat, length
    
    def scroll(self, char): 
        mat =[ None for y in range(len(char))]
        total_len = [None for y in range(len(char))]
        for i in range(len(char)):
                mat[i], total_len[i] = self.__get_ind_mat(char[i])
        tot_len = 0
        for i in range(len(char)):
            tot_len += total_len[i]+2
        
        matr = [[None for y in range(tot_len+10)]for x in range(8)]
        k = 0
        h = 0
        l = 0
        for x in range(tot_len):
            for y in range(8):
                if(h>total_len[k]+1):
                    k +=1
                    l = 0
                    h = 0
                a = mat[k][y][l]
                matr[y][x] = mat[k][y][l]
            l +=1
            h+=1
        for i in range(8):
            for j in range(tot_len, tot_len+10):
                matr[i][j] = 0
        for h in range(len(matr[1])-8):
            for i in range(8):
                for j in range(8):
                    self.m[i,j] = matr[i][j+h]
                time.sleep(0.001)
                
       
    def show (self, char):
            if (len(char)>1):
                raise ValueError("Cannot Display two characters at the same time")
            char_matrix = self.__get_character_matrix(char)
            for i in range(0,8):
                for j in range(0,8):
                    self.m[i,j] = char_matrix[i][j]
                    
def main():
    character_disp = character()
    #character_disp.character_show('a')
    #character_disp.character_scroll('ai')
    #character_disp.scroll('money for sale')
    character_disp.show('a')
    #character_disp.scroll('abcdefghijklmnopqrstuvwxyz')
    
    
    
if __name__ == "__main__":
    main()

