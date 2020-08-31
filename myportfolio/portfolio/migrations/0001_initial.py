# Generated by Django 3.1 on 2020-08-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('imagePath', models.CharField(max_length=255)),
                ('imageAlt', models.CharField(max_length=127)),
                ('fullImagePath', models.CharField(max_length=255)),
                ('siteURL', models.CharField(max_length=255)),
                ('gitURL', models.CharField(max_length=255)),
            ],
        ),
    ]
