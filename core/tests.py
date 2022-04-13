from django.test import TestCase
import unittest
import pytest 
import sys
from core.models import PlayerBoard, Game, Submarine


class TestShips():

    def testPlacementValid(self):
        board = PlayerBoard()
        submarine = Submarine(0,0,True)
        for coordinate in submarine.position:
            xCurrent = coordinate[0]
            yCurrent = coordinate[1]
            board.playersBoard[xCurrent][yCurrent] = 1
# Create your tests here.
    def testPlacementInvalid(self):
        board = PlayerBoard()
        submarine = Submarine(6,0,True)
        for coordinate in submarine.position:
            xCurrent = coordinate[0]
            yCurrent = coordinate[1]
            board.playersBoard[xCurrent][yCurrent] = 1
    