from django.shortcuts import render, redirect
from portfolio.models import Header, About, Skills, Portfolio, Services, Testimonials, Contact
from ..portfolio.forms import HeaderForm, AboutForm, PortfolioForm, SkillsForm, PortfolioForm, ServicesForm, TestimonialsForm, ContactForm

header = Header.objects.last()
about = About.objects.last()
skills = Skills.objects.last()
portfolio = Portfolio.objects.all()
services = Services.objects.all()
testimonials = Testimonials.objects.all()
contact = Contact.objects.last()

