from django.shortcuts import render, redirect
from .models import Carro, Aluguel
from .forms import AluguelForm, ClienteForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def listar_carros(request):
    carros = Carro.objects.all()
    context = {"carros": carros}
    return render(request, "carro/listar_carros.html", context)

def detalhar_carro(request, pk):
    carro = Carro.objects.get(pk=pk)
    context = {"carro": carro}
    return render (request, "carro/detalhar_carro.html", context)


def listar_aluguel(request):
    alugel = Aluguel.objects.all()
    context = {"alugel": alugel}
    return render (request, "aluguel/listar_aluguel.html", context)

def realizar_aluguel(request):
    if request.method == "POST":
        form = AluguelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AluguelForm()
            return render(request, "aluguel/realizar_aluguel.html", {'form': form})
    else:
        form = AluguelForm()
        return render(request, "aluguel/realizar_aluguel.html", {'form': form})
    
def realizar_cadastro(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ClienteForm()
            return render(request, "cliente/realizar_cadastro.html", {'form': form})
    else:
        form = ClienteForm()
        return render(request, "cliente/realizar_cadastro.html", {'form': form})