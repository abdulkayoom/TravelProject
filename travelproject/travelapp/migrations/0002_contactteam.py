# Generated by Django 4.1.7 on 2023-03-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=250)),
                ('cimg', models.ImageField(upload_to='pics')),
                ('cdesc', models.TextField()),
            ],
        ),
    ]
