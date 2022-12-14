# Generated by Django 4.1.1 on 2022-09-06 14:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('city', models.CharField(blank=True, max_length=80, null=True)),
                ('state', models.CharField(blank=True, max_length=80, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('phone', models.CharField(blank=True, max_length=80, null=True)),
                ('cep', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225, unique=True)),
                ('infos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='institution', to='institutions.institutioninfo')),
            ],
        ),
    ]
