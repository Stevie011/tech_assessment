# Generated by Django 3.2.25 on 2024-05-16 10:49

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('data_frame', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
            ],
        ),
    ]
