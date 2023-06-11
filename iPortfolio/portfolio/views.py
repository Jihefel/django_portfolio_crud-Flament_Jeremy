from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Header, About, Skills, Portfolio, Services, Testimonials, Contact, SendMessage, Portfolio_description, Services_description, Testimonials_description
from admin.forms import SendMessageForm



# Create your views here.
def index(request):
    header = Header.objects.last()
    about = About.objects.last()
    skills = Skills.objects.last()
    portfolio = Portfolio.objects.all()
    portfolio_description = Portfolio_description.objects.last()
    all_services = Services.objects.all()
    services_description = Services_description.objects.last()
    testimonials = Testimonials.objects.all()
    testimonials_description = Testimonials_description.objects.last()
    contact = Contact.objects.last()
    messages = SendMessage.objects.all()
    portfolio = Portfolio.objects.all()
    paginator = Paginator(all_services, 6)  # Divise les services en pages de 6 éléments par page
    page_number = request.GET.get('page')  # Récupère le numéro de page à partir des paramètres GET

    services = paginator.get_page(page_number)  # Récupère les services pour la page spécifiée


    if request.method == 'POST':
        form = SendMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SendMessageForm()

    messages = SendMessage.objects.all()

    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'portfolio_description': portfolio_description,
    'services': services,
    'services_description': services_description,
    'testimonials': testimonials,
    'testimonials_description': testimonials_description,
    'contact': contact,
    'messages': messages,
    'form': form
    }

    return render(request, 'portfolio/index.html', context)

def navbar(request):
    header = Header.objects.last()
    about = About.objects.last()
    skills = Skills.objects.last()
    portfolio = Portfolio.objects.all()
    portfolio_description = Portfolio_description.objects.last()
    all_services = Services.objects.all()
    services_description = Services_description.objects.last()
    testimonials = Testimonials.objects.all()
    testimonials_description = Testimonials_description.objects.last()
    contact = Contact.objects.last()
    messages = SendMessage.objects.all()
    paginator = Paginator(all_services, 6)  # Divise les services en pages de 6 éléments par page
    page_number = request.GET.get('page')  # Récupère le numéro de page à partir des paramètres GET

    services = paginator.get_page(page_number)  # Récupère les services pour la page spécifiée
    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'portfolio_description': portfolio_description,
    'services': services,
    'services_description': services_description,
    'testimonials': testimonials,
    'testimonials_description': testimonials_description,
    'contact': contact,
    'messages': messages
}
    return render(request, 'portfolio/header.html', context)

def portfolio_details(request, id):
    project = Portfolio.objects.get(id=id)
    return render(request, 'portfolio/portfolio-details.html', {'project': project})