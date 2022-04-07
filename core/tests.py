from django.test import TestCase
import unittest
import pytest 
import sys
from core.models import Board, Game, Submarine


class TestShips():

    def testPlacementValid(self):
        board = Board()
        submarine = Submarine(0,0,True)
        for coordinate in submarine.position:
            xCurrent = coordinate[0]
            yCurrent = coordinate[1]
            board.playersBoard[xCurrent][yCurrent] = 1
# Create your tests here.
    def testPlacementInvalid(self):
        board = Board()
        submarine = Submarine(6,0,True)
        for coordinate in submarine.position:
            xCurrent = coordinate[0]
            yCurrent = coordinate[1]
            board.playersBoard[xCurrent][yCurrent] = 1
    