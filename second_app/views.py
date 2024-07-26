from django.shortcuts import render
import random
from faker import Faker


# Create your views here.

def name(request):
    return render(request, 'name.html')

def goal(request, number):
    
    goal = random.randrange(1,10)

    context = {
        'goal': goal,
    }

    return render(request, 'goal.html', context)

def salad(request):

    menus= ['닭가슴살', '포크', '양배추']

    salad = random.choice(menus)
    context = {
        'salad' : salad,
    }

    return render(request, 'salad.html', context)

def posts(request):
    fake = Faker()

    fake_posts = []

    for i in range(100):
        fake_posts.append(fake.text())

    context = {
        'fake_posts': fake_posts,
    }

    return render(request, 'posts.html', context)

def combination(request):

    context = {
        'combination':combination,
               }

    return render(request, 'combination.html' , context)






