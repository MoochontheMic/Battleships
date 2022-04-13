#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
import core.models

playerBoard = core.models.PlayerBoard()
guessBoard = core.models.GuessBoard()
players = core.models.Players()
class Index(View):
    template = 'index.html'
    def get(self, request):
        return render(request, self.template, {'playerBoard': playerBoard, 'guessBoard': guessBoard})
