# Generated by Django 2.2 on 2021-10-31 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=200)),
                ('Book_Category', models.CharField(max_length=200)),
                ('Book_ISBN', models.CharField(max_length=100)),
                ('Book_Description', models.CharField(max_length=200)),
                ('Book_Rating', models.FloatField()),
                ('Book_Image', models.CharField(max_length=200)),
            ],
        ),
    ]
