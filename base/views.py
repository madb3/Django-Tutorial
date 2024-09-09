from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name': 'Lets learn python1'},
    {'id':2, 'name': 'Design with me'},
    {'id':3, 'name': 'Frontend developers'}
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'home.html', {'rooms':rooms})

def room(request):
    return render('room.html')