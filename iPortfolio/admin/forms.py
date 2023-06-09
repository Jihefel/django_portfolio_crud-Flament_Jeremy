from django import forms
from portfolio.models import Header, About, Skills, Portfolio, Services, Testimonials, Contact, SendMessage

class HeaderForm(forms.ModelForm):
    class Meta:
        model = Header
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = '__all__'

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = SendMessage
        fields = '__all__'