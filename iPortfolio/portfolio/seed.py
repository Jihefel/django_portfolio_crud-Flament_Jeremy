from django_seed import Seed
from portfolio.models import Header, About, Skills, Portfolio, Services, Testimonials, Contact, Portfolio_description, Services_description, Testimonials_description
import random
from faker import Faker

def run():
    seeder = Seed.seeder()
    faker = Faker()

    # Header
    seeder.add_entity(Header, 1, {
        'full_name': lambda x: faker.name(),
        'jobs': lambda x: [faker.job() for _ in range(3)],
        'image_hero': "hero-bg.jpg",
    })

    # About
    seeder.add_entity(About, 1, {
        'photo': "profile-img.jpg",
        'description1_ab': lambda x: faker.paragraph(nb_sentences=3),
        'description2_ab': lambda x: faker.sentence(nb_words=50, variable_nb_words=True),
        'description3_ab': lambda x: faker.paragraph(nb_sentences=6),
        'birthday': lambda x: faker.date_of_birth(),
        'website': lambda x: faker.url(),
        'phone': lambda x: faker.phone_number(),
        'city': lambda x: faker.city(),
        'age': lambda x: random.randint(18, 65),
        'diploma': lambda x: faker.word(),
        'email': lambda x: faker.email(),
        'job': lambda x: faker.job(),
        'freelance': lambda x: faker.boolean(chance_of_getting_true=80),
    })

    # Skills
    seeder.add_entity(Skills, 1, {
        'description1_sk': lambda x: faker.paragraph(nb_sentences=3),
        'html': lambda x: random.randint(80, 100),
        'css': lambda x: random.randint(60, 100),
        'js': lambda x: random.randint(30, 100),
        'php': lambda x: random.randint(30, 100),
        'wp': lambda x: random.randint(30, 100),
        'ps': lambda x: random.randint(30, 100),
    })

    # Portfolio
    seeder.add_entity(Portfolio, 12, {
        'image': lambda x: f'portfolio/portfolio-{faker.random_int(min=1, max=9)}.jpg',
        'title': lambda x: faker.sentence(nb_words=3),
        'category': lambda x: random.choice(['app', 'card', 'web']),
    })

    seeder.add_entity(Portfolio_description, 1, {
        'description_portfolio': lambda x: faker.paragraph(nb_sentences=3),
    })

    # Services
    seeder.add_entity(Services, 6, {
        'icon': lambda x: random.choice(['<i class="fa-solid fa-briefcase"></i>', '<i class="fa-solid fa-binoculars"></i>', '<i class="fa-solid fa-sun"></i>', '<i class="fa-solid fa-calendar-days"></i>', '<i class="fa-solid fa-ranking-star"></i>', '<i class="fa-solid fa-list-check"></i>', '<i class="fa-solid fa-lightbulb"></i>', '<i class="fa-solid fa-medal"></i>']),
        'title': lambda x: faker.sentence(nb_words=2),
        'description_se': lambda x: faker.sentence(nb_words=40, variable_nb_words=True),
    })

    seeder.add_entity(Services_description, 1, {
        'description_services': lambda x: faker.paragraph(nb_sentences=3),
    })

    #Testimonials
    seeder.add_entity(Testimonials, 5, {
        'photo': lambda x: f'testimonials/testimonials-{faker.random_int(min=1, max=5)}.jpg',
        'name': lambda x: faker.name(),
        'job': lambda x: faker.job(),
        'message': lambda x: faker.sentence(nb_words=50, variable_nb_words=True),
    })

    seeder.add_entity(Testimonials_description, 1, {
        'description_testimonials': lambda x: faker.paragraph(nb_sentences=3),
    })

    #Contact
    seeder.add_entity(Contact, 1, {
        'description_co': lambda x: faker.paragraph(nb_sentences=3),
        'address': lambda x: faker.address(),
        'email': lambda x: faker.email(),
        'phone': lambda x: faker.phone_number(),
    })

    inserted_pks = seeder.execute()
    print(inserted_pks)
