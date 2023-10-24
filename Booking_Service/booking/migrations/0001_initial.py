# Generated by Django 3.2 on 2021-05-02 01:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('hotel_uid', models.UUIDField(default=uuid.uuid4)),
                ('user_uid', models.UUIDField(default=uuid.uuid4)),
                ('payment_uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('comment', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]