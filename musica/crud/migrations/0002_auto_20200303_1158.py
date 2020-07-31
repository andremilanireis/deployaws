# Generated by Django 2.2.2 on 2020-03-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'violao'), (2, 'piano'), (3, 'bateria')])),
                ('foto', models.ImageField(blank=True, null=True, upload_to='instrumentos')),
            ],
        ),
        migrations.RemoveField(
            model_name='loja',
            name='imagem',
        ),
        migrations.AddField(
            model_name='loja',
            name='nome',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='loja',
            name='instrumentos',
            field=models.ManyToManyField(blank=True, null=True, to='crud.Instrumento'),
        ),
    ]