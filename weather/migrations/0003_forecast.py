# Generated by Django 2.0.4 on 2018-04-20 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20180419_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperatue', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
    ]