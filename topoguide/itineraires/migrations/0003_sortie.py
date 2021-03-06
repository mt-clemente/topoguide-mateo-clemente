# Generated by Django 4.0.4 on 2022-04-19 16:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itineraires', '0002_alter_itineraire_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sortie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duree', models.DurationField()),
                ('nbParticipants', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('experience', models.IntegerField(choices=[(1, 'Débutants'), (2, 'Mixte'), (3, 'Expérimentés')])),
                ('meteo', models.IntegerField(choices=[(1, 'Mauvaise'), (2, 'Moyenne'), (3, 'Bonne')])),
                ('itineraire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itineraires.itineraire')),
                ('randonneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
