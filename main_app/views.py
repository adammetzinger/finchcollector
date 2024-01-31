from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Toy
from .forms import FeedingForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request, bird_id):
    birds = Bird.objects(id=bird_id)
    return render(request, 'birds/index.html', {'birds': birds,})

def birds_detail(request, bird_id):
    bird = Bird.objects.get(id=bird_id)
    id_list = bird.toys.all().values_list('id')
    toys_bird_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    feeding_form = FeedingForm()
    return render(request, 'birds/detail.html', {
       'bird': bird, 
       'feeding_form': feeding_form,
       'toys': toys_bird_doesnt_have
        })

class FinchCreate(CreateView):
    model = Bird
    fields = ['name', 'breed', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Bird
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Bird
    success_url = '/birds'

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, bird_id, toy_id):
   Bird.objects.get(id=bird_id).toys.add(toy_id)
   return redirect('detail', bird_id=bird_id)

def unassoc_toy(request, bird_id, toy_id):
   Bird.objects.get(id=bird_id).toys.remove(toy_id)
   return redirect('detail', bird_id=bird_id)