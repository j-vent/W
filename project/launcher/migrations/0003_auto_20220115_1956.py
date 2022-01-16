# Generated by Django 3.2.11 on 2022-01-16 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launcher', '0002_alter_housing_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='housing',
            name='food_provided',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='housing',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='housing',
            name='lgbtq2s_friendly',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='housing',
            name='longitude',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='housing',
            name='public_transit_accessible',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='housing',
            name='showers_provided',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='housing',
            name='wheelchair_accessible',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='housing',
            name='women_only',
            field=models.IntegerField(default=2),
        ),
    ]