# Generated by Django 2.0.1 on 2018-02-11 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('degree', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
