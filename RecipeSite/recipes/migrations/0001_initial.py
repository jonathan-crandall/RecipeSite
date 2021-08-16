# Generated by Django 3.1.7 on 2021-08-16 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=4000)),
                ('instructions', models.CharField(max_length=4000)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
