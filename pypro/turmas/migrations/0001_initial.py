# Generated by Django 3.0.8 on 2020-08-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
            ],
        ),
    ]
