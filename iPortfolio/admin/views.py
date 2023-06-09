from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from portfolio.models import Header, About, Skills, Portfolio, Services, Testimonials, Contact, SendMessage, Portfolio_description, Services_description, Testimonials_description
from .forms import HeaderForm, AboutForm, PortfolioForm, SkillsForm, ServicesForm, TestimonialsForm, ContactForm, PortfolioDescriptionForm, ServicesDescriptionForm, TestimonialsDescriptionForm


# Admin

def edit(request, section, id=None):

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

    form = None
    paginator = Paginator(all_services, 6)  # Divise les services en pages de 6 éléments par page
    page_number = request.GET.get('page')  # Récupère le numéro de page à partir des paramètres GET

    services = paginator.get_page(page_number)  # Récupère les services pour la page spécifiée

    if request.method == 'POST':
        if section == 'header':
            form = HeaderForm(request.POST, request.FILES, instance=header)
        elif section == 'about':
            form = AboutForm(request.POST, request.FILES, instance=about)
        elif section == 'skills':
            form = SkillsForm(request.POST, instance=skills)
        elif section == 'portfolio':
            if id is not None:
                project = Portfolio.objects.get(id=id)
                form = PortfolioForm(request.POST, request.FILES, instance=project)
            else:
                form = PortfolioForm()
        elif section == 'portfolio_description':
            form = PortfolioDescriptionForm(request.POST, instance=portfolio_description)
        elif section == 'services':
            if id is not None:
                service = Services.objects.get(id=id)
                form = ServicesForm(request.POST, instance=service)
            else:
                form = ServicesForm()
        elif section == 'services_description':
            form = ServicesDescriptionForm(request.POST, instance=services_description)
        elif section == 'testimonials':
            if id is not None:
                testi = Testimonials.objects.get(id=id)
                form = TestimonialsForm(request.POST, request.FILES, instance=testi)
            else:
                form = TestimonialsForm()
        elif section == 'testimonials_description':
            form = TestimonialsDescriptionForm(request.POST, instance=testimonials_description)
        elif section == 'contact':
            form = ContactForm(request.POST, instance=contact)
        
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print('no')
      
    else:
        if section == 'header':
            form = HeaderForm(instance=header)
        elif section == 'about':
            form = AboutForm(instance=about)
        elif section == 'skills':
            form = SkillsForm(instance=skills)
        elif section == 'portfolio':
            if id is not None:
                project = Portfolio.objects.get(id=id)
                form = PortfolioForm(instance=project)
            else:
                form = PortfolioForm()
        elif section == 'portfolio_description':
            form = PortfolioDescriptionForm(instance=portfolio_description)
        elif section == 'services':
            if id is not None:
                service = Services.objects.get(id=id)
                form = ServicesForm(instance=service)
            else:
                form = ServicesForm()
        elif section == 'services_description':
            form = ServicesDescriptionForm(instance=services_description)
        elif section == 'testimonials':
            if id is not None:
                testi = Testimonials.objects.get(id=id)
                form = TestimonialsForm(instance=testi)
            else:
                form = TestimonialsForm()
        elif section == 'testimonials_description':
            form = TestimonialsDescriptionForm(instance=testimonials_description)
        elif section == 'contact':
            form = ContactForm(instance=contact)
    
    portfolio = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()

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
    'form' : form,
    'section': section
    }

    return render(request, 'admin/edit.html', context)


def index_admin(request):

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
    portfolio = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()
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
    }

    return render(request, 'admin/index.html', context)


def navbar_admin(request):
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
    'messages': messages,
    }


    return render(request, 'admin/header.html', context)


def delete(request, section, property):
        
    if section == 'portfolio':
        if property is not None:
            project = Portfolio.objects.get(id=property)
            project.delete()
    elif section == 'services':
        if property is not None:
            service = Services.objects.get(id=property)
            service.delete()
    elif section == 'testimonials':
        if property is not None:
            testi = Testimonials.objects.get(id=property)
            testi.delete()
    elif section == 'contact':
        if property is not None:
            message = SendMessage.objects.get(id=property)
            message.delete()
            
    return redirect('admin')


def create(request, section):
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
    
    form = None
    paginator = Paginator(all_services, 6)  # Divise les services en pages de 6 éléments par page
    page_number = request.GET.get('page')  # Récupère le numéro de page à partir des paramètres GET

    services = paginator.get_page(page_number)  # Récupère les services pour la page spécifiée

    if request.method == 'POST':
        if section == 'portfolio':
            form = PortfolioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                form = PortfolioForm()
            
        elif section == 'services':
            form = ServicesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                form = ServicesForm()
        elif section == 'testimonials':
            form = TestimonialsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('index')
            else:
                form = TestimonialsForm()
      
    else:
        if section == 'portfolio':
            form = PortfolioForm()
        elif section == 'services':
            form = ServicesForm()
        elif section == 'testimonials':
            form = TestimonialsForm()
    
    portfolio = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()

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
    'form' : form,
    'section': section
    }

    return render(request, 'admin/create.html', context )