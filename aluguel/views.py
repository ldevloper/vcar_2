from django.shortcuts import render, redirect 
from .models import Carro, Aluguel
from .forms import AluguelForm, ClienteForm
from .admin import CustomUserCreationForm
from django.contrib.auth.decorators import login_required, permission_required

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


@login_required
def listar_aluguel(request):
    aluguel = Aluguel.objects.filter(user=request.user)
    context = {'aluguel':aluguel}
    return render (request, "aluguel/listar_aluguel.html", context)

@login_required
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

def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            return render(request, 'index.html')
        
        else:
            print('invalid registration details')

    return render(request, "registration/register.html",{"form":form})


