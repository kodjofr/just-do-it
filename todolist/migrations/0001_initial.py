# Generated by Django 4.0.5 on 2022-06-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
