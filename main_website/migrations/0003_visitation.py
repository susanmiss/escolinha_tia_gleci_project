# Generated by Django 3.1.2 on 2020-11-01 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0002_diferentials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('phoneNumber', models.CharField(max_length=20)),
            ],
        ),
    ]
