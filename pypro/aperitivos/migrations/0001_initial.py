# Generated by Django 3.0.8 on 2020-07-26 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
                ('titulo', models.CharField(max_length=32)),
                ('vimeo_id', models.CharField(max_length=32)),
            ],
        ),
    ]
