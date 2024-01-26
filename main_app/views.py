from django.shortcuts import render

# Create your views here.

birds = [
    {'name': 'Jeff', 'breed': 'European Goldfinch', 'description': 'great nest builder', 'age': 5},
    {'name': 'Dillan', 'breed': 'House Finch', 'description': 'Nestbody', 'age': 5},
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'birds/index.html', {
        'birds': birds
    })