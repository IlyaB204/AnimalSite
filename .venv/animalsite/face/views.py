from django.shortcuts import render

def index_view(request):
    render(request, 'anipat/index.html')