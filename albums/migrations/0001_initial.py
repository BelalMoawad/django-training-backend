# Generated by Django 4.1.2 on 2022-11-04 20:07

import albums.models_validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(default='New Album', max_length=30)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('releasing_date', models.DateField()),
                ('album_cost', models.FloatField(blank=True)),
                ('approved', models.BooleanField(default=False, help_text='Approve the album if its name is not explicit')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(default='New Album', max_length=30)),
                ('img', models.ImageField(upload_to='./images/')),
                ('audio_file', models.FileField(upload_to='./audios/', validators=[albums.models_validators.audio_file_validator])),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
            ],
        ),
    ]
