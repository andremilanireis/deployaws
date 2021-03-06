# Generated by Django 2.2.2 on 2020-03-03 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20200303_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='loja_dona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.Loja'),
        ),
        migrations.AlterField(
            model_name='loja',
            name='instrumentos',
            field=models.ManyToManyField(blank=True, to='crud.Instrumento'),
        ),
    ]
