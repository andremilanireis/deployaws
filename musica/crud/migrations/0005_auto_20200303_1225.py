# Generated by Django 2.2.2 on 2020-03-03 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20200303_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrumento',
            name='loja_dona',
        ),
        migrations.RemoveField(
            model_name='loja',
            name='instrumentos',
        ),
        migrations.AddField(
            model_name='instrumento',
            name='loja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instrumentos', to='crud.Loja'),
        ),
    ]