# Generated by Django 5.0.1 on 2024-01-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/teams')),
            ],
        ),
    ]