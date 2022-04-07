from xmlrpc.client import Boolean
from django.db import models
#from views import Index

MAX_HEIGHT = 3
MAX_WIDTH = 3
MAX_PLAYERS = 2
# Create your models here.
class Board():
    
    def __init__(self):
        """
        initalises array of board
        """
        self.playersBoard = [[None for item in range(MAX_HEIGHT)] for other in range(MAX_WIDTH)]
        self.guessBoard = [[None for item in range(MAX_HEIGHT)] for other in range(MAX_WIDTH)]
         
        # def display(self):
        #     Index.get()
    





class Game():
    def __init__(self):
        """
        initalises the storing of ship postions
        """
        pass

    
    def positionShip(self, shipType:list, coords: list, orientation: bool):
        """
        creates the submarine
        """
        id = 1
        x = coords[0]
        y = coords[1]
        board = Board()
        if orientation :
            #Horizontal
            shipPlace = shipType[0]
        else:
            #Vertical
            shipPlace = shipType[1]
        try:
            for shipcoord in shipPlace:
                x = shipcoord[0]
                y = shipcoord[1]
                print(x,y)
                if not board.playersBoard[x][y]:
                    board.playersBoard[x][y] = id
        except IndexError:
            # Invalid move error
            print('Invalid move, please try again')
        
        return shipPlace, id

class Submarine():
    def __init__(self, x: int, y: int, horizontal: bool):
        """
        intialises submarine
        """
        if horizontal:
            self.position = [[x,y],[x+1,y],[x+2,y]]
        else:
            self.position = [[x,y],[x,y+1],[x,y+2]]



class Players():
    def __init__(self):
        """
        initalises the stored ships and guesses for each player
        """
        self.shipPositions1 = []
        self.shipPositions2 = []
        self.guessPositions1 = []
        self.guessPositions2 = []

    def updatePlayerShips(self,player:bool, shipPositionsAndID: list):
        """
        updates players board with placed ships positions
        """
        currentShipPositions = shipPositionsAndID[0]
        currentShipID = shipPositionsAndID[1]
        # try:

        #     if player:
        #         for coords in currentShipPositions:
        #             x = coords[0]
        #             y = coords[1]
        #             if self.shipPositions1
# ships = Ships()
# ships.positionShip(ships.submarine,[78,1765],True)