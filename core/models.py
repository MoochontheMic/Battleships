from django.db import models

MAX_HEIGHT = 3
MAX_WIDTH = 3
# Create your models here.
class Board():
    
    def __init__(self):
        """
        initalises array of board
        """
        self.name = 'test'
        self.array = [[' ' for item in range(MAX_HEIGHT)] for other in range(MAX_WIDTH)]