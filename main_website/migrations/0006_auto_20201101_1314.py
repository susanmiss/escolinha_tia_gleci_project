# Generated by Django 3.1.2 on 2020-11-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_website', '0005_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diferentials',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='school',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='visitation',
            name='description',
            field=models.TextField(max_length=5000),
        ),
    ]
