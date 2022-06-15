# Generated by Django 4.0.4 on 2022-06-12 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0012_remove_profile_bio_comanda_author_comanda_coments_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
