# Generated by Django 4.1.1 on 2022-09-08 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("works", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("feedbacks", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedbacks",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="feedbacks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="feedbacks",
            name="work",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="feedbacks",
                to="works.work",
            ),
        ),
    ]
