# Generated by Django 4.0.4 on 2022-06-03 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_almuerzo_typ_desayuno_typ_handroll_typ_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bowl',
            name='typ',
            field=models.CharField(default='b', max_length=50),
        ),
    ]
