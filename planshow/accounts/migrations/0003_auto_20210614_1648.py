# Generated by Django 3.1.7 on 2021-06-14 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_auto_20210614_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poste', to=settings.AUTH_USER_MODEL),
        ),
    ]
