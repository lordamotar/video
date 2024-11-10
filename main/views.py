from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Category

def index(request):
    return render(request, 'main/index.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'main/portfolio.html', {'projects': projects})

def portfolio(request):
    projects = Project.objects.all()
    categories = Category.objects.all()  # Получаем все категории
    return render(request, 'main/portfolio.html', {'projects': projects, 'categories': categories})