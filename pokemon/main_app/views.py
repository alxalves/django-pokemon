from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon, Ribbon
from .forms import MoveForm
# Create your views here.
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3
import os


# Define the home view

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def pokemon_index(request):
    # pokemon = Pokemon.objects.all()
    pokemon = Pokemon.objects.filter(user=request.user)
    return render(request, 'pokemon/index.html', { 'pokemon': pokemon})

@login_required
def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    ribbons_pokemon_doesnt_have = Ribbon.objects.exclude(id__in=pokemon.ribbons.all().values_list('id'))
    move_form = MoveForm()
    return render(request, 'pokemon/detail.html', 
    { 
      'pokemon': pokemon,
      'move_form': move_form,
      'ribbons': ribbons_pokemon_doesnt_have
     })


class PokemonCreate(LoginRequiredMixin,CreateView):
    model = Pokemon
    fields = ['name', 'type', 'description', 'level']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)


class PokemonUpdate(LoginRequiredMixin,UpdateView):
    model = Pokemon
    fields = ['name', 'type', 'description', 'level']
    success_url = '/pokemon/'


class PokemonDelete(LoginRequiredMixin,DeleteView):
    model = Pokemon
    success_url = '/pokemon/'


@login_required
def add_move(request, pokemon_id):
    form = MoveForm(request.POST)

    if form.is_valid():
        # do some stuff on when the form is valid
        new_move = form.save(commit=False)
        # stuff? create a new move instance
        new_move.pokemon_id = pokemon_id
        new_move.save()
        # stuff? write new feeding to the db
    return redirect('detail', pokemon_id=pokemon_id)


class RibbonList(LoginRequiredMixin,ListView):
  model = Ribbon


class RibbonCreate(LoginRequiredMixin,CreateView):
    model = Ribbon
    fields = '__all__'


class RibbonDetail(LoginRequiredMixin,DetailView):
    model = Ribbon


class RibbonUpdate(LoginRequiredMixin,UpdateView):
    model = Ribbon
    fields = ['name', 'color']


class RibbonDelete(LoginRequiredMixin,DeleteView):
    model = Ribbon
    success_url = '/ribbons'


@login_required
def assoc_ribbon(request, pokemon_id, ribbon_id):
    Pokemon.objects.get(id=pokemon_id).ribbons.add(ribbon_id)
    return redirect('detail', pokemon_id=pokemon_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    else:
      error_message = 'Invalid signup - Try Again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
