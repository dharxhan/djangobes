# Generated by Django 5.1.3 on 2024-12-06 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('marks', models.FloatField()),
                ('city', models.CharField(max_length=30)),
                ('fees', models.FloatField()),
            ],
        ),
    ]
