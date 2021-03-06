# Generated by Django 3.1.7 on 2021-06-12 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('poste', models.CharField(blank=True, max_length=45, null=True)),
                ('district', models.CharField(blank=True, max_length=45, null=True)),
                ('region', models.CharField(blank=True, max_length=45, null=True)),
                ('logo', models.CharField(blank=True, max_length=45, null=True)),
                ('telephone', models.CharField(blank=True, max_length=45, null=True)),
                ('profile', models.CharField(blank=True, choices=[('icp', 'Infirmier chef de poste'), ('plan', 'Staff Plan'), ('xxx', 'xx')], max_length=255, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accounts_profil',
            },
        ),
    ]
