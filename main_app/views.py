from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import bird
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    birds = bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    birb = bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': birb})

class FinchCreate(CreateView):
    model = bird
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = bird
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = bird
    success_url = '/birds'