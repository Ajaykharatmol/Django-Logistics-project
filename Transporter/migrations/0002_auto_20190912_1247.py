# Generated by Django 2.0 on 2019-09-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('confirm_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Tranporter_Details',
        ),
    ]
