from django.db import models

# Create your models here.
class Header(models.Model):
    full_name = models.CharField(max_length=150, blank=True)
    jobs = models.TextField(null=True, blank=True)
    image_hero = models.ImageField(blank=True)
    def __str__(self):
        return self.full_name

class About(models.Model):
    photo = models.ImageField(blank=True)
    description1_ab = models.TextField(blank=True)
    description2_ab = models.TextField(blank=True)
    description3_ab = models.TextField(blank=True)
    job = models.CharField(max_length=200, blank=True)
    birthday = models.DateField(blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    diploma = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    freelance = models.BooleanField(default=True, blank=True)
    def __str__(self):
        return self.description1_ab

class Skills(models.Model):
    description1_sk = models.TextField(blank=True)
    html = models.IntegerField(blank=True)
    css = models.IntegerField(blank=True)
    js = models.IntegerField(blank=True)
    php = models.IntegerField(blank=True)
    wp = models.IntegerField(blank=True)
    ps = models.IntegerField(blank=True)
    def __str__(self):
        return self.description1_sk

class Portfolio(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    CATEGORY_CHOICES = (
        ('app', 'App'),
        ('card', 'Card'),
        ('web', 'Web'),
    )
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, blank=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
    
class Portfolio_description(models.Model):
    description_portfolio = models.TextField(blank=True)

class Services(models.Model):
    icon = models.TextField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    description_se = models.TextField(blank=True)

    def __str__(self):
        return f"{self.icon} - {self.title}"
    
class Services_description(models.Model):
    description_services = models.TextField(blank=True)

class Testimonials(models.Model):
    photo = models.ImageField(blank=True)
    name = models.CharField(max_length=100, blank=True)
    job = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Testimonials_description(models.Model):
    description_testimonials = models.TextField(blank=True)

class Contact(models.Model):
    description_co = models.TextField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    def __str__(self):
        return self.description_co
    
class SendMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()