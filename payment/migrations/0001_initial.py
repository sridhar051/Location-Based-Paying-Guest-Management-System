# Generated by Django 3.0.3 on 2020-03-29 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='userdetails',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pno', models.IntegerField()),
                ('room', models.CharField(max_length=100)),
                ('guest', models.CharField(max_length=100)),
                ('adate', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('ddate', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('selhotel', models.CharField(max_length=100)),
            ],
        ),
    ]