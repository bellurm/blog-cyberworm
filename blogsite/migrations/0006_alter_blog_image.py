# Generated by Django 3.2.9 on 2022-05-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
