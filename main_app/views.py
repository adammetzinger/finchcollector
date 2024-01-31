from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird
from .forms import FeedingForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    birds = Bird.objects.all()
    return render(request, 'birds/index.html', {'birds': birds})

def birds_detail(request, bird_id):
    birb = Bird.objects.get(id=bird_id)
    return render(request, 'birds/detail.html', {'bird': birb})

class FinchCreate(CreateView):
    model = Bird
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Bird
    success_url = '/birds'

def cats_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    feeding_form = FeedingForm()
    return render(request, 'cats/detail.html', {
        'bird': bird, 'feeding_form': feeding_form
    })

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)