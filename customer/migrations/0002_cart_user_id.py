# Generated by Django 5.0.6 on 2024-12-24 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]