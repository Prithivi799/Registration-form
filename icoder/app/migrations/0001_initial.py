# Generated by Django 3.0.8 on 2020-07-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('usn', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('branch', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=30)),
            ],
        ),
    ]
