# Generated by Django 5.1.3 on 2024-11-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_current_debt'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=False,
        ),
    ]