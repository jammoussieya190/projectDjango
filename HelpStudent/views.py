# views.py

from django.shortcuts import render, redirect
from blog import models
from .models import Post
from .forms import EventForm, PostForm
from django.http import HttpResponse 
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    # Logique de la vue index
    return render(request, 'helpstudent/acceuil.html')
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Enregistrer le post dans la base de données
            post = form.save()
            return redirect('helpstudent/listepub.html')  # Rediriger vers la page d'accueil après la création du post
    else:
        form = PostForm()
    return render(request, 'helpstudent/listepub.html', {'form': form})


def publish_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'helpstudent/blog.html', {'form': form})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'helpstudent/post_detail.html', {'post': post})

def search(request):
    keyword = request.GET.get('keyword')
    results = Post.objects.filter(title__icontains=keyword)
    return render(request, 'helpstudent/search.html', {'search_results': results})

@login_required
def home(request):
    context = {'val': "Menu Acceuil"}
    return render(request, 'helpstudent/dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        # Gérer les requêtes non-POST
        messages.error(request, "Méthode non autorisée.")
        return redirect('home')  # Rediriger vers la page d'accueil ou une autre page


def dashboard(request):
    # Logique pour récupérer les données du tableau de bord
    # Par exemple, vous pouvez récupérer des données d'utilisateur, des statistiques, etc.
    context = {
        # Incluez les données nécessaires à votre modèle de modèle
    }
    return render(request, 'helpstudent/dashboard.html', context)

def transport(request):
    transports = Transport.objects.all()
    return render(request, 'helpstudent/transport.html')

def publications(request):
    return render(request, 'helpstudent/publications.html')




from .models import Event


def evenements(request):
    events = Event.objects.all()
    return render(request, 'helpstudent/evenements.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre les données du formulaire dans la base de données
            return render(request, 'helpstudent/evenements.html')  # Redirige vers une vue après l'ajout d'un événement
    else:
        form = EventForm()

    return render(request, 'helpstudent/add_event.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

def edit_event(request, event_id):
    # Récupérer l'événement à modifier depuis la base de données
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        # Remplir le formulaire avec les données de la requête POST et de l'instance d'événement actuelle
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            # Enregistrer les modifications dans la base de données
            form.save()
            # Rediriger vers la page des détails de l'événement modifié
            return render(request, 'helpstudent/evenements.html', {'event': event}) 
    else:
        # Remplir le formulaire avec les données de l'événement existant
        form = EventForm(instance=event)

    return render(request, 'helpstudent/edit_event.html', {'form': form, 'event': event})  


def delete_event(request, event_id):
    # Récupérer l'événement à supprimer depuis la base de données
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        # Si la requête est une méthode POST, cela signifie que l'utilisateur a confirmé la suppression
        event.delete()
        # Rediriger vers une page de confirmation ou une autre vue
        return redirect('evenements')  # Remplacez 'event_list' par le nom de l'URL de la vue qui affiche la liste des événements

    # Si la requête n'est pas POST, afficher la page de confirmation de la suppression
    return render(request, 'helpstudent/delete_event.html', {'event': event})

from .models import StageOffer
from .forms import StageOfferForm

def stage(request):
    stage_offers = StageOffer.objects.all()
    return render(request, 'helpstudent/stage.html', {'stage_offers': stage_offers})
   
def add_stage_offer(request):
    if request.method == 'POST':
        form = StageOfferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stage')
    else:
        form = StageOfferForm()
    return render(request, 'helpstudent/add_stage_offer.html', {'form': form})

def edit_stage_offer(request, offer_id):
    offer = get_object_or_404(StageOffer, pk=offer_id)
    if request.method == 'POST':
        form = StageOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect('stage')
    else:
        form = StageOfferForm(instance=offer)
    return render(request, 'helpstudent/edit_stage_offer.html', {'form': form})

def delete_stage_offer(request, offer_id):
    offer = get_object_or_404(StageOffer, pk=offer_id)
    if request.method == 'POST':
        offer.delete()
        return redirect('stage')
    return render(request, 'helpstudent/delete_stage_offer.html', {'offer': offer})


from .forms import LogementForm
from .models import Logement



def logement(request):
    logements = Logement.objects.all()
    return render(request, 'helpstudent/logement.html', {'logements': logements})


def ajouter_logement(request):
    if request.method == 'POST':
        form = LogementForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers la vue affichant la liste des logements après l'ajout
            return redirect('logement')
    else:
        form = LogementForm()
    return render(request, 'helpstudent/ajouter_logement.html', {'form': form})



def modifier_logement(request, logement_id):
    logement = Logement.objects.get(pk=logement_id)
    if request.method == 'POST':
        form = LogementForm(request.POST, instance=logement)
        if form.is_valid():
            form.save()
            return redirect('logement')
    else:
        form = LogementForm(instance=logement)
    return render(request, 'helpstudent/modifier_logement.html', {'form': form})

def supprimer_logement(request, logement_id):
    logement = Logement.objects.get(pk=logement_id)
    logement.delete()
    return redirect('logement')

from django.shortcuts import render
from .models import Transport
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transport
from .forms import TransportForm

def transport_list(request):
    transports = Transport.objects.all()
    return render(request, 'helpstudent/transport.html', {'transports': transports})


def add_transport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport_list')
    else:
        form = TransportForm()
    return render(request, 'helpstudent/add_transport.html', {'form': form})

def edit_transport(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    if request.method == 'POST':
        form = TransportForm(request.POST, instance=transport)
        if form.is_valid():
            form.save()
            return redirect('transport_list')
    else:
        form = TransportForm(instance=transport)
    return render(request, 'helpstudent/edit_transport.html', {'form': form})

def delete_transport(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    if request.method == 'POST':
        transport.delete()
        return redirect('transport_list')
    return render(request, 'helpstudent/delete_transport.html', {'transport': transport})


from django.shortcuts import render, redirect
from .forms import PublicationForm

def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm()
    return render(request, 'helpstudent/add_publication.html', {'form': form})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Publication
from .forms import PublicationForm

def edit_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('publication_list')
    else:
        form = PublicationForm(instance=publication)
    return render(request, 'helpstudent/edit_publication.html', {'form': form})

def delete_publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        publication.delete()
        return redirect('publication_list')
    # S'il y a une requête GET, cela ne fait rien et redirige simplement vers la liste des publications
    return redirect('publication_list')


from django.shortcuts import render
from .models import Publication

def publication_list(request):
    publications = Publication.objects.all()
    return render(request, 'helpstudent/publication_list.html', {'publications': publications})


from django.shortcuts import render
from .models import Event, StageOffer, Logement, Transport, Publication

def publication_listcl(request):
    publications = Publication.objects.all()
    return render(request, 'helpstudent/client/publication.html', {'publications': publications})

def logementcl(request):
    logements = Logement.objects.all()
    return render(request, 'helpstudent/client/logement.html', {'logements': logements})

def evenementscl(request):
    events = Event.objects.all()
    return render(request, 'helpstudent/client/event.html', {'events': events})

def transport_listecl(request):
    transports = Transport.objects.all()
    return render(request, 'helpstudent/client/transport.html', {'transports': transports})

def stagecl(request):
    stage_offers = StageOffer.objects.all()
    return render(request, 'helpstudent/client/stage.html', {'stage_offers': stage_offers})


from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(title, duration, location, description):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    
    # Ajoutez les données au PDF
    c.drawString(100, 750, f"Titre: {title}")
    c.drawString(100, 730, f"Durée: {duration}")
    c.drawString(100, 710, f"Lieu: {location}")
    c.drawString(100, 690, f"Description: {description}")

    c.save()
    buffer.seek(0)
    return buffer
from django.http import HttpResponse
from .models import StageOffer

def print_stage_offer(request, offer_id):
    offer = StageOffer.objects.get(id=offer_id)
    pdf = generate_pdf(offer.title, offer.duration, offer.location, offer.description)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="offre_stage_{offer_id}.pdf"'
    return response
