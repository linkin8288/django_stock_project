# Generated by Django 4.1.7 on 2023-03-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('shares_owned', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('currency_type', models.CharField(default='stock', max_length=50)),
            ],
        ),
    ]
