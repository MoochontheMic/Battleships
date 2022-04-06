#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views import View
import core.models

board = core.models.Board()

class Index(View):
    template = 'index.html'
    def get(self, request):
        return render(request, self.template, {'board': board})
