# Generated by Django 5.1.3 on 2024-11-14 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan',
            old_name='monthly_repayment',
            new_name='monthly_installment',
        ),
    ]