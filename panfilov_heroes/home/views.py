from django.shortcuts import render, get_object_or_404
from heroes.models import Hero

def home(request):
    panfilov = Hero.objects.filter(last_name='Панфилов').first()
    heroes = Hero.objects.exclude(last_name='Панфилов')
    return render(request, 'home/home.html', {'heroes': heroes, 'panfilov': panfilov})


def hero_detail(request, hero_id):
    hero = get_object_or_404(Hero, id=hero_id)  
    return render(request, 'home/hero_detail.html', {'hero': hero})

def panfilov_static_page(request):
    return render(request, 'home/Panfilov.html')

def momyshuly_static_page(request):
    return render(request, 'home/Momyshuly.html')

def panfilovcy_static_page(request):
    return render(request, 'home/Panfilovcy.html')


def school_info(request):
    return render(request, 'home/school_info.html')  

def panfilov_school_info(request):
    return render(request, 'home/panfilov_school_info.html')  
