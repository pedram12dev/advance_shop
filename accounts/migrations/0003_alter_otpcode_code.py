# Generated by Django 5.0.1 on 2024-01-24 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.PositiveBigIntegerField(),
        ),
    ]