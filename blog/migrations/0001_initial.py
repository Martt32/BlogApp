# Generated by Django 4.0a1 on 2023-06-14 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, null=True)),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('content', models.TextField(max_length=5000000, null=True)),
                ('date', models.DateField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
