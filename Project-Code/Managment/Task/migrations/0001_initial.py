# Generated by Django 4.0.4 on 2023-07-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]