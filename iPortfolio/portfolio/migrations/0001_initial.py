# Generated by Django 4.2.2 on 2023-06-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description1_ab', models.CharField(blank=True, max_length=200)),
                ('description2_ab', models.CharField(blank=True, max_length=50)),
                ('description3_ab', models.CharField(blank=True, max_length=400)),
                ('job', models.CharField(blank=True, max_length=200)),
                ('birthday', models.DateField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True)),
                ('diploma', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('freelance', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_co', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=150)),
                ('jobs', models.CharField(blank=True, max_length=200, null=True)),
                ('image_hero', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_po', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='portfolio/static/portfolio/img')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(blank=True, choices=[('app', 'App'), ('card', 'Card'), ('web', 'Web')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_se', models.CharField(blank=True, max_length=200)),
                ('icon', models.TextField(blank=True)),
                ('title', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description1_sk', models.CharField(blank=True, max_length=200)),
                ('html', models.IntegerField(blank=True)),
                ('css', models.IntegerField(blank=True)),
                ('js', models.IntegerField(blank=True)),
                ('php', models.IntegerField(blank=True)),
                ('wp', models.IntegerField(blank=True)),
                ('ps', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_te', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('job', models.CharField(blank=True, max_length=50)),
                ('message', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
