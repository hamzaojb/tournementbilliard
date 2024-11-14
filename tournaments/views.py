# tournaments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Tournament
from .forms import RegistrationForm
from django.contrib import messages
from .models import Publication


def home(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/home.html', {'tournaments': tournaments})
def register_for_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            phone = form.cleaned_data['phone']
            
            # Vérifier si le numéro de téléphone existe déjà dans la base de données
            if form.instance.__class__.objects.filter(phone=phone).exists():
                # Si le numéro existe déjà, afficher un message d'erreur
                messages.error(request, "Ce numéro de téléphone est déjà utilisé. Veuillez en choisir un autre.")
                return render(request, 'tournaments/register.html', {'form': form, 'tournament': tournament})

            # Si le numéro n'existe pas, l'enregistrer
            registration = form.save(commit=False)
            registration.tournament = tournament  # Lier l'inscription au tournoi
            registration.save()
            messages.success(request, "Inscription réussie !")
            return redirect('tournaments:home')  # Rediriger vers la page principale des tournois

        else:
            messages.error(request, "Le numéro de téléphone ou email est déjà utilisé. Veuillez en fournir un autre.")
            return render(request, 'tournaments/register.html', {'form': form, 'tournament': tournament})

    else:
        form = RegistrationForm()

    return render(request, 'tournaments/register.html', {'form': form, 'tournament': tournament})

# tournaments/views.py

def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'tournaments/list.html', {'publications': publications})
