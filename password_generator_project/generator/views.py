
from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def home(request):  # we can access information within the request variable passed
    '''Set up the home page'''
    return render(request, 'generator/home.html', {'password':'iug4t8734feif'})  # the dictionary we pass here is sent to the templates and we can access it

def password(request):
    '''Set up the password page'''
    characters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    numbers = ''.join(f'{i} ' for i in range(10)).split()
    
    if request.GET.get('uppercase'):
        characters.extend([*map(str.upper, characters)])
    if request.GET.get('special'):
        characters.extend(string.punctuation)
    if request.GET.get('numbers'):
        characters.extend(numbers)
    
    length= int(request.GET.get('length', 12))
    thepassword = ''
    for _ in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    '''Set up the about page'''
    return render(request, 'generator/about.html')