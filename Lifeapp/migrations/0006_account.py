# Generated by Django 4.2.8 on 2023-12-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lifeapp', '0005_patientledger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_type', models.CharField(choices=[('Asset', 'Asset'), ('Liability', 'Liability'), ('Equity', 'Equity')], max_length=10)),
                ('account_subtype', models.CharField(choices=[('Current', 'Current'), ('NonCurrent', 'Non-Current')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
