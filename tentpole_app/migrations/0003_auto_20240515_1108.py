# Generated by Django 3.2.25 on 2024-05-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tentpole_app', '0002_alter_userdetails_excel_sheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeExpenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('income', models.CharField(max_length=20)),
                ('expenses', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='userdetails',
            name='excel_sheet',
        ),
    ]