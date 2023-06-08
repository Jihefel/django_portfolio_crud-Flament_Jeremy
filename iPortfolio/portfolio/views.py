from django.shortcuts import render, redirect
from .models import Header, About, Skills, Portfolio, Services, Testimonials, Contact
from admin.forms import HeaderForm, AboutForm, PortfolioForm, SkillsForm, ServicesForm, TestimonialsForm, ContactForm

header = Header.objects.last()
about = About.objects.last()
skills = Skills.objects.last()
portfolio = Portfolio.objects.all()
services = Services.objects.all()
testimonials = Testimonials.objects.all()
contact = Contact.objects.last()


# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()
    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'services': services,
    'testimonials': testimonials,
    'contact': contact
}
    return render(request, 'portfolio/index.html', context)

def navbar(request):
    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'services': services,
    'testimonials': testimonials,
    'contact': contact
}
    return render(request, 'portfolio/header.html', context)

def portfolio_details(request, id):
    project = Portfolio.objects.get(id=id)
    return render(request, 'portfolio/portfolio-details.html', {'project': project})


# Admin

def edit(request, section, id=None):
    form = None
    if request.method == 'POST':
        if section == 'header':
            form = HeaderForm(request.POST, instance=header)
        elif section == 'about':
            form = AboutForm(request.POST, instance=about)
        elif section == 'skills':
            form = SkillsForm(request.POST, instance=skills)
        elif section == 'portfolio':
            if id is not None:
                project = Portfolio.objects.get(id=id)
                form = PortfolioForm(request.POST, instance=project)
            else:
                form = PortfolioForm()
        elif section == 'services':
            form = ServicesForm(request.POST, instance=services)
        elif section == 'testimonials':
            form = TestimonialsForm(request.POST, instance=testimonials)
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
        elif section == 'services':
            form = ServicesForm(instance=services)
        elif section == 'testimonials':
            form = TestimonialsForm(instance=testimonials)
        elif section == 'contact':
            form = ContactForm(instance=contact)
    
    portfolio = Portfolio.objects.all()

    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'services': services,
    'testimonials': testimonials,
    'contact': contact,
    'form' : form,
    'section': section
    }

    return render(request, 'admin/edit.html', context)


def index_admin(request):
    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'services': services,
    'testimonials': testimonials,
    'contact': contact
}
    return render(request, 'admin/index.html', context)

def navbar_admin(request):
    context = {
    'header': header,
    'about': about,
    'skills': skills,
    'portfolio': portfolio,
    'services': services,
    'testimonials': testimonials,
    'contact': contact
}
    return render(request, 'admin/header.html', context)

