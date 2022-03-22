from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .utils import habr_parser

class HomePageView(View):
    def get(self, request):
        posts = habr_parser('https://habr.com/ru/all/')
        return render(request, 'index.html', {'posts':posts})

    


